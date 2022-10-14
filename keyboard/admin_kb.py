from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_download = KeyboardButton("/download")
button_delete = KeyboardButton("/delete")
button_show_all = KeyboardButton("/show_all")
button_cancel = KeyboardButton("/cancel")

button_admin  = ReplyKeyboardMarkup(resize_keyboard=True).add(button_delete,button_download,button_show_all, button_cancel)
