from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from bot_istance import dp, bot
from database import bot_db
from keyboard import keyboard
from parser import tv_show


# bot say hello .... (your name)
async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello my master: {message.from_user.full_name}",
                           reply_markup=keyboard.keyboard_stat)

#quiz bot
async def quiz_1(message: types.Message):
    question = "Who are you?"
    answer = ["Girl", "Boy", "I don't know"]
    await bot.send_poll(message.chat.id,
                        question=question,
                        options=answer,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1, #правильный ответ
                        open_period=5,#время для опроса
                        explanation="This is easy quiz1",#подсказка
                        explanation_parse_mode=ParseMode.MARKDOWN_V2
                        )

    question2 = "What are you doing now?"
    answer2 = ["Sleep", "Work", "I don't know"]
    await bot.send_poll(message.chat.id,
                        question=question2,
                        options=answer2,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=1,
                        open_period=5,
                        explanation="This is easy quiz2",
                        explanation_parse_mode=ParseMode.MARKDOWN_V2
                        )

    question3 = "How old are you?"
    answer3 = ["12 y.o", "22 y.o", "19 y.o"]
    await bot.send_poll(message.chat.id,
                        question=question3,
                        options=answer3,
                        is_anonymous=False,
                        type='quiz',
                        correct_option_id=2,
                        open_period=10,
                        explanation="This is easy quiz3",
                        explanation_parse_mode=ParseMode.MARKDOWN_V2
                        )

# Задачки
async def task_1(message: types.Message):
    #регистрируем нашу кнопку
    markup = InlineKeyboardMarkup()
    #кнопка для регистрации а так же для отображения в боте
    button_call_1 =  InlineKeyboardButton('next task',
                                          callback_data='next_task1')
    markup.add(button_call_1)

    question1 = "Output:"
    answer = ["Белый медведь", "Черный медведь",
              "Красный медведь", "Загорелый"]
    #загрузка картинок для викторины
    img = open("media/q1.jpg", "rb")
    await bot.send_photo(message.chat.id, photo=img)

    await bot.send_poll(
        message.chat.id,
        question=question1,
        options=answer,
        is_anonymous=False,
        correct_option_id=0,
        open_period=20,
        explanation='Такое возможно только на Северном полюсе',
        type="quiz",
        reply_markup=markup #кнопка для отображения
    )


async def show_all_anime_command(message: types.Message):
    await bot_db.sql_command_select(message)

#for parser
async def parser_manas_film(message: types.Message):
    data = tv_show.parser()
    for i in data:
        await bot.send_message(message.chat.id, i)
    #await bot.send_message(message.chat.id, data)




#Регистрируем наши хэндлеры
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])#команда для запуска
    dp.register_message_handler(task_1, commands=['tasks'])  # команда для запуска
    dp.register_message_handler(show_all_anime_command, commands=['show_all'])
    dp.register_message_handler(parser_manas_film, commands=['parser'])



# echo bot code
# @dp.message_handler()
# async def echo_message(message: types.Message):
#     await message.answer(message.text)
