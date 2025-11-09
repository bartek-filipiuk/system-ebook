"""Tests for prompt manager service."""
import pytest

from app.services.prompt_manager import PromptManager


def test_prompt_manager_initialization():
    """Test prompt manager initializes correctly."""
    manager = PromptManager()
    assert manager.prompts_dir.exists()
    assert manager._cache == {}


def test_load_prompt_smart_detection():
    """Test loading smart detection prompt."""
    manager = PromptManager()
    prompt = manager.load_prompt("smart_detection")

    assert "Project Idea:" in prompt
    assert "use_event_storming" in prompt
    assert "{idea}" in prompt


def test_load_prompt_caching():
    """Test that prompts are cached after first load."""
    manager = PromptManager()

    # First load
    prompt1 = manager.load_prompt("smart_detection")
    assert "smart_detection" in manager._cache

    # Second load should use cache
    prompt2 = manager.load_prompt("smart_detection")
    assert prompt1 == prompt2


def test_load_nonexistent_prompt():
    """Test that loading nonexistent prompt raises error."""
    manager = PromptManager()

    with pytest.raises(FileNotFoundError):
        manager.load_prompt("nonexistent_prompt")


def test_render_prompt():
    """Test rendering prompt with variables."""
    manager = PromptManager()
    rendered = manager.render_prompt("smart_detection", idea="Build a blog platform")

    assert "Build a blog platform" in rendered
    assert "{idea}" not in rendered


def test_get_smart_detection_prompt():
    """Test getting smart detection prompt."""
    manager = PromptManager()
    prompt = manager.get_smart_detection_prompt("Build a todo app")

    assert "Build a todo app" in prompt
    assert "use_event_storming" in prompt


def test_get_init_prompt_without_event_storming():
    """Test getting INIT prompt without event storming."""
    manager = PromptManager()
    prompt = manager.get_init_prompt("Build a blog")

    assert "Build a blog" in prompt
    assert "15 clarifying questions" in prompt
    assert "Event Storming Summary" not in prompt


def test_get_init_prompt_with_event_storming():
    """Test getting INIT prompt with event storming summary."""
    manager = PromptManager()
    event_storming = "# Event Storming Summary\n\nDomain: Blog platform"
    prompt = manager.get_init_prompt("Build a blog", event_storming)

    assert "Build a blog" in prompt
    assert "Event Storming Summary" in prompt
    assert "Domain: Blog platform" in prompt


def test_get_tech_stack_prompt():
    """Test getting tech stack prompt."""
    manager = PromptManager()
    prd = "# PRD\n\n## Requirements\n- Feature A\n- Feature B"
    prompt = manager.get_tech_stack_prompt(prd)

    assert prd in prompt
    assert "Tech Stack Definition" in prompt


def test_get_stages_prompt_horizontal():
    """Test getting stages prompt with horizontal approach."""
    manager = PromptManager()
    prd = "# PRD"
    tech_stack = "# Tech Stack"

    prompt = manager.get_stages_prompt(prd, tech_stack, approach="HORIZONTAL")

    assert "HORIZONTAL" in prompt
    assert "layer-by-layer" in prompt
    assert prd in prompt
    assert tech_stack in prompt


def test_get_stages_prompt_vertical():
    """Test getting stages prompt with vertical approach."""
    manager = PromptManager()
    prd = "# PRD"
    tech_stack = "# Tech Stack"

    prompt = manager.get_stages_prompt(prd, tech_stack, approach="VERTICAL")

    assert "VERTICAL" in prompt
    assert "feature-by-feature" in prompt


def test_get_approach_detection_prompt():
    """Test getting approach detection prompt."""
    manager = PromptManager()
    prd = "# PRD\n\n## Features\n- Auth\n- Dashboard\n- Reports"

    prompt = manager.get_approach_detection_prompt(prd)

    assert prd in prompt
    assert "HORIZONTAL" in prompt
    assert "VERTICAL" in prompt
