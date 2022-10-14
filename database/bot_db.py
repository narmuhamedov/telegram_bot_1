import sqlite3
from bot_istance import bot
#файл для базы данных в пакете database

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()
    if db:
        print("Database connect.....")
    db.execute("CREATE TABLE IF NOT EXISTS anime (img TEXT, title TEXT PRIMARY KEY, description TEXT )")
    db.commit()

async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO anime VALUES (?, ?, ?)", tuple(data.values()))
        db.commit()

#команда для отображения результата
async def sql_command_select(message):
    for result in cursor.execute("SELECT * FROM anime").fetchall():
        await bot.send_photo(message.from_user.id, result[0],
                             caption=f'Заголовок: {result[1]}\n'
                               f'Описание:{result[2]}\n')

async def sql_casual_select():
    return cursor.execute('SELECT * FROM anime').fetchall()

#команда для удаления
async def sql_command_delete(data):
    cursor.execute("DELETE FROM anime WHERE title == ?", (data,))
    db.commit()
