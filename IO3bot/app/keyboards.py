from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils import keyboard
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

web_app_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Створити оголошення', web_app=WebAppInfo(url='https://itshnikisobuhovki.github.io/IO3bot/index.html'))]],
                                          resize_keyboard=True,
                input_field_placeholder="тисніть кнопку")



# main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Открыть веб страницу')]
#                                      ], web_app=WebAppInfo(url='https://itshnikisobuhovki.github.io/IO3bot/templates/index.html/telegram.html'),
#                                           one_time_keyboard=True,
#                                           resize_keyboard=True,
#                 input_field_placeholder="введіть адресу у довільній формі")

# main = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='XXX', callback_data="find_on_map")]])
# # property_types = ['квартира', 'будинок', 'земельна_ділянка', 'магазин_салон', 'ресторан_кафе',
# #                   'офіс', 'склад', 'пром_база', 'виробництво', 'база_відпочинку', 'готель',
# #                   'МАФ_кіоск', 'точка_на_базарі', 'АЗС', 'автомийка', 'СТО',
# #                   'фермерське_господарство', 'гараж_паркувальне_місце',]
# #
# #
# #
# # transaction_types = ['ОРЕНДА', 'ПРОДАЖ']
# #
# # async def reply_property_types():
# #     keyboard = ReplyKeyboardBuilder()
# #     for property_type in property_types:
# #         keyboard.add(KeyboardButton(text=property_type))
# #     return keyboard.adjust(4).as_markup()
# #
# # async def inline_property_types():
# #     keyboard = InlineKeyboardBuilder()
# #     for property_type in property_types:
# #         keyboard.add(InlineKeyboardButton(text=property_type, callback_data=property_type))
# #     return keyboard.adjust(3).as_markup()
#
# # main = InlineKeyboardMarkup(inline_keyboard=[
# #     [InlineKeyboardButton(text='Пошук на мапі', callback_data='find_on_map')]
# # ])
# #
# cur = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Євро', callback_data='EUR')],
#     [InlineKeyboardButton(text='Долари США', callback_data='USD')],
#     [InlineKeyboardButton(text='Гривні', callback_data='UAGRN')],
# ])
