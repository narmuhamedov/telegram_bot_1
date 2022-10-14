import asyncio
import aioschedule


from aiogram import types, Dispatcher

from bot_istance import  bot
async def echo_and_ban(message: types.Message):
    ban_words = ['дурак', 'урод', 'козел', 'сука', 'пидорас', 'еблан', 'гандон', 'bitch',
                 'хуй', 'чмо', 'жопа', 'жопка', 'коза', 'тварь'
                 ]
    # функция будильника
    global chat_id
    chat_id = message.chat.id
    if message.text == "разбуди меня":
        await message.reply("OK мой хозяин!")

    for i in ban_words:
        if i in message.text.lower().replace(" ", ""):
            await message.delete()
            await bot.send_message(message.chat.id, "Сообщение удалено так как присутствует не нормативная лексика!")

    if message.text.lower() == "dice":
        await bot.send_dice(message.chat.id, emoji="🎲")

    elif message.text.startswith("pin"):
        await bot.pin_chat_message(message.chat.id, message.message_id)


async def wake_up():
    await bot.send_message(chat_id=chat_id, text="Проснись хозяин, а то опоздаешь на работу!")


async def schleuder():
    aioschedule.every().day.at("10:21").do(wake_up)

        # aioschedule.cancel_job(wake_up())
    while 1:
        await aioschedule.run_pending()
        await asyncio.sleep(1)



def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(echo_and_ban)