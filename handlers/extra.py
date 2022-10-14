from aiogram import types, Dispatcher
from bot_istance import bot
#
# #Бот будет отвечать тебе что то
async def secret_word1(message: types.Message):
    await message.reply('да мой господин!!!')

async def secret_word2(message:types.Message):
    await message.reply('У Ники будет все хорошо, я уверен она сдаст ОРТ на отлично!)')



# игра кости и прикрепление и бан слов


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(secret_word1, lambda word: "бот" in word.text)#регистрируем бота ответчика
    dp.register_message_handler(secret_word2, lambda word: "скажи мне" in word.text)  # регистрируем бота ответчика







    # elif message.text.lower() in ban_words:
    #     await message.reply('Сообщение удалено так как присутствует не нормативная лексика!')
    #     await bot.delete_message(message.chat.id, message.message_id)

    # else:
    #     await message.answer(message.text)


