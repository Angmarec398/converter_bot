import pytest
from sqlalchemy import text

from database.session import SessionLocal, engine
from database.models import Base


@pytest.mark.asyncio
async def test_database_connection():
    """Проверяет подключение к базе данных."""
    # Проверяем, что движок создан
    assert engine is not None, "Движок БД должен быть создан"
    
    # Проверяем подключение через выполнение простого запроса
    async with engine.begin() as conn:
        result = await conn.execute(text("SELECT 1"))
        row = result.fetchone()
        assert row[0] == 1, "Запрос должен вернуть 1"


@pytest.mark.asyncio
async def test_database_session():
    """Проверяет создание сессии и выполнение простого запроса."""
    async with SessionLocal() as session:
        # Выполняем простой запрос через сессию
        result = await session.execute(text("SELECT 1 as test"))
        row = result.fetchone()
        assert row.test == 1, "Запрос через сессию должен вернуть 1"


@pytest.mark.asyncio
async def test_database_tables_exist():
    """Проверяет, что таблицы созданы в БД."""
    async with engine.begin() as conn:
        # Проверяем наличие таблиц
        result = await conn.execute(text(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ))
        tables = [row[0] for row in result.fetchall()]
        
        # Проверяем наличие необходимых таблиц
        assert "motivation" in tables, "Таблица 'motivation' должна существовать"
        assert "user" in tables, "Таблица 'user' должна существовать"


@pytest.mark.asyncio
async def test_database_can_query_motivation_table():
    """Проверяет, что можно выполнить запрос к таблице motivation."""
    from database.models import Motivation
    
    async with SessionLocal() as session:
        # Пытаемся выполнить запрос к таблице motivation
        from sqlalchemy import select
        result = await session.execute(select(Motivation).limit(1))
        # Запрос должен выполниться без ошибок
        _ = result.fetchall()


@pytest.mark.asyncio
async def test_database_can_query_user_table():
    """Проверяет, что можно выполнить запрос к таблице user."""
    from database.models import User
    
    async with SessionLocal() as session:
        # Пытаемся выполнить запрос к таблице user
        from sqlalchemy import select
        result = await session.execute(select(User).limit(1))
        # Запрос должен выполниться без ошибок
        _ = result.fetchall()

