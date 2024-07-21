from aiogram import Bot, Dispatcher, types


kbWall = [
            [types.KeyboardButton(text="Кладка газосиликатных блоков"),],
            [types.KeyboardButton(text="Кладка керамзитобетонных блоков"),],
            [types.KeyboardButton(text="Кладка кирпичных стен"),],
            [types.KeyboardButton(text="Кладка бессер блоков"),],
            [types.KeyboardButton(text="Пока не определился"),],
            [types.KeyboardButton(text="Вернуться назад"),],
    ]
keyboardWall = types.ReplyKeyboardMarkup(
    keyboard=kbWall,
    resize_keyboard=True
)

kbRoof = [
            [types.KeyboardButton(text="Кровля из металлочерепицы"),],
            [types.KeyboardButton(text="Кровля из гибкой битумной черепицы"),],
            [types.KeyboardButton(text="Кровля из композитной черепицы"),],
            [types.KeyboardButton(text="Кровля из пронастила"),],
            [types.KeyboardButton(text="Шиферная кровля"),],
            [types.KeyboardButton(text="Пока не определился"),],
            [types.KeyboardButton(text="Вернуться назад"),],
    ]
keyboardRoof = types.ReplyKeyboardMarkup(
    keyboard=kbRoof,
    resize_keyboard=True
)


kbFoundation = [
            [types.KeyboardButton(text="Заливка ленточного фундамента"),],
            [types.KeyboardButton(text="Заливка свайно-ростверкового фундамента"),],
            [types.KeyboardButton(text="Заливка плитного фундамента"),],
            [types.KeyboardButton(text="Пока не определился"),],
            [types.KeyboardButton(text="Вернуться назад"),],
    ]
keyboardFoundation = types.ReplyKeyboardMarkup(
    keyboard=kbFoundation,
    resize_keyboard=True
)


kbFacade = [
            [types.KeyboardButton(text="Облицовка клинкерным кирпичом"),],
            [types.KeyboardButton(text="Облицовка естественным камнем"),],
            [types.KeyboardButton(text="Облицовка декоративным камнем"),],
            [types.KeyboardButton(text="Отделка сайдингом"),],
            [types.KeyboardButton(text="Обшивка вагонкой"),],
            [types.KeyboardButton(text="Обшивка блок хаусом"),],
            [types.KeyboardButton(text="Пока не определился"),],
            [types.KeyboardButton(text="Вернуться назад"),],
    ]
keyboardFacade = types.ReplyKeyboardMarkup(
    keyboard=kbFacade,
    resize_keyboard=True
)



kbYesNo = [
            [types.KeyboardButton(text="Да"),
             types.KeyboardButton(text="Нет"),
             ],
            [types.KeyboardButton(text="Пока не определился"),],
            [types.KeyboardButton(text="Вернуться назад"),],
    ]
keyboardYesNo = types.ReplyKeyboardMarkup(
    keyboard=kbYesNo,
    resize_keyboard=True
)

kbBack = [
            [types.KeyboardButton(text="Вернуться назад")],
    ]
keyboardBack = types.ReplyKeyboardMarkup(
    keyboard=kbBack,
    resize_keyboard=True
)


kbAgain = [
            [types.KeyboardButton(text="Да"),
             types.KeyboardButton(text="Нет"),
             ],
    ]
keyboardAgain = types.ReplyKeyboardMarkup(
    keyboard=kbAgain,
    resize_keyboard=True
)


kbSendContact = [
            [types.KeyboardButton(text="Отправить контакт", request_contact=True)
             ]
    ]
keyboardSendContact = types.ReplyKeyboardMarkup(
    keyboard=kbSendContact,
    resize_keyboard=True
)

