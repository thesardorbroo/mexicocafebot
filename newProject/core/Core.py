from newProject.config.Config import db,bot,dp,menu_photo, PAYME_TOKEN,CLICK_TOKEN
from aiogram.types import Message,CallbackQuery, PreCheckoutQuery, ContentType
from newProject.keys.MyKeyboards import *
from newProject.texts.Text import *
from newProject.details import Details
from newProject.settings import MSettings
from newProject.core import Booking

async def pressed_start(message: Message):
    await db.delete_from_base(message.from_user.id)
    await db.update_all_column(message.from_user.id)

    if (await db.is_user_exist(message.from_user.id)):
        # Mavjud userga menyuni ko'rsatish
        print("User is exist!")
        await Details.userIsAvailable(message)
    else:
        # Yangi userni qo'shish kerak
        await bot.send_message(message.from_user.id, f"""
            Assalomu alaykum)\n\n{botext["ToAll"]["Choose language"]}
        """, reply_markup=all_keys["ToAll"]["language"])
        await db.insert_user(message.from_user.id)
        print("New user followed!")

    """
    Agar user /start kommandasini bossa books jadvaldan unga 
    tegishli bo'lgan hamma buyurtmalarni o'chirib tashlaydi
    """

async def sendPN(message: Message):
    user = await db.get_user(message.from_user.id)
    await Details.sendPhoneNumber(message,user)

async def user_is_booking(message: Message):
    user = await db.get_user(message.from_user.id)
    text = message.text
    if user.step < 3:
        await Details.addNewUser(message,user)

    elif user.step == 3:
        if text == "🛍Buyurtma berish" or text == "🛍Заказать":
            await message.answer_photo(menu_photo,reply_markup=all_keys[user.language]["Into booking"])
            await db.update_all_column(user.user_id)
            await db.update_column(user.user_id,"step",7)

        elif text == "🎉Aksiyalar" or text == "🎉Акции":
            await bot.send_message(user.user_id,dis_and_abus[user.language]["Discounts"])

        elif text == "ℹBiz haqimizda" or text == "ℹО нас":
            await bot.send_message(user.user_id,dis_and_abus[user.language]["About us"])

        elif text == "⚙Sozlamalar" or text == "⚙Настройки":
            await bot.send_message(user.user_id, await data_of_user(user))
            await bot.send_message(user.user_id, botext[user.language]["Which change"],reply_markup=all_keys[user.language]["Which change"])
            await db.update_column(user.user_id, "step", 4)
            await Details.change_data(message,user)

    elif user.step == 4: # Settings menu ni ko'rish
        await Details.change_data(message,user)

    elif user.step == 5: # Usernameni o'zgartirish
        await MSettings.change_username(message,user)

    elif user.step == 6: # Telefon raqamni o'zgartirish
        result = await MSettings.change_phone_number(message, user) # Agar telefon raqam qabul qilinsa hech nima sodir bo'lmaydi
        if result:
            await db.update_column(user.user_id, "step", 3)
            message.text == "⚙Sozlamalar"
            await user_is_booking(message)

        else:
            await bot.send_message(user.user_id,botext[user.language]["Expected error"]) # Aks holda xato haqida userga xabar beradi

    elif user.step == 7:
        await Booking.booking_foods(message)

    elif user.step >= 8 and user.step < 10:
        await Booking.selected_one(message, user)

    elif user.step == 10:
        await Booking.foods_accepted(message, user)

    elif user.step == 11:
        await Booking.get_description(message, user)

    elif user.step == 12:
        await Booking.get_user_status(message, user)

    elif user.step == 13:
        await Booking.get_user_pay(message, user)

async def go_to_location(message: Message):
    user = await db.get_user(message.from_user.id)
    await Details.get_user_location(message, user)


async def get_user_money(call: CallbackQuery):
    user = await db.get_user(call.from_user.id)
    orders = await db.get_user_orders(user)
    check_list = await return_orders(user, orders)
    await bot.delete_message(call.from_user.id, call.message.message_id)
    await bot.send_invoice(
        chat_id=call.from_user.id,
        title=user.username,
        description=check_list[0],
        payload="This is payload",
        provider_token=PAYME_TOKEN if call.data == "payme" or call.data == "пейми" else CLICK_TOKEN,
        currency="UZS",
        prices=[
            {
                "label": "UZS",
                "amount": int(f"{check_list[1]}00")
            }
        ]
    )

async def check_out(money: PreCheckoutQuery):
    await bot.answer_pre_checkout_query(money.id, ok=True)

async def final(message: Message):
    user = await db.get_user(message.from_user.id)
    if message.successful_payment.invoice_payload == "This is payload":
        orders = await db.get_user_orders(user)
        check_list = await final_check(user, orders)
        summa = check_list[1]
        check_list = check_list[0]
        await db.add_to_sales(user.user_id, summa)
        await db.update_column(user.user_id, "step", 3)
        await bot.send_message(user.user_id, check_list)
        await bot.send_message(-1001682833459, check_list)
        await bot.send_message(user.user_id, botext[user.language]["Thanks"],reply_markup=all_keys[user.language]["Main menu"])
        if user.status == "🚙Yetkazib berish" or user.status == "🚙Доставка": await bot.send_location(-1001682833459, user.location[0], user.location[1])



