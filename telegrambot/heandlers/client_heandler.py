from createBot import dp, bot
from aiogram import types
from aiogram.filters import Command
from aiogram import Router, Dispatcher
import surrogates


async def cmd_start(message: types.Message):
    await message.answer("Здравствуйте, я телеграмм-бот компании BelStriver. Мы занимаемся строительством домов. С помощью этого бота Вы можете рассчитать стоимость строительства дома. \nДоступные команды:\n/start - Перезапустить бота\n/help - Помощь\n/calculate - Расчиать цену строитальства\n/contacts - Контактная информация")
    


async def help_handler(message: types.Message):
    await message.answer("Доступные команды:\n/start - Перезапустить бота\n/help - Помощь\n/calculate - Расчиать цену строитальства\n/contacts - Контактная информация", reply_markup=types.ReplyKeyboardRemove())


async def contacts(message: types.Message):
    telephon = surrogates.decode('📱')
    email = surrogates.decode('📧')
    adres = surrogates.decode('🗺️')
    await message.answer(f"{telephon}Номер телефона: `+375298258340`\n{email}Email: `belstriver@mail.ru`\n{adres}Адрес: `г.Барановичи ул.Брестская д.159, пом.16`\n", parse_mode="MARKDOWN", reply_markup=types.ReplyKeyboardRemove())



def register_client_heandler(dp : Dispatcher):
    dp.message.register(cmd_start, Command('start'))
    dp.message.register(help_handler, Command('help'))
    dp.message.register(contacts, Command('contacts'))
