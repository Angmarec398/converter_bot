from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from services.utils import _is_allowed, _other_random_quote

router = Router()


@router.message(~F.document, ~CommandStart())
async def handle_unknown(message: Message):
    if not await _is_allowed(message.from_user.id):
        await message.answer("Привет, я тебя не узнал")
        return

    quote = await _other_random_quote()
    await message.answer(
        f"Извини, я тебя не понял. Но вот тебе цитата на сегодня:\n{quote}"
    )
