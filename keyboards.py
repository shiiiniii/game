from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_start = KeyboardButton('/start 😎')
btn_help = KeyboardButton('/help 😉')
btn_stop = KeyboardButton('/stop 😔')

kb_main_menu.add(btn_start, btn_help, btn_stop)



