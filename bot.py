import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import BOT_TOKEN
from handlers import basic

async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Начать диалог"),
        # BotCommand(command="/hint", description="Выберите посказку")
    ]
    await bot.set_my_commands(commands)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(basic.router)

    await set_commands(bot)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.close()

if __name__ == "__main__":
    asyncio.run(main())
