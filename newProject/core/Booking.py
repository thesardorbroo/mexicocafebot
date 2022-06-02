from aiogram.types import Message,CallbackQuery
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from newProject.config.Config import bot,db,burger_photo,menu_photo
from newProject.user.User import UserOB
from newProject.texts.Text import botext, return_orders, final_check
from newProject.keys.FoodsData import foods_keys, foods_data
from newProject.keys.MyKeyboards import all_keys, remove, create_buttons
from newProject.core import Core

async def booking_foods(message: Message):
    user = await db.get_user(message.from_user.id)
    text = message.text

    if text == "📥Savat" or text == "📥Корзина":
        """
        Savat buttoni uchun
        """
        orders = await db.get_user_orders(user)
        buttons = await create_buttons(user.language, orders)
        if orders == None or buttons == None: await bot.send_message(user.user_id, botext[user.language]["Basket is empty"])
        else:
            check_paper = await return_orders(user, orders)
            check_paper = check_paper[0]
            await bot.send_message(user.user_id, f"""{botext[user.language]["Your order"]}\n===================\n{check_paper}\n""",reply_markup=buttons)
            await db.update_column(user.user_id,"step",10)


    elif text == "◀Orqaga" or text == "◀Назад":
        """
        Orqaga buttoni uchun
        """
        await db.update_column(user.user_id, "step", 3)
        await bot.send_message(user.user_id, botext[user.language]["Main menu"],reply_markup=all_keys[user.language]["Main menu"])

    else:
        """
        Qolgan boshqa hamma buttonlar uchun
        """
        await bot.send_message(user.user_id,botext[user.language]["Select one"], reply_markup=foods_keys[user.language][text])
        await db.update_column(user.user_id,"step", 8)


async def selected_one(message: Message, user: UserOB):
    text = message.text
    if user.step == 8:
        """
        Asosiy menyudagi ovqatlarni tanlaganida shuyerga kirishi kerak
        """
        if text == "◀Orqaga" or text == "◀Назад":
            await db.update_column(user.user_id, "step", 7)
            await bot.send_message(user.user_id, botext[user.language]["Main menu"], reply_markup=all_keys[user.language]["Into booking"])

        else:
            """
            Bu yerda ovqat bazaga yozilishi kereak
            """
            food = foods_data[user.language][message.text]
            if user.language == 'UZ': await bot.send_photo(user.user_id,burger_photo,caption=f"Ovqat nomi: {food.name}\nOvqat narxi: {food.cost}")
            else: await bot.send_photo(user.user_id,burger_photo,caption=f"Название блюда: {food.name}\nСтоимость еды: {food.cost}")
            await bot.send_message(user.user_id, botext[user.language]["How many"],reply_markup=all_keys[user.language]["Numbers"])
            await db.update_column(user.user_id,"last_food",f"{food.name}")
            await db.update_column(user.user_id, "step", 9)

    elif user.step == 9:
        """
        Ovqat tanlaganidan keyin nechta olishini ko'rsatish kerak
        """
        food = 0
        for key, value in foods_data[user.language].items():
            if value.name == user.last_food:
                food = value
                break

        # info = f"{food.name} * {int(text)}:\n{int(food.cost)} * {int(text)} = {int(food.cost * text)}\n"
        info = food.name + " * " + text + ":\n" + str(food.cost) + " * " + text + " = " + str(food.cost * int(text)) + "\n"
        await message.answer(info)
        await db.update_column(user.user_id, "step", 7)
        await db.add_user_order(user, food, text)
        await message.answer(botext[user.language]["Continue?"], reply_markup=all_keys[user.language]["Into booking"])

async def foods_accepted(message: Message, user: UserOB):
    """
    User bu yerda ovqatlarni ayirishi, savatini bo'shatishi va buyurtmani tasdiqlashi mumkun
    """
    text = message.text
    if text == "🔄Savatni tozalash" or text == "🔄Очистка корзины":
        """
        Agar user savatni bo'shatmoqchi bo'lsa shu metod ishlaydi
        """
        await db.delete_from_books(user.user_id)
        await db.update_column(user.user_id, "step", 7)
        await bot.send_message(user.user_id, botext[user.language]["Continue?"],reply_markup=all_keys[user.language]["Into booking"])

    elif text == "✅Buyurtmani tasdiqlash" or text == "✅Подтверждение заказа":
        """
        Agar user buyurtmani tasdiqlamoqchi bo'lsa shu metod ishlaydi
        """
        await bot.send_message(user.user_id, botext[user.language]["Description"], reply_markup=all_keys[user.language]["Description"])
        await db.update_column(user.user_id, "step", 11)

    elif text == "◀Orqaga" or text == "◀Назад":
        """
        Agar user orqaga qaytmoqchi bo'lsa shu metod ishlaydi
        """
        await db.update_column(user.user_id, "step", 7)
        await bot.send_message(user.user_id, botext[user.language]["Main menu"], reply_markup=all_keys[user.language]["Into booking"])

    else:
        """
        Agar user qandaydir ovqatni ayirmoqchi bo'lsa shu metod ishlaydi
        """
        text = text[1:]
        await db.delete_from_books(user.user_id,text)
        await db.update_column(user.user_id, "step", 7)
        await bot.send_message(user.user_id, botext[user.language]["Text is deleted"], reply_markup=all_keys[user.language]["Into booking"])

async def get_description(message: Message, user: UserOB):
    """
    Userning qo'shimcha ma'lumotlari shu yerga yoziladi
    """
    text = message.text
    if text == "🤷‍♂Qo'shimcha ma'lomtlar yo'q" or text == "🤷‍♂Нет дополнительной информации":
        await db.update_column(user.user_id, "step", 12)
        await bot.send_message(user.user_id, botext[user.language]["Service"], reply_markup=all_keys[user.language]["Service"], parse_mode='HTML')

    elif text == "◀Orqaga" or text == "◀Назад":
        await db.update_column(user.user_id, "step", 7)
        await bot.send_message(user.user_id, botext[user.language]["Main menu"], reply_markup=all_keys[user.language]["Into booking"])

    elif text != "✅Buyurtmani tasdiqlash" or text != "✅Подтверждение заказа":
        await db.update_column(user.user_id, "description", text)
        await db.update_column(user.user_id, "step", 12)
        await bot.send_message(user.user_id, botext[user.language]["Service"], reply_markup=all_keys[user.language]["Service"], parse_mode='HTML')

async def get_user_status(message: Message, user: UserOB):
    text = message.text
    if text == "🚙Yetkazib berish" or text == "🚙Доставка":
        await db.update_column(user.user_id, "step", 13)
        await db.update_column(user.user_id, "status", text)
        await bot.send_message(user.user_id, botext[user.language]["Location"], reply_markup=all_keys[user.language]["Location"])

    elif text == "◀Orqaga" or text == "◀Назад":
        await bot.send_message(user.user_id, botext[user.language]["Description"],reply_markup=all_keys[user.language]["Description"])
        await db.update_column(user.user_id, "step", 11)

    elif text == "🏃‍♂Olib ketish" or text == "🏃‍♂Самовывоз":
        await db.update_column(user.user_id, "step", 13)
        await db.update_column(user.user_id, "status", text)
        await bot.send_message(user.user_id, botext[user.language]["Payments"], reply_markup=all_keys[user.language]["Payments"])

async def get_user_pay(message: Message, user: UserOB):
    text = message.text
    if text == "💴Naqd pul" or text == "💴Наличные":
        orders = await db.get_user_orders(user)
        check_list = await final_check(user, orders)
        summa = check_list[1]
        check_list = check_list[0]
        await bot.send_message(user.user_id, check_list)
        await db.update_column(user.user_id, "step", 3)
        await bot.send_message(user.user_id, botext[user.language]["Thanks"], reply_markup=all_keys[user.language]["Main menu"])
        await bot.send_message(-1001682833459, check_list)
        if user.status == "🚙Yetkazib berish" or user.status == "🚙Доставка": await bot.send_location(-1001682833459, user.location[0], user.location[1])
        await db.add_to_sales(user.user_id, summa)

    elif text == "💳Payme/Click" or text == "💳Пейми/Клик":
        orders = await db.get_user_orders(user)
        check_list = await return_orders(user, orders)
        check_list = check_list[0]
        await bot.send_message(user.user_id, check_list, reply_markup=all_keys[user.language]["Payme/Click"])

    elif text == "◀Orqaga" or text == "◀Назад":
        await bot.send_message(user.user_id, botext[user.language]["Description"],reply_markup=all_keys[user.language]["Description"])
        await db.update_column(user.user_id, "step", 11)


