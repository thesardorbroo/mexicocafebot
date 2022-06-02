from newProject.user.User import UserOB
from newProject.food.FoodClass import Food
from newProject.food.DrinkClass import Drink
from newProject.keys.FoodsData import foods_data
from newProject.database.BotDB import SCDB
d2 = SCDB()

botext = {
    "ToAll": {
        "Choose language": "Iltimos tilni tanlang\n\nПожалуйста, выберите язык"
    },
    "UZ": {
        "Summary": "Ja'mi: ",
        "Choose": "Iltimos tanlang",
        "Main menu": "Asosiy menyu",
        "How many": "Nechta kerak?",
        "Basket is empty": "Savat bo'sh",
        "Continue?": "Davom etamizmi? 😉",
        "Thanks": "Xaridingiz uchun raxmat😊",
        "Payments": "To'lov turini tanlang",
        "Select one": "Nimadan boshlaymiz?",
        "Your order": "Sizning buyurtmangiz",
        "Select one again":"Iltimos tanlang",
        "Query Ok!": "Ma'lumot qabul qilindi",
        "How many foods": "Nechta ayirmoqchisiz?",
        "Enter name": "Iltimos ismingizni kiriting",
        "Text is deleted": "Buyurtmalar o'chirildi",
        "Location": "Iltimos manzilingizni yuboring",
        "Which change": "Nimani o'zgartirmoqchisiz?",
        "Expected error": "Ma'lumot noto'g'ri kiritildi!",
        "Send PN": "Iltimos telefon raqamingizni jo'nating 📲",
        "Description": "Agar qo'shimcha ma'lumotlaringiz bo'lsa yozib qoldirishingiz mumkun",
        "Service": "Sizga nima qulay? <b>🚙Yetkazib berish</b> yoki <b>🏃‍♂Olib ketish</b>\n\nEslatib o'tamiz yetkazib berish xizmati: 15000 so'm",
    },
   "RU": {
        "Summary": "Общее: ",
        "Choose": "Пожалуйста, выберите",
        "Main menu": "Главное меню",
        "How many": "Сколько нужно?",
        "Basket is empty": "Корзина пуста",
        "Thanks": "Спасибо за покупку😊",
        "Continue?": "Продолжаем? 😉",
        "Payments": "Выберите тип оплаты",
        "Select one": "С чего начнем?",
        "Your order": "Ваш заказ",
        "Select one again":"Пожалуйста, выберите(RU)",
        "Query Ok!": "Информация получена",
        "How many foods": "Сколько вы хотите вычесть?",
        "Enter name": "Пожалуйста, введите свое имя",
        "Text is deleted": "Заказы удалены",
        "Location": "Пожалуйста, отправьте свой адрес",
        "Which change": "Что вы хотите изменить?",
        "Expected error": "Информация была введена неправильно!",
        "Send PN": "Пожалуйста, отправьте свой номер телефона 📲",
        "Description": "Вы можете оставить запись, если у вас есть дополнительная информация",
        "Service": "Что вам удобно? <b>🚙Доставка</b> или <b>🏃 Самовывоз</b>\n\nНапомним, что услуга доставки: 15000 Сум",
   }
}

settings_text = {
    "UZ":{
        "Change language": "Tilni tanlang",
        "Change username": "Yangi username ni kiriting",
        "Change phone_number": "Yangi telefon raqamni kiriting",
    },
    "RU":{
        "Change language": "Выберите язык",
        "Change username": "Введите новое имя пользователя",
        "Change phone_number": "Введите новый номер телефона",
    }
}

dis_and_abus = {
    'UZ':{
        "Discounts": "Buyerda korxonaning aksyialar turadi",
        "About us": "Buyerda korxona haqidagi ma'lumotlar turadi",
    },
    'RU': {
        "Discounts": "Здесь акции предприятия стоят",
        "About us": "Вот где информация о предприятии стоит(RU)",
    }
}

async def data_of_user(user: UserOB):
    if user.language == 'UZ':
        all_data = f"""
Til: 🇺🇿
Foydalanuvchi ismi: {user.username}
Foydalanuvchi telefon raqami: {user.phone_number}
"""
        return all_data
    else:
        all_data = f"""
Язык: 🇷🇺
Имя пользователя: {user.username}
Номер телефона пользователя: {user.phone_number}
"""
        return all_data

async def return_caption_of_food(user: UserOB,food: Food):
    if user.language == 'UZ':
        caption = f"""
Ovqat nomi: {food.name}
Ovqat narxi: {food.cost}
"""
        return caption
    else:
        caption = f"""
Название блюда(RU): {food.name}
Стоимость еды(RU): {food.cost}
"""
        return caption

async def return_orders(user: UserOB, d: dict):
    """
    Bu metod userni savatga nimalar to'plaganini ko'rsatadi
    🇷🇺
    """
    check_paper = ""
    summa = 0;
    try:
        for key, value in d.items():
            food = await __ro_helper(user, key)
            check_paper += f"{key}:\n{food.cost} * {value} = {food.cost * value}\n\n"
            summa += int(food.cost * value)

        if user.status == "🚙Yetkazib berish" or user.status == "🚙Доставка":
            check_paper += f"\n{user.status[1:]}:\n{summa} + 15000 = {summa + int(15000)}\n"
            summa += int(15000)
            check_paper += f"""{botext[user.language]["Summary"]}{summa}"""

        else:
            check_paper += f"""{botext[user.language]["Summary"]}{summa}"""

        return [check_paper, summa]

    except AttributeError:
        return None


async def __ro_helper(user: UserOB, key: str):
    foods = foods_data[user.language]
    for k,v in foods.items():
        if v.name == key:
            return v

async def final_check(user: UserOB, orders: dict):
    check_list = await return_orders(user, orders)
    user_data = ""
    if user.language == 'UZ':
        user_data = f"""
Buyurtmachi ismi: {user.username}
Telefon raqam: {user.phone_number}
Tili: {'uz'}
=======================
Qo'shimcha ma'lumotlar: {user.description}
=======================
Buyurtma: \n{check_list[0]}

"""
    else :
        user_data = f"""
Имя заказчика: {user.username}
Номер телефона: {user.phone_number}
Язык: {'uz'}
=======================
Дополнительная информация: {user.description}
=======================
Заказ: \n{check_list[0]}

"""

    await d2.delete_from_base(user.user_id)
    return user_data,check_list[1]