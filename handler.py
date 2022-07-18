from aiogram.types import Message
from bot import bot, dp
from data_base_tools.database_tools import DataBaseTools
from keyboards import get_keyboard


@dp.message_handler(commands="Files")
async def cmd_numbers(message: Message):
    chat_id = message.chat.id
    info = DataBaseTools().get_last_row_from_database()
    while True:
        await bot.send_message(chat_id, text=f"🏢  <i>Фирма:</i>                     <b>{info[1]}</b>\n"
                                             f"📝  <i>Название:</i>                <b>{info[4]}</b>\n"
                                             f"🟦  <i>Размер:</i>                     <b>{info[2]}</b>\n"
                                             f"☑  <i>Количество:</i>           <b>{info[3]}</b>\n"
                                             f"🕐  <i>Дата и время:</i>       <b>{info[5]}</b>\n"
                                             f"📦  <i>Статус:</i>                  <b> ГОТОВ ✅ </b>\n"
                                             f"🏷  <i>Номер:</i>                      <b>{info[0]}</b>",
                               parse_mode="HTML", reply_markup=get_keyboard())
