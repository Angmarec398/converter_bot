import os
import sys
from unittest.mock import patch

import pytest


def test_bot_token_exists():
    """Проверяет, что BOT_TOKEN существует и не None."""
    from config import BOT_TOKEN
    
    assert BOT_TOKEN is not None, "BOT_TOKEN не должен быть None"


def test_bot_token_not_empty():
    """Проверяет, что BOT_TOKEN не является пустой строкой."""
    from config import BOT_TOKEN
    
    assert BOT_TOKEN, "BOT_TOKEN не должен быть пустой строкой"
    assert len(BOT_TOKEN) > 0, "BOT_TOKEN должен содержать хотя бы один символ"


def test_bot_token_is_string():
    """Проверяет, что BOT_TOKEN является строкой."""
    from config import BOT_TOKEN
    
    assert isinstance(BOT_TOKEN, str), "BOT_TOKEN должен быть строкой"

