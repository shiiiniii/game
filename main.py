from aiogram import Bot, Dispatcher, executor, types
from handlers import dp


async def on_start(_):
    print('Бот запущен')




executor.start_polling(dp, skip_updates=True, on_startup=on_start)

