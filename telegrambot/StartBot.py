from createBot import dp, bot
# from aiogram.utils import executor
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import io
from aiogram import Bot, Dispatcher, types
from aiogram import Router
import logging
from aiogram.types.input_file import FSInputFile
from aiogram.types import  ReplyKeyboardMarkup, KeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from utils.excelCreation import createExcelFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router
from aiogram.types import Message
import config
from heandlers.client_heandler import register_client_heandler
from heandlers.fsm_calculate import register_fsm_callback
from heandlers.fsm_callback import register_fsm
from aiogram.fsm.state import StatesGroup, State
import aiogram.utils.markdown as fmt
from aiogram.types import InputFile
import surrogates
from keyboard.keyboards import  keyboardWall, keyboardBack,keyboardSendContact,keyboardAgain,keyboardFacade, keyboardYesNo,keyboardFoundation, keyboardRoof  
from utils.calculate import allSum


async def main():
    await dp.start_polling(bot)

# Создаем роутер
router = Router()
dp.include_router(router)

register_client_heandler(dp)
# register_fsm_callback(dp)
register_fsm(dp)



@router.message()
async def echo_handler(message: Message):
    await message.answer("Доступные команды:\n/start - Перезапустить бота\n/help - Помощь\n/calculate - Расчиать цену строитальства\n/contacts - Контактная информация", reply_markup=types.ReplyKeyboardRemove())




if __name__ == '__main__':
    asyncio.run(main())