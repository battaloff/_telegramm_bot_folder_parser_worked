from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_keyboard():
    buttons = [
        InlineKeyboardButton(text="Готов", callback_data="ready"),
        InlineKeyboardButton(text="Доставлен", callback_data="delivered"),
        InlineKeyboardButton(text="Отменён", callback_data="cancelled"),
    ]

    keyboard = InlineKeyboardMarkup(row_width=3)
    keyboard.add(*buttons)
    return keyboard


