from create import dp
from aiogram import types
from keyboards import kb_main_menu


total = 150


@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name} мы будем играть с тобой в конфеты!)', reply_markup=kb_main_menu)



@dp.message_handler(commands=['help'])
async def mes_help(message: types.Message):
    await message.answer('Бот создан для игры с конфетками. Сначала с помощью команды **/set количество конфет** можно '
                         'установить максимальное количество конфет. Потом каждый игрок по очереди будет брать '
                         'определенное количество конфет. Учтите! За раз можно взять не более 28 конфет. Побеждает '
                         'тот, у кого в итоге окажется больше всего конфет)', reply_markup=kb_main_menu)

@dp.message_handler(commands=['set'])
async def mes_settings(message: types.Message):
    global total
    count = int(message.text.split()[1])
    total = count
    await message.answer(f' Максимальное количество конфет установлено - {total}. Теперь вы можете брать конфетки. '
                         f'Введите нужное количество: ')

@dp.message_handler(commands=['stop'])
async def stop(message: types.Message):
    await message.answer('Прощай...')


@dp.message_handler()
async def mes_smth(message: types.Message):
    global total
    if message.text.isdigit() and int(message.text) < 29:
        total -= int(message.text)
        await message.answer(f'На столе осталось {total} конфет')
    else:
        await message.answer('Введите корректное количество конфет')
    if total <= 28:
        await message.answer('Ура! Эта игра окончена!')




@dp.message_handler()
async def mes_all(message: types.Message):
    await message.answer('Поймал все, что летит мимо')

