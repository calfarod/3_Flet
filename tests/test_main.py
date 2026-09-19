import pytest
from unittest.mock import MagicMock
import flet as ft
from src.main import main


@pytest.mark.asyncio
async def test_increment():
    # Oñembosako'i peteĩ mock sesión rehegua
    mock_session = MagicMock()
    page = ft.Page(mock_session)
    
    # Oñemboguatata main función
    main(page)

    # Ojehecha oĩpa nyryty ha ipyenda
    assert len(page.controls) > 0

    # Ojeheka mba'eichapa oĩ pe text inicial ("0")
    safe_area = page.controls[0]
    counter_text = safe_area.content.content
    assert counter_text.value == "0"

    # Oñeha'ã oñembotapykue pe botón
    page.floating_action_button.on_click(MagicMock())

    # Ojehecha oñemoambuepa ("1")
    assert counter_text.value == "1"