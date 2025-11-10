"""OpenRouter LLM service for making API calls."""
import json
import time
from typing import Any, Dict, Optional

import httpx

from app.config import settings


class LLMResponse:
    """Response from LLM API call."""

    def __init__(
        self,
        content: str,
        model: str,
        usage: Dict[str, int],
        cost_usd: float,
        latency_ms: int,
        raw_response: Dict[str, Any],
    ):
        self.content = content
        self.model = model
        self.usage = usage  # {"prompt_tokens": X, "completion_tokens": Y, "total_tokens": Z}
        self.cost_usd = cost_usd
        self.latency_ms = latency_ms
        self.raw_response = raw_response


class LLMService:
    """Service for interacting with OpenRouter API."""

    # Model pricing per 1M tokens (approximate, update as needed)
    # Format: {"model_name": {"input": price, "output": price}}
    MODEL_PRICING = {
        "openai/gpt-4o-mini": {"input": 0.150, "output": 0.600},
        "openai/gpt-4o": {"input": 2.50, "output": 10.00},
        "anthropic/claude-3.5-sonnet": {"input": 3.00, "output": 15.00},
        "anthropic/claude-3-haiku": {"input": 0.25, "output": 1.25},
    }

    def __init__(self):
        self.base_url = settings.OPENROUTER_BASE_URL
        self.api_key = settings.OPENROUTER_API_KEY
        self.client = httpx.AsyncClient(timeout=120.0)

    async def call(
        self,
        model: str,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4000,
        response_format: Optional[Dict[str, str]] = None,
        system_message: Optional[str] = None,
    ) -> LLMResponse:
        """Make an LLM API call via OpenRouter.

        Args:
            model: Model identifier (e.g., "openai/gpt-4o-mini")
            prompt: User prompt
            temperature: Sampling temperature (0.0-1.0)
            max_tokens: Maximum tokens to generate
            response_format: Optional response format (e.g., {"type": "json_object"})
            system_message: Optional system message

        Returns:
            LLMResponse with content, usage, and cost

        Raises:
            httpx.HTTPError: If API call fails

        """
        start_time = time.time()

        # Build messages
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})

        # Build request payload
        payload = {
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }

        # Add response format if specified (for JSON mode)
        if response_format:
            payload["response_format"] = response_format

        # Make API call
        response = await self.client.post(
            f"{self.base_url}/chat/completions",
            json=payload,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                "HTTP-Referer": settings.PROJECT_NAME,
            },
        )
        response.raise_for_status()

        # Parse response
        data = response.json()
        latency_ms = int((time.time() - start_time) * 1000)

        # Extract content
        content = data["choices"][0]["message"]["content"]

        # Extract usage
        usage = {
            "prompt_tokens": data["usage"]["prompt_tokens"],
            "completion_tokens": data["usage"]["completion_tokens"],
            "total_tokens": data["usage"]["total_tokens"],
        }

        # Calculate cost
        cost_usd = self._calculate_cost(model, usage)

        return LLMResponse(
            content=content,
            model=model,
            usage=usage,
            cost_usd=cost_usd,
            latency_ms=latency_ms,
            raw_response=data,
        )

    def _calculate_cost(self, model: str, usage: Dict[str, int]) -> float:
        """Calculate cost in USD based on token usage.

        Args:
            model: Model identifier
            usage: Token usage dict

        Returns:
            Cost in USD

        """
        # Get pricing for model (default to GPT-4o pricing if unknown)
        pricing = self.MODEL_PRICING.get(
            model, {"input": 2.50, "output": 10.00}  # Default to GPT-4o pricing
        )

        # Calculate cost (pricing is per 1M tokens)
        input_cost = (usage["prompt_tokens"] / 1_000_000) * pricing["input"]
        output_cost = (usage["completion_tokens"] / 1_000_000) * pricing["output"]

        return round(input_cost + output_cost, 6)

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()


# Global instance
llm_service = LLMService()
