from CreateBot import dp, bot
from aiogram import types, Dispatcher
from keyboards.client_kb import keyboardClient
from aiogram.dispatcher import FSMContext
from database import db_open
import pymysql
from keyboards.client_kb import keyboards


# обработка команды /start (стартовая клавиатура клавиатура и вывод сообщения)
async def cmd_start(message: types.Message, state: FSMContext):
    print(message.text)
    await message.answer("Здравствуйте. Кажется у Вас есть вопрос? Задайте его напрямую или через меню.", reply_markup=keyboardClient)

@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    print(call.data)
    db_open.sql_start()
    #answer=cur_1.execute('SELECT Ответ FROM Категории WHERE Категория=?', (call.data,)).fetchone()
    parameters = "SELECT * FROM Категории WHERE Категория=%s"
    tuple = (call.data)
    db_open.cur_1.execute(parameters, tuple)
    db_open.data.close()
    answer = db_open.cur_1.fetchone()

    await call.message.answer(answer[1], reply_markup=keyboards[call.data])

def handlers_menu (dp:Dispatcher):
    dp.register_message_handler(cmd_start, commands = ["start"], state = None)
