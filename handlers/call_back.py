from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from aiogram.types import ParseMode
from bot_istance import bot


async def task_1(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('next task', callback_data='next_task2')
    markup.add(button_call_2)
    question2 = "Output:"
    answer = ["Буква 'e' ", "Что то",
              "Незнаю", "Взорвался мозг"]
    img = open("media/q2.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=img)
    await bot.send_poll(
        call.message.chat.id,
        question=question2,
        options=answer,
        is_anonymous=False,
        correct_option_id=0,
        open_period=20,
        explanation='Подумай глупенький',
        type="quiz",
        reply_markup=markup
    )


async def task_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("next task", callback_data="next_task3")
    markup.add(button_call_3)
    question3 = "Output:"
    answer = ["Буква 'e' ", "Что то",
              "Незнаю", "Одна собака и одна кошка"]
    img = open("media/q3.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=img)
    await bot.send_poll(
        call.message.chat.id,
        question=question3,
        options=answer,
        is_anonymous=False,
        correct_option_id=3,
        open_period=20,
        explanation='Подумай глупенький',
        type="quiz",
        reply_markup=markup
    )

async def task_3(call:types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("next task", callback_data='next_task4')
    markup.add(button_call_4)
    question4 = "Что изображено на картике"
    answer = ["Вова рисует дом", "Леша дерево", "Вова рисует дом а леша дерево"]
    img = open("media/q4.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=img)
    await bot.send_poll(
        call.message.chat.id,
        question=question4,
        options=answer,
        is_anonymous=False,
        correct_option_id=2,
        open_period=20,
        explanation='Подумай глупенький',
        type="quiz",
        reply_markup=markup
    )


async def task_4(call:types.CallbackQuery):
    question5 = "Что можно увидеть закрытыми глазами"
    answer = ["Сон", "Храп", "Андройд"]
    img = open("media/q5.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=img)
    await bot.send_poll(
        call.message.chat.id,
        question=question5,
        options=answer,
        is_anonymous=False,
        correct_option_id=0,
        open_period=20,
        explanation='Подумай глупенький',
        type="quiz"
    )









def register_handlers_callback(dp: Dispatcher):
    # прописываем через лямбда функцию для отображения задачи при клике на кнопку 1, а так же добавили кнопку для отображения следующей викторины
    # обязательно указываем уникальное название
    dp.register_callback_query_handler(task_1,lambda func: func.data == "next_task1")
    # все тоже самое как под номером 1
    # обязательно указываем уникальное название
    dp.register_callback_query_handler(task_2, lambda func: func.data == "next_task2")
    # обязательно указываем уникальное название
    dp.register_callback_query_handler(task_3, lambda func: func.data == "next_task3")
    # обязательно указываем уникальное название
    dp.register_callback_query_handler(task_4, lambda func: func.data == "next_task4")