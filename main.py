import asyncio
from aiogram import executor
from bot_istance import dp
from handlers import client, call_back, extra, fsmadmin, notification
from database import bot_db
from handlers.notification import schleuder
#
async def on_startup(_):
    bot_db.sql_create()
    asyncio.create_task(schleuder())
    print("Бот онлайн")


fsmadmin.register_handlers_fsmadmin(dp)
client.register_handlers_client(dp)
call_back.register_handlers_callback(dp)
extra.register_handlers_extra(dp)
notification.register_handlers_notification(dp)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup)



