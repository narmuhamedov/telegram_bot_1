from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button_start = KeyboardButton("/start")
button_quiz = KeyboardButton("/quiz")
button_tasks = KeyboardButton("/tasks")
button_game = KeyboardButton('dice')
button_location = KeyboardButton("Share Location", request_location=True)
button_info = KeyboardButton("Share Info", request_contact=True)


keyboard_stat = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4, one_time_keyboard=True)

keyboard_stat.add(button_start,button_quiz, button_tasks, button_info,
                  button_location,button_game)