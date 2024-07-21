import math

def sumMansard(data):
    if (data["mansard"]):
        priceOneWindow = 130
        countWindow = (int(data["square"])//10)//2
        # print(countWindow*priceOneWindow)
        return countWindow*priceOneWindow
    else:
        return 0
    

def sumWallMaterial(data, listWallMaterial):
    priceWall = listWallMaterial[data["WallMaterial"]]
    squareWall = math.sqrt(float(data["square"]))*4*float(data["numberStoreys"])*2.7
    # print(priceWall*squareWall)
    return priceWall*squareWall


def sumRoofMaterial(data, listRoofMaterial):
    priceRoof = listRoofMaterial[data["RoofMaterial"]]
    # print(priceRoof*int(data["square"]))
    return priceRoof*int(data["square"])

def sumFoundationMaterial(data, listFoundationMaterial):
    priceFoundation = listFoundationMaterial[data["FoundationMaterial"]]/2.6
    # print(priceFoundation*float(data["square"]))
    return priceFoundation*float(data["square"])


def sumFacadeMaterial(data,listFacadeMaterial):
    priceFacade = listFacadeMaterial[data["FacadeMaterial"]]
    squareFacade = math.sqrt(float(data["square"]))*4*float(data["numberStoreys"])*2.7
    # print(priceFacade*squareFacade)
    return priceFacade*squareFacade

def allSum(data):
    return round(float(sumMansard(data)) + float(sumWallMaterial(data, listWallMaterial)) + float(sumRoofMaterial(data, listRoofMaterial)) + float(sumFoundationMaterial(data, listFoundationMaterial)) + float(sumFacadeMaterial(data, listFacadeMaterial)),2)


listWallMaterial = {"Кладка газосиликатных блоков": 30,
                    "Кладка керамзитобетонных блоков": 36,
                    "Кладка кирпичных стен": 38,
                    "Кладка бессер блоков": 36,
                    "Пока не определился": 35}

listRoofMaterial = {"Кровля из металлочерепицы": 24,
                    "Кровля из гибкой битумной черепицы": 32,
                    "Кровля из композитной черепицы": 30,
                    "Кровля из пронастила": 24,
                    "Шиферная кровля": 24,
                    "Пока не определился": 27}

listFoundationMaterial = {"Заливка ленточного фундамента": 23,
                        "Заливка свайно-ростверкового": 23,
                        "Заливка плитного фундамента": 23,
                        "Пока не определился": 23}

listFacadeMaterial = {"Облицовка клинкерным кирпичом":40,
                    "Облицовка естественным камнем":44,
                    "Облицовка декоративным камнем":36,
                    "Отделка сайдингом":16,
                    "Обшивка вагонкой":17,
                    "Обшивка блок хаусом":17,
                    "Пока не определился":28}