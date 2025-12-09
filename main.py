import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from database.init_db import init_db
from handlers.file import router as file_router
from handlers.other import router as other_router
from handlers.start import router as start_router


logging.basicConfig(level=logging.INFO)


async def main():
    await init_db()

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(file_router)
    dp.include_router(other_router)

    try:
        await dp.start_polling(bot)
    except (KeyboardInterrupt, asyncio.CancelledError):
        logging.info("Получен сигнал остановки, завершаем работу бота...")
    finally:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())

