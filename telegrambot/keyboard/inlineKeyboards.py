from aiogram import types


answers = {
    "numberStoreys":{
        "1": "1",
        "2": "2",
        "3": "3"
    },
    "square" : {
        "до 50м2": "50",
        "50-100м2": "75",
        "100-150м2": "125",
        "200-250м2": "225",
        "250-300м2": "275",
        "300-350м2": "325"
    },
    "mansard": {
        "Да": "Да",
        "Нет": "Нет"
    },
    "WallMaterial": {
        "Кладка газосиликатных блоков":"Кладка газосиликатных блоков",
        "Кладка керамзитобетонных блоков":"Кладка керамзитобетонных блоков",
        "Кладка кирпичных стен":"Кладка кирпичных стен",
        "Кладка бессер блоков":"Кладка бессер блоков"
    },
    "RoofMaterial":{
        "Кровля из металлочерепицы":"Кровля из металлочерепицы",
        "Кровля из гибкой битумной черепицы":"Кровля из гибкой битумной черепицы",
        "Кровля из композитной черепицы":"Кровля из композитной черепицы",
        "Кровля из пронастила":"Кровля из пронастила",
        "Шиферная кровля":"Шиферная кровля",
    },
    "FoundationMaterial":{
        "Заливка ленточного фундамента":"Заливка ленточного фундамента",
        "Заливка свайно-ростверкового фундамента":"Заливка свайно-ростверкового",
        "Заливка плитного фундамента":"Заливка плитного фундамента",
    },
    "FacadeMaterial":{
        "Облицовка клинкерным кирпичом":"Облицовка клинкерным кирпичом",
        "Облицовка естественным камнем":"Облицовка естественным камнем",
        "Облицовка декоративным камнем":"Облицовка декоративным камнем",
        "Отделка сайдингом":"Отделка сайдингом",
        "Обшивка вагонкой":"Обшивка вагонкой",
        "Обшивка блок хаусом":"Обшивка блок хаусом",
    }
}


def createKeyboard(question_key, listData, vertically=False):
    buttons = []
    if vertically:
        verticallyButtons = []
        for key, value in answers[question_key].items():
            if value == listData[question_key]:
                verticallyButtons.append(types.InlineKeyboardButton(text=f"✅{key}", callback_data=value))
            else:
                verticallyButtons.append(types.InlineKeyboardButton(text=f"{key}", callback_data=value))
        buttons.append(verticallyButtons)
    else:
        for key, value in answers[question_key].items():
            if value == listData[question_key]:
                buttons.append([types.InlineKeyboardButton(text=f"✅{key}", callback_data=value)])
            else:
                buttons.append([types.InlineKeyboardButton(text=key, callback_data=value)])
    print(question_key)
    if question_key!="square" and question_key!="numberStoreys":
        print("tesssst")
        if listData[question_key] == "Пока не определился":
            buttons.append([types.InlineKeyboardButton(text=f"✅Пока не определился", callback_data=f"Пока не определился")])
        else:
            buttons.append([types.InlineKeyboardButton(text=f"Пока не определился", callback_data=f"Пока не определился")])
    print(listData[question_key])
    if listData[question_key] != None and question_key != "numberStoreys" :
        buttons.append([ types.InlineKeyboardButton(text=f"<Назад", callback_data=f"Назад"), types.InlineKeyboardButton(text=f"Далее>", callback_data=f"Далее")])
    elif listData[question_key] != None and question_key == "numberStoreys":
        buttons.append([types.InlineKeyboardButton(text=f"Далее>", callback_data=f"Далее")]) 
    elif question_key != "numberStoreys":
        buttons.append([types.InlineKeyboardButton(text=f"<Назад", callback_data=f"Назад")]) 
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)




buttonsInline = [
    [types.InlineKeyboardButton(text="Да", callback_data="Да"),types.InlineKeyboardButton(text="Нет", callback_data="Нет")],
]

YesOrNo = types.InlineKeyboardMarkup(inline_keyboard=buttonsInline)