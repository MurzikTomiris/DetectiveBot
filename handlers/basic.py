from aiogram import Router, types
from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

from config import history
from db import show_hint_by_id

router = Router()


@router.message(commands=["start"])
async def start_command(message: types.Message):
    await message.reply(
        """Зал для торгов Аукционного дома “Сотбис”
     Участники аукциона заходят в зал и занимают свои места. В зале перешептывание. Кто-то стучит молотком, призывая к тишине.
     Леди Сотби: Доброе утро! Всё готово к аукциону
     (голоса затихают) …
     Сегодняшним аукционом руководит известный оценщик Реджинальд Вебстер. Благодарю, сэр Вебстер. Сегодня с молотка уйдут три лота. Давайте начнём с “Обед у пруда“ Лайма Белдона.
     Двое мужчин выносят большую картину и ставят её на сценуs.
     Леди Сотби: Начальная цена 120 тысяч фунтов.
     Реджинальд Вебстер: Прошу прощения, леди Сотби , вы не могли бы дать мне минуту?
     Леди Сотби: Конечно, сэр Вебстре.
     Все задерживают дыхание, пока Вебстер осматривает картину.
     Реджинальд Вебстер: Торги должны быть остановлены.
     Леди Сотби: Простите?
     Реджинальд Вебстер: Это не “Обед у пруда“ . Это подделка!
     Шёпот нарастает, пока весь зал не заполняется голосами.  """
    )


@router.message(commands=["hint"])
async def send_hint(message: types.Message):
    hint_id = 1
    hint = show_hint_by_id(hint_id)

    # Создаем инлайн-клавиатуру с подсказками
    keyboard = InlineKeyboardMarkup()
    for hint_id, hint_text in hint:
        keyboard.add(InlineKeyboardButton(hint_text, callback_data=f"hint_{hint_id}"))

    await message.reply(hint, reply_markup=keyboard)

