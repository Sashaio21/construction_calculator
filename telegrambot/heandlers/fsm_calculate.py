from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from keyboard.keyboards import  keyboardWall, keyboardBack,keyboardSendContact,keyboardAgain,keyboardFacade, keyboardYesNo,keyboardFoundation, keyboardRoof  
from utils.calculate import allSum
from utils.excelCreation import createExcelFile


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
    await message.answer("Давайте начнем!\nКак вас зовут?", reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(Form.name)


# Обработчик для состояния Form.name
async def process_name(message: Message, state: FSMContext):
    print(message.text)
    await state.update_data(name=message.text)
    await message.answer("Укажите этажность вашего будущего дома", reply_markup=keyboardBack)
    await state.set_state(Form.numberStoreys)


# Обработчик для состояния Form.numberStoreys
async def process_numberStoreys(message: Message, state: FSMContext):
    if message.text == "Вернуться назад":
        await message.answer("Как Вас зовут?", reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.name)
    else: 
        await state.update_data(numberStoreys=message.text)
        user_data = await state.get_data()
        print(user_data)
        await message.answer("Укажите примерную площадь дома", reply_markup=keyboardBack)
        await state.set_state(Form.square)


# Обработчик для состояния Form.numberStoreys
async def process_square(message: Message, state: FSMContext):
    await state.update_data(square=message.text)
    user_data = await state.get_data()
    print(user_data)
    await message.answer("Будет ли мансардный этаж", reply_markup=keyboardYesNo)
    await state.set_state(Form.mansard)


# Обработчик для состояния Form.numberStoreys
async def process_mansard(message: Message, state: FSMContext):
    await state.update_data(mansard=message.text)
    user_data = await state.get_data()
    print(user_data)
    await message.answer("Выберите тип кладки стен ", reply_markup=keyboardWall)
    await state.set_state(Form.WallMaterial)


# Обработчик для состояния Form.numberStoreys
async def process_WallMaterial(message: Message, state: FSMContext):
    await state.update_data(WallMaterial=message.text)
    user_data = await state.get_data()
    print(user_data)
    await message.answer(f"Выберите тип кровли  ", reply_markup=keyboardRoof)
    await state.set_state(Form.RoofMaterial)


# Обработчик для состояния Form.numberStoreys
async def process_RoofMaterial(message: Message, state: FSMContext):
    await state.update_data(RoofMaterial=message.text)
    user_data = await state.get_data()
    print(user_data)
    await message.answer(f"Выберите тип фундамента ", reply_markup=keyboardFoundation)
    await state.set_state(Form.FoundationMaterial)


# Обработчик для состояния Form.numberStoreys
async def process_FoundationMaterial(message: Message, state: FSMContext):
    await state.update_data(FoundationMaterial=message.text)
    user_data = await state.get_data()
    print(user_data)
    await message.answer(f"Выберите тип фасада  ", reply_markup=keyboardFacade)
    await state.set_state(Form.FacadeMaterial)


# Обработчик для состояния Form.numberStoreys
async def process_FacadeMaterial(message: Message, state: FSMContext):
    await state.update_data(FacadeMaterial=message.text)
    user_data = await state.get_data()
    print(user_data)
    await message.answer(f"Отправтье нам Ваш номер телефона, и мы в скорем времени свяжемся с вами", reply_markup=keyboardSendContact)
    await state.set_state(Form.number)


# Обработчик для состояния Form.numberStoreys
async def process_number(message: Message, state: FSMContext):
    print(message.contact.phone_number)
    await state.update_data(number=message.contact.phone_number)
    user_data = await state.get_data()
    print(user_data)
    await message.answer(f'Имя: {user_data["name"]} \nКоличество этажей: {user_data["numberStoreys"]} \nПлощадь: {user_data["square"]} \nМансардный этаж: {user_data["mansard"]} \nМатериал стен: {user_data["WallMaterial"]} \nТип кровли: {user_data["RoofMaterial"]} \nТип фундамента: {user_data["FoundationMaterial"]} \nФасад: {user_data["FacadeMaterial"]} \nНомер телефона: {user_data["number"]} \nВсё верно? (да/нет)', 
        reply_markup=keyboardAgain)
    await state.set_state(Form.confirm)


# Обработчик для состояния Form.confirm
async def process_confirm(message: Message, state: FSMContext):
    if message.text.lower() == 'да':
        user_data = await state.get_data()
        print(message)
        await message.answer(f"Результат расчета\n{allSum(user_data)} у.е.",  parse_mode='HTML', reply_markup=types.ReplyKeyboardRemove())

        file_stream = createExcelFile(user_data)
        document = types.input_file.FSInputFile("building_info.xlsx")
        # await bot.send_document(chat_id=481620692, document=document)
        await state.clear()
    else:
        await message.answer("Давайте попробуем еще раз. Как вас зовут?")
        await state.set_state(Form.name)
        

def register_fsm_callback(dp:Dispatcher):
    dp.message.register(form_start, Command('calculate'))
    dp.message.register(process_name, Form.name)
    dp.message.register(process_numberStoreys, Form.numberStoreys)
    dp.message.register(process_square, Form.square)
    dp.message.register(process_mansard, Form.mansard)
    dp.message.register(process_WallMaterial, Form.WallMaterial)
    dp.message.register(process_RoofMaterial, Form.RoofMaterial)
    dp.message.register(process_FoundationMaterial, Form.FoundationMaterial)
    dp.message.register(process_FacadeMaterial, Form.FacadeMaterial)
    dp.message.register(process_number, Form.number)
    dp.message.register(process_confirm, Form.confirm)