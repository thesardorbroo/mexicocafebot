from aiogram import Bot
from aiogram import Dispatcher
from newProject.database.BotDB import Botdb

API_TOKEN = "5215022026:AAG0isJMty_zfawvfiXBFnl3eIM1RXNXdvc"
PAYME_TOKEN = "371317599:TEST:1654109566957"
CLICK_TOKEN = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)
db = Botdb()

menu_photo = "AgACAgIAAxkDAAICsmKPZ0nNmkct2_sooWmQ1E1G-bM7AAJDuzEbLaeASPB2EOHmDoD5AQADAgADcwADJAQ"
burger_photo = "AgACAgIAAxkDAAIDRWKQ8gEP2chdtvWJG8i-d3Q64uzhAAL_vjEbQl-JSESkFVPn7PgjAQADAgADcwADJAQ"