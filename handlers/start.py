from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from sqlalchemy import select

from database.models import User
from database.session import SessionLocal

router = Router()


async def _get_user(user_id: int) -> User | None:
    async with SessionLocal() as session:
        return await session.scalar(select(User).where(User.id == user_id))


@router.message(CommandStart())
async def cmd_start(message: Message):
    user = await _get_user(message.from_user.id)
    if not user:
        await message.answer("Привет, я тебя не узнал. Напиши @it_cifraz чтобы тебе дали доступ")
        return

    await message.answer(
        f"Здраствуй {user.name}! Пришли .xlsx файл, я сконвертирую его в CSV."
    )

