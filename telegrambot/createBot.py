from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.fsm.storage.memory import MemoryStorage
import  config
import os

storage1 = MemoryStorage()
# Initialize bot and dispatcher
bot = Bot(token="6786203938:AAFfC6aqTBeCWauIUsgNvMw0N6ftu1Qa5M0")
dp = Dispatcher(storage=storage1)