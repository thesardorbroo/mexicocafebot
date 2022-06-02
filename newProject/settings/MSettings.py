from aiogram.types import Message

from newProject.core.Core import user_is_booking
from newProject.texts.Text import settings_text,botext
from newProject.config.Config import bot,db,dp
from newProject.user.User import UserOB

async def change_username(message: Message, user: UserOB):
    await db.update_column(user.user_id,"username",message.text)
    await db.update_column(user.user_id,"step",3)
    message.text = "⚙Sozlamalar"
    await user_is_booking(message)

async def change_language(message: Message, user: UserOB):
    if user.language == 'UZ': await db.update_column(user.user_id,"language",'RU')
    else: await db.update_column(user.user_id,"language",'UZ')
    await db.update_column(user.user_id,"step",3)
    message.text = "⚙Sozlamalar"
    await user_is_booking(message)

async def change_phone_number(message: Message, user: UserOB):
    answer = True
    if "+" in message.text: message.text = message.text[1:]
    if len(message.text) >= 7 and len(message.text) <= 12:
        if message.text.isdigit() and (message.text[0] == '9' and message.text[1] == '9' and message.text[2] == '8'):
            await bot.send_message(user.user_id,botext[user.language]["Query Ok!"])
            await db.update_column(user.user_id,"phone_number",message.text)

        else: answer = False
    else: answer = False
    return answer
