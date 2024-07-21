from aiogram.fsm.state import StatesGroup, State
from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboard.inlineKeyboards import YesOrNo, createKeyboard
from keyboard.keyboards import keyboardSendContact
from createBot import bot
from utils.calculate import allSum

# Состояния
class Form(StatesGroup):
    name = State()
    numberStoreys = State()
    square = State()
    mansard = State()
    WallMaterial = State()
    RoofMaterial = State()
    FoundationMaterial = State()
    FacadeMaterial = State()
    number = State()
    confirm = State()

# Обработчик команды /form
async def form_start(message: Message, state: FSMContext):
    await state.update_data(numberStoreys=None)
    await state.update_data(square=None)
    await state.update_data(mansard=None)
    await state.update_data(WallMaterial=None)
    await state.update_data(RoofMaterial=None)
    await state.update_data(FoundationMaterial=None)
    await state.update_data(FacadeMaterial=None)
    await state.update_data(name=None)
    await state.update_data(number=None)
    user_data = await state.get_data()
    await message.answer("Давайте начнем!\nУкажите этажность вашего будущего дома", reply_markup=createKeyboard("numberStoreys", user_data, True), one_time_keyboard=False)
    await state.set_state(Form.numberStoreys)
    

async def process_numberStoreys(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback.data == "Далее":
        await callback.message.edit_text("Укажите примерную площадь дома", reply_markup=createKeyboard("square", user_data))
        await state.set_state(Form.square)
    else:
        await state.update_data(numberStoreys=callback.data)
        await callback.message.edit_text("Укажите примерную площадь дома", reply_markup=createKeyboard("square", user_data))
        await state.set_state(Form.square)
        print(user_data)

async def process_square(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback.data == "Назад":
        await callback.message.edit_text("Укажите этажность вашего будущего дома", reply_markup=createKeyboard("numberStoreys", user_data, True), one_time_keyboard=False)
        await state.set_state(Form.numberStoreys)
    elif callback.data == "Далее":
        await callback.message.edit_text("Будет ли мансардный этаж", reply_markup=createKeyboard("mansard", user_data, True))
        await state.set_state(Form.mansard)
    else:
        await state.update_data(square=callback.data)
        await callback.message.edit_text("Будет ли мансардный этаж", reply_markup=createKeyboard("mansard", user_data, True))
        await state.set_state(Form.mansard)
        print(user_data)


async def process_mansard(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback.data == "Назад":
        await callback.message.edit_text("Укажите примерную площадь дома", reply_markup=createKeyboard("square", user_data))
        await state.set_state(Form.square)
    elif callback.data == "Далее":
        await callback.message.edit_text("Выберите тип кладки стен", reply_markup=createKeyboard("WallMaterial", user_data))
        await state.set_state(Form.WallMaterial)
    else:
        await state.update_data(mansard=callback.data)
        await callback.message.edit_text("Выберите тип кладки стен", reply_markup=createKeyboard("WallMaterial", user_data))
        await state.set_state(Form.WallMaterial)
        print(user_data)


async def process_WallMaterial(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback.data == "Назад":
        await callback.message.edit_text("Будет ли мансардный этаж", reply_markup=createKeyboard("mansard", user_data, True))
        await state.set_state(Form.mansard)
    elif callback.data == "Далее":
        await callback.message.edit_text("Выберите тип кровли", reply_markup=createKeyboard("RoofMaterial", user_data))
        await state.set_state(Form.RoofMaterial)
    else:
        await state.update_data(WallMaterial=callback.data)
        await callback.message.edit_text("Выберите тип кровли", reply_markup=createKeyboard("RoofMaterial", user_data))
        await state.set_state(Form.RoofMaterial)
        print(user_data)


async def process_RoofMaterial(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback.data == "Назад":
        await callback.message.edit_text("Выберите тип кладки стен", reply_markup=createKeyboard("WallMaterial", user_data))
        await state.set_state(Form.WallMaterial)
    elif callback.data == "Далее":
        await callback.message.edit_text("Выберите тип фундамента", reply_markup=createKeyboard("FoundationMaterial", user_data))
        await state.set_state(Form.FoundationMaterial)
    else:
        await state.update_data(RoofMaterial=callback.data)
        
        await callback.message.edit_text("Выберите тип фундамента", reply_markup=createKeyboard("FoundationMaterial", user_data))
        await state.set_state(Form.FoundationMaterial)
        print(user_data)


async def process_FoundationMaterial(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback.data == "Назад":
        await callback.message.edit_text("Выберите тип кровли", reply_markup=createKeyboard("RoofMaterial", user_data))
        await state.set_state(Form.RoofMaterial)
    elif callback.data == "Далее":
        await callback.message.edit_text("Выберите тип фасада", reply_markup=createKeyboard("FacadeMaterial", user_data))
        await state.set_state(Form.FacadeMaterial)
    else:
        await state.update_data(FoundationMaterial=callback.data)
        await callback.message.edit_text("Выберите тип фасада", reply_markup=createKeyboard("FacadeMaterial", user_data))
        await state.set_state(Form.FacadeMaterial)
        print(user_data)


async def process_FacadeMaterial(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    if callback.data == "Назад":
        await callback.message.edit_text("Выберите тип фундамента", reply_markup=createKeyboard("FoundationMaterial", user_data))
        await state.set_state(Form.FoundationMaterial)
    elif callback.data == "Далее":
        # await state.update_data(FacadeMaterial=callback.data)
        user_data2 = await state.get_data()
        await callback.message.edit_text(f'Количество этажей: {user_data2["numberStoreys"]} \nПлощадь: {user_data2["square"]} \nМансардный этаж: {user_data2["mansard"]} \nМатериал стен: {user_data2["WallMaterial"]} \nТип кровли: {user_data2["RoofMaterial"]} \nТип фундамента: {user_data2["FoundationMaterial"]} \nФасад: {user_data2["FacadeMaterial"]} \nВсё верно? (да/нет)', reply_markup=YesOrNo)
        await state.set_state(Form.confirm)
    else:
        await state.update_data(FacadeMaterial=callback.data)
        user_data2 = await state.get_data()
        await callback.message.edit_text(f'Количество этажей: {user_data2["numberStoreys"]} \nПлощадь: {user_data2["square"]} \nМансардный этаж: {user_data2["mansard"]} \nМатериал стен: {user_data2["WallMaterial"]} \nТип кровли: {user_data2["RoofMaterial"]} \nТип фундамента: {user_data2["FoundationMaterial"]} \nФасад: {user_data2["FacadeMaterial"]} \nВсё верно? (да/нет)', reply_markup=YesOrNo)
        await state.set_state(Form.confirm)
        print(user_data)


async def process_confirm(callback: CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    print(user_data)
    if callback.data == "Да":
        await callback.message.edit_text(f"Результат расчета\n{allSum(user_data)} у.е.")
        await callback.message.answer("Отправтье ваши контакты и мы свяжемся с вами в ближайшее время", reply_markup=keyboardSendContact)
        await state.set_state(Form.number)
    else:
        await callback.message.edit_text("Укажите этажность вашего будущего дома", reply_markup=createKeyboard("numberStoreys", user_data, True), one_time_keyboard=False)
        await state.set_state(Form.numberStoreys)


async def process_number(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await state.update_data(number=message.contact.phone_number)
    await message.answer("Как вас зовут", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.name)
    print(user_data)


async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    user_data = await state.get_data()
    print(message)
    await message.answer(f"Отлично, {user_data["name"]}!\nВ ближайшее время мы свяжемся с Вами", reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
    print(user_data)






def register_fsm(dp : Dispatcher):
    dp.message.register(form_start, Command('calculate'))
    dp.callback_query.register(process_numberStoreys, Form.numberStoreys)
    dp.callback_query.register(process_square, Form.square)
    dp.callback_query.register(process_mansard, Form.mansard)
    dp.callback_query.register(process_WallMaterial, Form.WallMaterial)
    dp.callback_query.register(process_RoofMaterial, Form.RoofMaterial)
    dp.callback_query.register(process_FoundationMaterial, Form.FoundationMaterial)
    dp.callback_query.register(process_FacadeMaterial, Form.FacadeMaterial)
    dp.message.register(process_number, Form.number)
    dp.message.register(process_name, Form.name)
    dp.callback_query.register(process_confirm, Form.confirm)