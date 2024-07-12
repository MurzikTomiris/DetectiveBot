from aiogram import types, Dispatcher

from db import show_hint_by_id

MAX_HINTS = 23

#hints = [f"Подсказка {i}" for i in range(1, MAX_HINTS + 1)]


async def process_callback_button(callback_query: types.CallbackQuery):
    hint_id = int(callback_query.data.split("_")[1])
    hint = str(show_hint_by_id(hint_id))
    await callback_query.message.answer(hint)


def register_callback_handlers(dp: Dispatcher):
    dp.callback_query.register(
        process_callback_button, lambda c: c.data and c.data.startswith("button")
    )
