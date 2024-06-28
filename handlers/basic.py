from aiogram import Router, types

from config import history

router = Router()

@router.message(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(history)
