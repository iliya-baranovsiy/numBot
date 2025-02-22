from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from serveses.texts import *
import time
from serveses.keybord import *
from serveses.calculating_func import *
from serveses.states import *
from aiogram.fsm.context import FSMContext

users_dict = {}
router = Router()


@router.message(CommandStart())
async def start_dialog(msg: Message, state: FSMContext):
    id = msg.chat.id
    users_dict[id] = []
    await msg.answer(hello_mes, parse_mode="HTML")
    time.sleep(2)
    await msg.answer("Напиши одно <b>число</b> - день своего рождения 👇 ", parse_mode="HTML")
    await state.set_state(Wait.first_mes)


@router.message(F.text, Wait.first_mes)
async def second_mes(msg: Message, state: FSMContext):
    id = msg.chat.id
    users_dict[id].append(msg.text)
    await msg.answer("Теперь <b>числом</b> введи месяц своего рождения 👇 ", parse_mode="HTML")
    await state.set_state(Wait.second_mes)


@router.message(F.text, Wait.second_mes)
async def third_mes(msg: Message, state: FSMContext):
    id = msg.chat.id
    users_dict[id].append(msg.text)
    await msg.answer("И последний шаг <b>4 цифры</b> года твоего рождения 👇 ", parse_mode="HTML")
    await state.set_state(Wait.third_mes)


@router.message(F.text, Wait.third_mes)
async def fourth_mes(msg: Message, state: FSMContext):
    id = msg.chat.id
    users_dict[id].append(msg.text)
    buttons = InlineKeyboardMarkup(inline_keyboard=kb)
    await msg.answer(
        f"Твоя дата рождения <b>{users_dict[id][0]}.{users_dict[id][1]}.{users_dict[id][2]}</b>\n\n Я права ? 💛",
        reply_markup=buttons, parse_mode="HTML")
    await state.clear()


@router.callback_query(F.data == "Yes")
async def next_step(call: CallbackQuery, state: FSMContext):
    id = call.message.chat.id
    try:
        first = first_calc(users_dict[id][0])
        second = second_calc(users_dict[id][1])
        third = third_calc(users_dict[id][2])
        fourth = fourth_calc(first, second, third)
        answer = str(first) + str(second) + str(third) + str(fourth)
        await call.message.answer(text_2, parse_mode="HTML")
        time.sleep(5)
        await call.message.answer(text_3, parse_mode="HTML")
        time.sleep(5)
        await call.message.answer(answer)
        users_dict[id].clear()
        time.sleep(5)
        await call.message.answer(text_4)
        await call.message.answer_photo(photo=types.FSInputFile(
            "photos and video/d7c5ea07-a5c7-494d-8ac9-b3f8a773a5e3.jpeg"))
    except:
        users_dict[id].clear()
        await call.message.answer("Что-то пошло не так, попробуй ввести дату еще раз")
        await call.message.answer("Напиши одно <b>число</b> - день своего рождения 👇 ", parse_mode="HTML")
        await state.set_state(Wait.first_mes)


@router.callback_query(F.data == "No")
async def wrong_answer(call: CallbackQuery, state: FSMContext):
    id = call.message.chat.id
    users_dict[id].clear()
    await call.message.answer("Давайте попробуем заново")
    await call.message.answer("Напиши одно <b>число</b> - день своего рождения 👇 ", parse_mode="HTML")
    await state.set_state(Wait.first_mes)
