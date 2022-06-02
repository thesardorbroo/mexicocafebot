from aiogram import executor
from aiogram.types import Message, CallbackQuery, PreCheckoutQuery, ContentType


from newProject.config.Config import dp
from newProject.core import Core


@dp.message_handler(commands=['start'])
async def botstarted(message: Message):
    await Core.pressed_start(message)

@dp.message_handler(content_types=['contact'])
async def send_phone_number(message: Message):
    await Core.sendPN(message)

@dp.message_handler(content_types=['text'])
async def to_main_menu(message: Message):
    await Core.user_is_booking(message)

@dp.callback_query_handler()
async def user_into_booking(call: CallbackQuery):
    await Core.get_user_money(call)

@dp.pre_checkout_query_handler()
async def pre_checkout(money: PreCheckoutQuery):
    await Core.check_out(money)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def success(message: Message):
    await Core.final(message)

@dp.message_handler(content_types=['location'])
async def send_location(message: Message):
    await Core.go_to_location(message)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
