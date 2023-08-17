from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from api import *

def category_buttons():
    data = get_categories()
    button = InlineKeyboardMarkup(row_width=2)
    for i in data:
        button.insert(InlineKeyboardButton(text=i['name'], callback_data=f"category_{i['id']}"))   
    return button


def buttons_by_category_id(id):
    data = get_by_category_id(id)
    button = InlineKeyboardMarkup(row_width=2)
    if data != []:
        for i in data:
            button.insert(InlineKeyboardButton(text=i['book_name'], callback_data=f"book_{i['id']}"))
        button.insert(InlineKeyboardButton(text="⬅️ Ortga", callback_data='ortga'))    
        return button
    else:
        button.insert(InlineKeyboardButton(text="⬅️ Ortga", callback_data='ortga'))
        return button
        