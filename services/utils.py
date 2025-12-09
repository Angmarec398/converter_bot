from sqlalchemy import func, select

from database.models import Motivation, User
from database.session import SessionLocal


async def _is_allowed(user_id: int) -> bool:
    """Проверяет, зарегистрирован ли пользователь в базе."""
    async with SessionLocal() as session:
        result = await session.scalar(select(User.id).where(User.id == user_id))
        return result is not None


async def _get_random_quote() -> str:
    """Возвращает случайную мотивирующую цитату или сообщение об отсутствии."""
    async with SessionLocal() as session:
        result = await session.scalar(
            select(Motivation).order_by(func.random()).limit(1)
        )
        if result:
            author = result.author or "Автор неизвестен"
            return (
                "<b>Держи новый файл. И вот тебе мотивирующая цитата на сегодня:</b>"
                f"<b>«{result.text}.»</b>\n<i>{author}</i>"
            )
    return "<b>Цитата не найдена</b>"

async def _other_random_quote() -> str:
    """Возвращает случайную мотивирующую цитату или сообщение об отсутствии."""
    async with SessionLocal() as session:
        result = await session.scalar(
            select(Motivation).order_by(func.random()).limit(1)
        )
        if result:
            author = result.author or "Автор неизвестен"
            return (
                f"<b>«{result.text}.»</b>\n<i>{author}</i>"
            )
    return "<b>Цитата не найдена</b>"