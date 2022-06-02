from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

from food.FoodClass import Food
from food.DrinkClass import Drink

taco_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🐤Taco tovuqli"),KeyboardButton("🐮Taco mol go`shtli"),
    KeyboardButton("◀Orqaga")
)

taco_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🐤Тако с курицей"),KeyboardButton("🐮Тако из говядины"),
    KeyboardButton("◀Назад")
# KeyboardButton("ℹOvqat haqida"),
)

brusketta_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("🐟Brusketta baliqli"),KeyboardButton("🥗Brusketta guakamola"),
    KeyboardButton("◀Orqaga")
# KeyboardButton("ℹOvqat haqida"),
)

brusketta_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("🐟Брускетта с рыбным мясом"),KeyboardButton("🥗Брускетта с гукамолой"),
    KeyboardButton("◀Назад")
# KeyboardButton("ℹOvqat haqida"),
)

burgers_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🍔Burger bunato"),KeyboardButton("🐤Burger chicken"),
    KeyboardButton("◀Orqaga"),
# KeyboardButton("ℹOvqat haqida"),
)

burgers_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🍔Бургер бунато"),KeyboardButton("🐤Бургер с курицей"),
    KeyboardButton("◀Назад"),
# KeyboardButton("ℹOvqat haqida")
)

sandwich_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("🦃Sandwich kurka go`shtli"), KeyboardButton("🐟Sandwich baliqli"),
    KeyboardButton("🐤Sandwich tovuqli"), KeyboardButton("◀Orqaga"),
    # KeyboardButton("ℹOvqat haqida"),
)

sandwich_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    KeyboardButton("🦃Сендвич с мясом индейки"), KeyboardButton("🐟Сендвич рыбный"),
    KeyboardButton("🐤Сендвич с курицей"), KeyboardButton("◀Назад"),
    # KeyboardButton("ℹOvqat haqida"),
)

salads_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🇬🇷Gretsiyacha salat"), KeyboardButton("🥑Salat avakado"),
    KeyboardButton("🤴Sezar salat"), KeyboardButton("🐟Salat baliqli"),
    KeyboardButton("🐤Salat tovuqli"), KeyboardButton("◀Orqaga"),
    # KeyboardButton("ℹOvqat haqida")
)

salads_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("🇬🇷Греческий салат"), KeyboardButton("🥑Салат из авокадо"),
    KeyboardButton("🤴Салат Цезарь"), KeyboardButton("🐟Салат с рыбой"),
    KeyboardButton("🐤Салат с курицей"), KeyboardButton("◀Назад"),
    # KeyboardButton("ℹOvqat haqida")
)

coffee_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("◀Orqaga")
)
coffee_uz.add(
    KeyboardButton("Amerikano qahva"), KeyboardButton("Qora choy"),
    KeyboardButton("Kapuchino qahva"), KeyboardButton("Ko`k choy"),
    KeyboardButton("Latte qahva"), KeyboardButton("Mevali choy"),
    KeyboardButton("Espresso qahva"), KeyboardButton("Limonli choy"),
    KeyboardButton("Qaynoq shokoladli qahva"), KeyboardButton("Yalpizli choy"),
)

coffee_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("◀Назад")
)
coffee_ru.add(
    KeyboardButton("Кофе американо"), KeyboardButton("Черный чай"),
    KeyboardButton("Кофе капучино"), KeyboardButton("Зеленый чай"),
    KeyboardButton("Кофе латте"), KeyboardButton("Фруктовый чай"),
    KeyboardButton("Кофе эспрессо"), KeyboardButton("Чай с лимоном"),
    KeyboardButton("Горячий шоколад"), KeyboardButton("Чай с мятой"),
)

coctails_ru = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("◀Назад"), KeyboardButton("Молочный шейк"),
    KeyboardButton("Фруктовый"),KeyboardButton("Молочный шоколад"),
    KeyboardButton("Латте со льдом"), KeyboardButton("Американо со льдом"),
    KeyboardButton("Чай со льдом"), KeyboardButton("Чай со льдом 1Л"),
    KeyboardButton("Махито"),KeyboardButton("Maxito 1Л"),
)

coctails_uz = ReplyKeyboardMarkup(resize_keyboard=True,row_width=2).add(
    KeyboardButton("◀Orqaga"), KeyboardButton("Milk sheyk"),
    KeyboardButton("Mevali"),KeyboardButton("Sutli shokolad"), 
    KeyboardButton("Ice latte"), KeyboardButton("Ice amerikano"),
    KeyboardButton("Ice tea"), KeyboardButton("Ice tea 1L"),
    KeyboardButton("Maxito"),KeyboardButton("Maxito 1L"),
)

fries_uz = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add("🍟Fries","◀Orqaga")
fries_ru = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1).add("🍟Картофель фри","◀Назад")

foods_data = {
    'UZ': {
        # "Taco": {
            "🐤Taco tovuqli": Food("Taco tovuqli", 27000, "Taco", "photo hashcode"),
            "🐮Taco mol go`shtli": Food("Taco mol go`shtli",30000,"Taco","photo hashcode"),
        # },
        # "Brusketta": {
            "🐟Brusketta baliqli": Food("Brusketta baliqli",30000,"Brusketti", "photo hashcode"),
            "🥗Brusketta guakamola": Food("Brusketta guakamola",21000,"Brusketti","photo hashcode"),
        # },
        # "Burger": {
            "🐤Burger chicken": Food("Burger chicken",24000,"Burger","photo hashcode"),
            "🍔Burger bunato": Food("Burger bunato",30000,"Burger", "photo hashcode"),
        # },
        # "Fries": {
            "🍟Fries": Food("Fries", 10000, "Fries", "photo hashcode"),
        # },
        # "Coffee": {
            "Amerikano qahva": Drink("Amerikano qahva", 15000, "Coffee"),
            "Kapuchino qahva": Drink("Kapuchino qahva", 15000, "Coffee"),
            "Latte qahva": Drink("Latte qahva", 15000, "Coffee"),
            "Espresso qahva": Drink("Espresso qahva", 15000, "Coffee"),
            "Qaynoq shokoladli qahva": Drink("Qaynoq shokoladli qahva", 16000, "Coffee"),
            "Qora choy": Drink("Qora choy", 10000, "Tea"),
            "Ko`k choy": Drink("Ko`k choy", 10000, "Tea"),
            "Mevali choy": Drink("Mevali choy", 20000, "Tea"),
            "Limonli choy": Drink("Limonli choy", 15000, "Tea"),
            "Yalpizli choy": Drink("Yalpizli choy", 10000, "Tea"),
        # },
        # "Sandwich": {
            "🦃Sandwich kurka go`shtli": Food("Sandwich kurka go`shtli", 18000, "Sandwich", "photo hashcode"),
            "🐤Sandwich tovuqli": Food("Sandwich tovuqli", 22000, "Sandwich", "photo hashcode"),
            "🐟Sandwich baliqli": Food("Sandwich baliqli", 22000, "Sandwich", "photo hashcode"),
        # },
        # "Salad": {
            "🐤Salat tovuqli": Food("Salat tovuqli", 25000, "Salad", "photo hashcode"),
            "🐟Salat baliqli": Food("Salat baliqli", 30000, "Salad", "photo hash code"),
            "🤴Sezar salat": Food("Sezar salat", 22000, "Salad", "photo hashcode"),
            "🥑Salat avakado": Food("Salat avakado", 25000, "Salad", "photo hashcode"),
            "🇬🇷Gretsiyacha salat": Food("Gretsiyacha salat", 22000, "Salad", "photo hashcode"),
        # },
        # "Coctail": {
            "Milk sheyk": Drink("Milk sheyk", 20000, "Coctail"),
            "Mevali": Drink("Mevali", 22000, "Coctail"),
            "Sutli shokolad": Drink("Sutli shokolad", 20000, "Coctail"),
            "Ice latte": Drink("Ice latte", 20000, "Coctail"),
            "Ice amerikano": Drink("Ice amerikano", 20000, "Coctail"),
            "Ice tea": Drink("Ice tea", 20000, "Coctail"),
            "Ice tea 1L": Drink("Ice tea 1L", 35000, "Coctail", 1),
            "Maxito": Drink("Maxito", 20000, "Coctail"),
            "Maxito 1L": Drink("Maxito 1L", 35000, "Coctail", 1),
        # },
    },
    'RU': {
        # "Taco": {
            "🐤Тако с курицей": Food("Тако с курицей", 27000, "Taco", "photo hashcode"),
            "🐮Тако из говядины": Food("Тако из говядины",30000,"Taco","photo hashcode"),
        # },
        # "Brusketta": {
            "🐟Брускетта с рыбным мясом": Food("Брускетта с рыбным мясом",30000,"Brusketti", "photo hashcode"),
            "🥗Брускетта с гукамолой": Food("Брускетта с гукамолой",21000,"Brusketti","photo hashcode"),
        # },
        # "Burger": {
            "🐤Бургер с курицей": Food("Бургер с курицей",24000,"Burger","photo hashcode"),
            "🍔Бургер бунато": Food("Бургер бунато",30000,"Burger", "photo hashcode"),
        # },
        # "Fries": {
            "🍟Картофель фри": Food("Картофель фри", 10000, "Fries", "photo hashcode"),
        # },
        # "Coffee": {
            "Кофе американо": Drink("Кофе американо", 15000, "Coffee"),
            "Кофе капучино": Drink("Кофе капучино", 15000, "Coffee"),
            "Кофе латте": Drink("Кофе латте", 15000, "Coffee"),
            "Кофе эспрессо": Drink("Кофе эспрессо", 15000, "Coffee"),
            "Горячий шоколад": Drink("Горячий шоколад", 16000, "Coffee"),
            "Черный чай": Drink("Черный чай", 10000, "Tea"),
            "Зеленый чай": Drink("Зеленый чай", 10000, "Tea"),
            "Фруктовый чай": Drink("Фруктовый чай", 20000, "Tea"),
            "Чай с лимоном": Drink("Чай с лимоном", 15000, "Tea"),
            "Чай с мятой": Drink("Чай с мятой", 10000, "Tea"),
        # },
        # "Sandwich": {
            "🦃Сендвич с мясом индейки": Food("Сендвич с мясом индейки", 18000, "Sandwich", "photo hashcode"),
            "🐤Сендвич с курицей": Food("Сендвич с курицей", 22000, "Sandwich", "photo hashcode"),
            "🐟Сендвич рыбный": Food("Сендвич рыбный", 22000, "Sandwich", "photo hashcode"),
        # },
        # "Salad": {
            "🐤Салат с курицей": Food("Салат с курицей", 25000, "Salad", "photo hashcode"),
            "🐟Салат с рыбой": Food("Салат с рыбой", 30000, "Salad", "photo hash code"),
            "🤴Салат Цезарь": Food("Салат Цезарь", 22000, "Salad", "photo hashcode"),
            "🥑Салат из авокадо": Food("Салат из авокадо", 25000, "Salad", "photo hashcode"),
            "🇬🇷Греческий салат": Food("Греческий салат", 22000, "Salad", "photo hashcode"),
        # },
        # "Coctail": {
            "Молочный шейк": Drink("Молочный шейк", 20000, "Coctail"),
            "Фруктовый": Drink("Фруктовый", 22000, "Coctail"),
            "Молочный шоколад": Drink("Молочный шоколад", 20000, "Coctail"),
            "Латте со льдом": Drink("Латте со льдом", 20000, "Coctail"),
            "Американо со льдом": Drink("Американо со льдом", 20000, "Coctail"),
            "Чай со льдом": Drink("Чай со льдом", 20000, "Coctail"),
            "Чай со льдом 1Л": Drink("Чай со льдом 1Л", 35000, "Coctail", 1),
            "Махито": Drink("Махито", 20000, "Coctail"),
            "Maxito 1Л": Drink("Maxito 1Л", 35000, "Coctail", 1),
        # },
    }
}

foods_keys = {
    'UZ': {
        "🌮Taco": taco_uz,
        "🥘Brusketta": brusketta_uz,
        "🍔Burger": burgers_uz,
        "🍟Fries": fries_uz,
        "🥪Sandwich": sandwich_uz,
        "🥗Salad": salads_uz,
        "☕Coffee": coffee_uz,
        "🍹Coctail": coctails_uz
    },
    'RU': {
        "🌮Тако": taco_ru,
        "🥘Брускетта": brusketta_ru,
        "🍔Бургер": burgers_ru,
        "🍟Кортошка фри": fries_ru,
        "🥪Сендвич": sandwich_ru,
        "🥗Салат": salads_ru,
        "☕Кофи": coffee_ru,
        "🍹Коктейл": coctails_ru
    }
}