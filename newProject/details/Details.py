from aiogram.types import Message

from newProject.texts.Text import *
from newProject.user.User import UserOB
from newProject.keys.MyKeyboards import *
from newProject.settings import MSettings
from newProject.config.Config import bot,db


async def addNewUser(message: Message, user: UserOB):
    user_id = message.from_user.id
    text = message.text
    if user.step == 1 :
        if text == "uz🇺🇿":
            await db.update_column(user_id,"language", 'UZ')
            await bot.send_message(user_id,botext["UZ"]["Enter name"],reply_markup=remove)
            await db.update_column(user_id,"step",2)
        elif text == "ru🇷🇺":
            await db.update_column(user_id, "language", 'RU')
            await bot.send_message(user_id, botext["RU"]["Enter name"],reply_markup=remove)
            await db.update_column(user_id, "step", 2)

    elif user.step == 2:
        await bot.send_message(user.user_id,botext[user.language]["Send PN"],reply_markup=all_keys[user.language]["Send PN"])
        await db.update_column(user.user_id,"username",f"{text}")
        await db.update_column(user.user_id,"step",3)

async def userIsAvailable(message: Message):
    # await db.update_all_column(message.from_user.id)
    user = await db.get_user(message.from_user.id)

    await bot.send_message(user.user_id,botext[user.language]["Main menu"],reply_markup=all_keys[user.language]["Main menu"])
    await db.update_column(user.user_id,"step",3)

async def sendPhoneNumber(message: Message, user: UserOB):
    await db.update_column(user.user_id,"phone_number",message.contact.phone_number)
    await bot.send_message(user.user_id,botext[user.language]["Main menu"],reply_markup=all_keys[user.language]["Main menu"])

async def change_data(message: Message, user: UserOB):
    text = message.text

    if text == "Ismni o'zgartirish" or text == "Смена имени": # Ismni o'zgartirish
        await db.update_column(user.user_id,"step",5)
        await bot.send_message(user.user_id, settings_text[user.language]["Change username"],reply_markup=remove)

    elif text == "Telefon raqamni o'zgartirish" or text == "Смена номера телефона": # Telefon raqamni o'zgartirish
        await db.update_column(user.user_id,"step",6)
        await bot.send_message(user.user_id,settings_text[user.language]["Change phone_number"],reply_markup=remove)

    elif text == "Tilni o'zgartirish" or text == "Изменение языка": # Tilni o'zgartirish
        await MSettings.change_language(message, user)

    elif text == "Orqaga" or text == "Назад":
        await bot.send_message(user.user_id,botext[user.language]["Main menu"],reply_markup=all_keys[user.language]["Main menu"])
        await db.update_column(user.user_id, "step", 3)

async def get_user_location(message: Message, user: UserOB):
    """
    Userni locationni shu metod qabul qiladi
    """
    await bot.send_message(user.user_id, botext[user.language]["Payments"], reply_markup=all_keys[user.language]["Payments"])
    await db.update_column(user.user_id, "location", f"{message.location.latitude}:{message.location.longitude}")
    await db.update_column(user.user_id, "step", 13)

