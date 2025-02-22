from aiogram.filters.state import State, StatesGroup


class Wait(StatesGroup):
    first_mes = State()
    second_mes = State()
    third_mes = State()
    fourth_mes = State()
