from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

kb = [
    [InlineKeyboardButton(text="Да", callback_data="Yes")],
    [InlineKeyboardButton(text="Нет", callback_data="No")]
]
