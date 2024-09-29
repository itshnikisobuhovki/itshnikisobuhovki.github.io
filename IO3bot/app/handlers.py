from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.fsm import state
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb

router = Router()

class GetInfo(StatesGroup):
    adres = State()
    currency = State()
    price = State()
    commission = State()
    number = State()
    name = State()
    type_of_transaction = State()
    type_of_property = State()


@router.message(CommandStart())
async def get_info(message: Message):
    await message.answer('Привет! Нажмите на кнопку ниже, чтобы открыть веб-страницу:',
                         reply_markup=kb.web_app_keyboard)
# @router.message(CommandStart())
# async def get_info(message: Message, state: FSMContext):
#     await state.set_state(GetInfo.adres)
#     await message.answer('Введіть адресу у довільній формі і потім тисніть "XXX" щоб додати адресу до оголошення',
#                           reply_markup=kb.main)
#
#
# @router.callback_query(F.data == 'find_on_map')
# async def get_adress(callback: CallbackQuery):
#     # текст в виде всплывающего уведомления оставить пустым если он не нужен
#     await callback.answer('Введіть адресу у довільній формі починаючи з вулиці'
#                           # всплывающее уведомление с кнопкой "Ок"
#                           #  , show_alert=True
#                           )
#     # текст отправится в чат
#     # await callback.message.answer('Введіть адресу у довільній формі починаючи з вулиці')
#     await callback.message.edit_text('Оберіть валюту', reply_markup=kb.cur)

# @router.message(Command('proptypes'))
# async def start_adress(message: Message):
#     await message.answer('Оберіть тип нерухомості',
#                          reply_markup=await kb.reply_property_types())
#
# @router.message(Command('proptypesinline'))
# async def start_adress(message: Message):
#     await message.answer('Оберіть тип нерухомості',
#                          reply_markup=await kb.inline_property_types())
#
# @router.message(CommandStart())
# async def start_adress(message: Message):
#     await message.answer('Введіть адресу',
#                          reply_markup=kb.main)
#
# @router.callback_query(F.data == 'find_on_map')
# async def get_adress(callback: CallbackQuery):
#     # текст в виде всплывающего уведомления оставить пустым если он не нужен
#     await callback.answer('Введіть адресу у довільній формі починаючи з вулиці'
#                           # всплывающее уведомление с кнопкой "Ок"
#                           # , show_alert=True
#                           )
#     # текст отправится в чат
#     # await callback.message.answer('Введіть адресу у довільній формі починаючи з вулиці')
#     await callback.message.edit_text('Оберіть валюту', reply_markup=await kb.inline_property_types())
#
# @router.callback_query(F.data == 'квартира')
# async def get_type(callback: CallbackQuery):
#     await callback.answer()
#     await callback.message.answer(f'Ви ввели квартира')
