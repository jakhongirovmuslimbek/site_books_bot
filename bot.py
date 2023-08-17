import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
from buttons import *
from aiogram.dispatcher.filters import Text
from api import *
import config

# Configure logging
logging.basicConfig(level=logging.INFO)
# Initialize bot and dispatcher
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    markup = category_buttons()
    data = user_create(message.from_user.id)
    if data:
        await message.answer("Assalomu alekum")
        await message.answer("<b>Kategoriyalardan birini tanlang...</b>", parse_mode='HTML', reply_markup=markup)
    else:
        await message.answer("Salom")
        await message.answer("<b>Kategoriyalardan birini tanlang...</b>", parse_mode='HTML', reply_markup=markup)
    
        
@dp.callback_query_handler(Text(startswith='category_'))
async def echo(call: types.CallbackQuery):
    index = call.data.index('_')
    id = call.data[index+1:]
    markup = buttons_by_category_id(id)
    if markup['inline_keyboard'] != []:
        await call.message.answer("<b>Kitoblardan birini tanlang...</b>", parse_mode='HTML', reply_markup=markup)
    else:
        await call.answer("Tez orada")

@dp.callback_query_handler(Text(startswith='book_'))
async def echo(call: types.CallbackQuery):
    index = call.data.index('_')
    id = call.data[index+1:]
    data = get_book(id)
    info = ''
    photo = ''
    if data:
        if data[0]['book_img']:
            photo = data[0]['book_img']
            info = f"""
Nomi: {data[0]['book_name']}
Yozuvchi: {data[0]['book_the_author']}
Janri: {data[0]['book_genre']}"""
        else:
            photo = open('img/default.jng', 'rb')
            info = f"""
Nomi: {data[0]['book_name']}
Yozuvchi: {data[0]['book_the_author']}
Janri: {data[0]['book_genre']}"""

        button = InlineKeyboardMarkup(row_width=2)
        button.insert(types.InlineKeyboardButton(text='⬅️ Ortga', callback_data=f"back_{data[0]['category']}"))
        await call.message.answer_photo(photo, info, reply_markup=button)

# backs
@dp.callback_query_handler(Text(startswith='ortga'))
async def echo(call: types.CallbackQuery):
    markup = category_buttons()
    await call.message.answer("<b>Kategoriyalardan birini tanlang...</b>", parse_mode='HTML', reply_markup=markup)   

@dp.callback_query_handler(Text(startswith='back_'))
async def echo(call: types.CallbackQuery):
    index = call.data.index('_')
    id = call.data[index+1:]
    markup = buttons_by_category_id(id)
    if markup['inline_keyboard'] != []:
        await call.message.answer("<b>Kitoblardan birini tanlang...</b>", parse_mode='HTML', reply_markup=markup)
    else:
        await call.answer("Tez orada")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)