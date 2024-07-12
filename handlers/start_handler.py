from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from config import history


async def start_command(message: types.Message):
    BUTTONS_PER_ROW = 5
    MAX_BUTTONS = 23
    # Создаем список кнопок
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{row * BUTTONS_PER_ROW + col}",
                callback_data=f"button_{row * BUTTONS_PER_ROW + col}",
            )
            for col in range(1, BUTTONS_PER_ROW + 1)
        ]
        for row in range(0, MAX_BUTTONS // BUTTONS_PER_ROW + 1)
    ]

    # Обрезаем кнопки, если они больше максимального количества
    buttons[MAX_BUTTONS // BUTTONS_PER_ROW] = buttons[MAX_BUTTONS // BUTTONS_PER_ROW][
                                              :
                                              MAX_BUTTONS % BUTTONS_PER_ROW
                                              ]

    keyboard = InlineKeyboardMarkup(
        type="inline", row_width=BUTTONS_PER_ROW, inline_keyboard=[*buttons]
    )

    await message.reply(f"{history} \nВыберите подсказку:", reply_markup=keyboard)


def register_start_handlers(dp: Dispatcher):
    dp.message.register(start_command, Command(commands=["start"]))
