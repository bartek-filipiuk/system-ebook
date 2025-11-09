"""Tests for LLM service."""
import pytest
from unittest.mock import AsyncMock, Mock, patch

from app.services.llm_service import LLMResponse, LLMService


@pytest.fixture
def mock_openrouter_response():
    """Mock OpenRouter API response."""
    return {
        "choices": [
            {
                "message": {
                    "content": "This is a test response from the LLM."
                }
            }
        ],
        "usage": {
            "prompt_tokens": 100,
            "completion_tokens": 50,
            "total_tokens": 150,
        },
    }


@pytest.mark.asyncio
async def test_llm_service_initialization():
    """Test LLM service initializes correctly."""
    service = LLMService()
    assert service.base_url is not None
    assert service.client is not None


@pytest.mark.asyncio
async def test_llm_call_success(mock_openrouter_response):
    """Test successful LLM API call."""
    service = LLMService()

    # Mock the HTTP client
    with patch.object(service.client, "post") as mock_post:
        # Create mock response
        mock_response = Mock()
        mock_response.json.return_value = mock_openrouter_response
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        # Make call
        result = await service.call(
            model="openai/gpt-4o-mini",
            prompt="Test prompt",
            temperature=0.7,
        )

        # Verify result
        assert isinstance(result, LLMResponse)
        assert result.content == "This is a test response from the LLM."
        assert result.model == "openai/gpt-4o-mini"
        assert result.usage["prompt_tokens"] == 100
        assert result.usage["completion_tokens"] == 50
        assert result.usage["total_tokens"] == 150
        assert result.cost_usd > 0
        assert result.latency_ms >= 0


@pytest.mark.asyncio
async def test_llm_call_with_system_message(mock_openrouter_response):
    """Test LLM call with system message."""
    service = LLMService()

    with patch.object(service.client, "post") as mock_post:
        mock_response = Mock()
        mock_response.json.return_value = mock_openrouter_response
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        await service.call(
            model="openai/gpt-4o-mini",
            prompt="Test prompt",
            system_message="You are a helpful assistant",
        )

        # Verify system message was included
        call_args = mock_post.call_args
        payload = call_args.kwargs["json"]
        assert len(payload["messages"]) == 2
        assert payload["messages"][0]["role"] == "system"
        assert payload["messages"][1]["role"] == "user"


@pytest.mark.asyncio
async def test_llm_call_with_json_mode(mock_openrouter_response):
    """Test LLM call with JSON response format."""
    service = LLMService()

    # Update mock response to be JSON
    mock_openrouter_response["choices"][0]["message"]["content"] = '{"result": "test"}'

    with patch.object(service.client, "post") as mock_post:
        mock_response = Mock()
        mock_response.json.return_value = mock_openrouter_response
        mock_response.raise_for_status = Mock()
        mock_post.return_value = mock_response

        result = await service.call(
            model="openai/gpt-4o-mini",
            prompt="Test prompt",
            response_format={"type": "json_object"},
        )

        # Verify response format was included
        call_args = mock_post.call_args
        payload = call_args.kwargs["json"]
        assert "response_format" in payload
        assert payload["response_format"]["type"] == "json_object"


def test_calculate_cost():
    """Test cost calculation."""
    service = LLMService()

    usage = {
        "prompt_tokens": 1000,
        "completion_tokens": 500,
        "total_tokens": 1500,
    }

    # Test with GPT-4o-mini (known pricing)
    cost = service._calculate_cost("openai/gpt-4o-mini", usage)
    assert cost > 0
    assert isinstance(cost, float)

    # Cost should be: (1000/1M * 0.150) + (500/1M * 0.600)
    expected_cost = (1000 / 1_000_000 * 0.150) + (500 / 1_000_000 * 0.600)
    assert abs(cost - expected_cost) < 0.000001


def test_calculate_cost_unknown_model():
    """Test cost calculation for unknown model uses default pricing."""
    service = LLMService()

    usage = {
        "prompt_tokens": 1000,
        "completion_tokens": 500,
        "total_tokens": 1500,
    }

    # Unknown model should use default pricing (GPT-4o)
    cost = service._calculate_cost("unknown/model", usage)
    assert cost > 0


@pytest.mark.asyncio
async def test_llm_service_close():
    """Test closing LLM service."""
    service = LLMService()

    with patch.object(service.client, "aclose") as mock_close:
        await service.close()
        mock_close.assert_called_once()
