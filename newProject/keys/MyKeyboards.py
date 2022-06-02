from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove,KeyboardButton

remove = ReplyKeyboardRemove()

menu_buttons_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("📥Savat"), KeyboardButton("◀Orqaga"),
    KeyboardButton("🌮Taco"),KeyboardButton("🥘Brusketta"),
    KeyboardButton("🥪Sandwich"), KeyboardButton("🍔Burger"),
    KeyboardButton("🍟Fries"), KeyboardButton("🥗Salad"),
    KeyboardButton("☕Coffee"), KeyboardButton("🍹Coctail"),
)

menu_buttons_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("📥Корзина"), KeyboardButton("◀Назад"),
    KeyboardButton("🌮Тако"),KeyboardButton("🥘Брускетта"),
    KeyboardButton("🥪Сендвич"), KeyboardButton("🍔Бургер"),
    KeyboardButton("🍟Кортошка фри"), KeyboardButton("🥗Салат"),
    KeyboardButton("☕Кофи"), KeyboardButton("🍹Коктейл"),
)

language = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("uz🇺🇿"),KeyboardButton("ru🇷🇺")
)

settings_keys_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("Ismni o'zgartirish"), KeyboardButton("Telefon raqamni o'zgartirish"),
    KeyboardButton("Tilni o'zgartirish"), KeyboardButton("Orqaga")
)

settings_keys_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("Смена имени"), KeyboardButton("Смена номера телефона"),
    KeyboardButton("Изменение языка"), KeyboardButton("Назад")
)

mainMenu_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2,one_time_keyboard=True).add(
    KeyboardButton("🛍Buyurtma berish"),KeyboardButton("⚙Sozlamalar"),
    KeyboardButton("ℹBiz haqimizda"),KeyboardButton("🎉Aksiyalar"),
)

mainMenu_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🛍Заказать"),KeyboardButton("⚙Настройки"),
    KeyboardButton("ℹО нас"),KeyboardButton("🎉Акции"),
)

phone_number_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(
    KeyboardButton("Telefon raqamni jo'natish 📲",request_contact=True)
)

phone_number_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=1).add(
    KeyboardButton("Отправка номера телефона 📲",request_contact=True)
)

numbers_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton("1"),KeyboardButton("2"),KeyboardButton("3"),
    KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6"),
    KeyboardButton("7"), KeyboardButton("8"), KeyboardButton("9"),
    KeyboardButton("◀Orqaga")
)


numbers_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    KeyboardButton("1"),KeyboardButton("2"),KeyboardButton("3"),
    KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6"),
    KeyboardButton("7"), KeyboardButton("8"), KeyboardButton("9"),
    KeyboardButton("◀Назад")
)

desc_uz = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("🤷‍♂Qo\'shimcha ma\'lomtlar yo\'q"),KeyboardButton("◀Orqaga")
)

desc_ru = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("🤷‍♂Нет дополнительной информации"),KeyboardButton("◀Назад")
)

deliver_service_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("🚙Yetkazib berish"), KeyboardButton("🏃‍♂Olib ketish"),
    KeyboardButton("◀Orqaga")
)

deliver_service_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("🚙Доставка"), KeyboardButton("🏃‍♂Самовывоз"),
    KeyboardButton("◀Назад")
)

payment_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("💴Naqd pul"), KeyboardButton("💳Payme/Click"),
    KeyboardButton("◀Orqaga")
)

payment_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("💴Наличные"), KeyboardButton("💳Пейми/Клик"),
    KeyboardButton("◀Назад")
)

location_uz = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(
    KeyboardButton("📍Manzilni jo'natish", request_location=True)
)

location_ru = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True).add(
    KeyboardButton("📍Отправка адреса", request_location=True)
)


payme_and_click_uz = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Pay me", callback_data="payme"),
    InlineKeyboardButton("Click", callback_data="Click")

)

payme_and_click_ru = InlineKeyboardMarkup(row_width=2).add(
    InlineKeyboardButton("Пейми", callback_data="пейми"),
    InlineKeyboardButton("Клик", callback_data="клик")

)
#
# payme_ru = InlineKeyboardMarkup(row_width=1).add(
#     InlineKeyboardButton("Pay Me", callback_data="payme")
# )
#
# click_uz = InlineKeyboardMarkup(row_width=1).add(
# )
#
# click_ru = InlineKeyboardMarkup(row_width=1).add(
#     InlineKeyboardButton("Click", callback_data="Click")
# )

all_keys = {
    "ToAll": {
        "language": language,
    },
    "UZ":{
        # "Click": click_uz,
        # "Pay me": payme_uz,
        "Numbers": numbers_uz,
        "Description": desc_uz,
        "Payments": payment_uz,
        "Location": location_uz,
        "Main menu": mainMenu_uz,
        "Send PN": phone_number_uz,
        "Service": deliver_service_uz,
        "Into booking": menu_buttons_uz,
        "Which change": settings_keys_uz,
        "Payme/Click": payme_and_click_ru,
    },
    "RU": {
        # "Click": click_ru,
        # "Pay me": payme_ru,
        "Numbers": numbers_ru,
        "Description": desc_ru,
        "Payments": payment_ru,
        "Location": location_ru,
        "Main menu": mainMenu_ru,
        "Send PN": phone_number_ru,
        "Service": deliver_service_ru,
        "Into booking": menu_buttons_ru,
        "Which change": settings_keys_ru,
        "Payme/Click": payme_and_click_ru,
    }
}

async def create_buttons(user_language: str, foods: dict) -> ReplyKeyboardMarkup:
    """
    Agar user qaysidir ovqatni ayirmoqchi yoki umuman savatni tozalamoqchi bo'lsa shu metod ishlaydi

    :param foods: Dictionary -> Userning buyutmalari
    :return: buttons: InlineKeyboardMarkup -> Ayirish, qo'shish va boshqa InlineKeyboardButton larni o'zida jamlaydi
    """
    buttons = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    if user_language == 'UZ':
        buttons.add(
            KeyboardButton("🔄Savatni tozalash"), KeyboardButton("✅Buyurtmani tasdiqlash"),
            KeyboardButton("◀Orqaga")
        )
    else:
        buttons.add(
            KeyboardButton("🔄Очистка корзины"), KeyboardButton("✅Подтверждение заказа"),
            KeyboardButton("◀Назад")
        )

    if foods == None: return None
    for key, value in foods.items():
        buttons.add(
            KeyboardButton(f"❌{key}")
        )

    return buttons






