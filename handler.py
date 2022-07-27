from aiogram.types import Message, CallbackQuery
from bot import bot, dp
from data_base_tools.database_tools import DataBaseTools
from keyboards import get_keyboard, ready_keyboard, delivered_keyboard
from datetime import datetime


@dp.message_handler(commands="Files")
async def get_last_iteration(message: Message):
    chat_id = message.chat.id
    info = DataBaseTools().get_last_row_from_database()
    await bot.send_message(chat_id, text=f"🏢  <i>Фирма:</i>                     <b>{info[1]}</b>\n"
                                         f"📝  <i>Название:</i>                <b>{info[4]}</b>\n"
                                         f"🟦  <i>Размер:</i>                     <b>{info[2]}</b>\n"
                                         f"☑  <i>Количество:</i>           <b>{info[3]}</b>\n"
                                         f"🕐  <i>Дата и время:</i>       <b>{info[5]}</b>\n"
                                         f"📦  <i>Статус:</i>                  <b> 🟨 В ОЧЕРЕДИ 🟨 </b>\n"
                                         f"🏷  <i>Номер:</i>                      <b>{info[0]}</b>",
                           parse_mode="HTML", reply_markup=get_keyboard())


@dp.callback_query_handler(text="ready")
async def send_random_value(call: CallbackQuery):
    info = DataBaseTools().get_last_row_from_database()
    date_time = datetime.now().strftime("%d-%m-%Y   %H:%M:%S")
    await call.message.edit_text(text=f"🏢  <i>Фирма:</i>                     <b>{info[1]}</b>\n"
                                      f"📝  <i>Название:</i>                <b>{info[4]}</b>\n"
                                      f"🟦  <i>Размер:</i>                     <b>{info[2]}</b>\n"
                                      f"☑  <i>Количество:</i>           <b>{info[3]}</b>\n"
                                      f"🕐  <i>Дата и время:</i>       <b>{info[5]}</b>\n"
                                      f"📦  <i>Статус:</i>                   <b> ✅ ГОТОВ ✅</b>\n"
                                      f"⏲  <i>Когда готов:</i>          <b>{date_time}</b>\n"
                                      f"🏷  <i>Номер:</i>                      <b>{info[0]}</b>",
                                 parse_mode="HTML", reply_markup=ready_keyboard())
    await call.answer(text="Молодец")


@dp.callback_query_handler(text="delivered")
async def send_random_value(call: CallbackQuery):
    info = DataBaseTools().get_last_row_from_database()
    date_time = datetime.now().strftime("%d-%m-%Y   %H:%M:%S")
    await call.message.edit_text(text=f"🏢  <i>Фирма:</i>                     <b>{info[1]}</b>\n"
                                      f"📝  <i>Название:</i>                <b>{info[4]}</b>\n"
                                      f"🟦  <i>Размер:</i>                     <b>{info[2]}</b>\n"
                                      f"☑  <i>Количество:</i>           <b>{info[3]}</b>\n"
                                      f"🕐  <i>Дата и время:</i>       <b>{info[5]}</b>\n"
                                      f"📦  <i>Статус:</i>                  <b> ✅ ГОТОВ ✅</b>\n"
                                      f"⏲  <i>Когда готов:</i>          <b>{date_time}</b>\n"
                                      f"📦  <i>Доставка:</i>               <b>🚛ДОСТАВЛЕН🚛</b>\n"
                                      f"📦  <i>Когда доставлен:</i> <b>{date_time}</b>\n"
                                      f"🏷  <i>Номер:</i>                      <b>{info[0]}</b>",
                                 parse_mode="HTML", reply_markup=delivered_keyboard())
    await call.answer(text="Молодец")


@dp.callback_query_handler(text="cancelled")
async def send_random_value(call: CallbackQuery):
    await call.message.delete()
