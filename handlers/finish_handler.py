from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def start_command(message: types.Message):
    MAX_BUTTONS = 6

    suspend_buttons = [
        [
            InlineKeyboardButton(
                text=f"{id}",
                callback_data=f"suspend_button_{id}",
            )
        ]
        for id in range(0, MAX_BUTTONS)
    ]

    keyboard = InlineKeyboardMarkup(
        type="inline", inline_keyboard=[*suspend_buttons]
    )

    await message.reply("Выберите подозреваемого:", reply_markup=keyboard)


def register_finish_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=["finish"]))
