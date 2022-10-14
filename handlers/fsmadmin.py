from aiogram import types,Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from database import bot_db
from bot_istance import dp, bot
from keyboard import admin_kb

#Создаем фазу что за чем идет
class FSADMIN(StatesGroup):
    photo = State()
    title = State()
    description = State()

#Запрос для бота пишем в групповом чате
async def is_admin_func(message:types.Message):
    global ADMIN_ID
    ADMIN_ID = message.from_user.id
    await bot.send_message(message.from_user.id, "Админ что ты хочешь?",
                           reply_markup=admin_kb.button_admin)

#Кнопка отмены добавления данных в БД
async def cancel_handler(message:types.Message, state:FSMContext):
    if message.from_user.id == ADMIN_ID:
        current_state = await state.get_state()
        await state.finish()
        await message.reply('Отмена удачно отменена')


#После того как все сработало отправляем фото
async def fsm_start(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        await FSADMIN.photo.set()
        await message.reply("Админ отправь мне фото пожалуйста!!!")

#Процесс загрузки фото
async def load_photo(message: types.Message,
                     state: FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy() as data:
            data["photo"] = message.photo[0].file_id
            #После процесса фото идет шаг следующий процесс описания к фото
        await FSADMIN.next()
        await message.reply("Админ отправь описание к фото")

#Процесс описания к фото
async def load_title(message: types.Message,
                     state:FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy()as data:
            data['title'] = message.text
            # После процесса описания к фото идет процесс описания полностью коого либо
        await FSADMIN.next()
        await message.reply('Отправь мне описание пожалуйста!!!')

#Процесс общего описания
async def load_desc(message: types.Message,state:FSMContext):
    if message.from_user.id == ADMIN_ID:
        async with state.proxy()as data:
            data['description'] = message.text
        # async with state.proxy()as data:
        #     await message.reply(str(data))
        #Через подключение к БД отдаем все данные и получаем результат
        await bot_db.sql_command_insert(state)
            #получаем результат
        await state.finish()

#для удаления функция
async def complete_delete(call: types.CallbackQuery):
    await bot_db.sql_command_delete(call.data.replace("delete ", ""))
    await call.answer(text=f"{call.data.replace('delete ', '')} deleted", show_alert=True)


#для отображения что удалить
async def delete_data(message: types.Message):
    if message.from_user.id == ADMIN_ID:
        inserting = await bot_db.sql_casual_select()
        for result in inserting:
            await bot.send_photo(message.from_user.id, result[0],
                                 caption=f'Заголовок: {result[1]}\n'
                                         f'Описание:{result[2]}\n',
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
                                     f'Удалить: {result[1]}',
                                     callback_data=f'delete {result[1]}'
                                 )))


def register_handlers_fsmadmin(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['download'], state=None)
    #регистрация для отмены в любом формате
    dp.register_message_handler(cancel_handler, state="*", commands="cancel")
    #конец регистрации отмены в любом формате
    dp.register_message_handler(cancel_handler, Text(equals="cancel", ignore_case=True), state="*")
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSADMIN.photo)
    dp.register_message_handler(load_title, state=FSADMIN.title)
    dp.register_message_handler(load_desc, state=FSADMIN.description)
    dp.register_message_handler(is_admin_func, commands=['admin'], is_chat_admin=True)
    #для удаления
    dp.register_callback_query_handler(complete_delete, lambda call: call.data and call.data.startswith('delete '))
    dp.register_message_handler(delete_data, commands=['delete'])