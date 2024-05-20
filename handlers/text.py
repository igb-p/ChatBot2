from CreateBot import dp, bot
from aiogram import types, Dispatcher
#from database.db_open import cur_1
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards.client_kb import keyboards
from database import db_open


async def cmd_text(message: types.Message, state: FSMContext):
        if message.text[0] != '/':
            import pickle
            from ML.preprocessing import text_preprocessing
            import pymysql

            db_open.sql_start()
            text = text_preprocessing(message.text)
            x=[text]
            with open ('data.pickle', 'rb') as f:
                text_clf = pickle.load(f)
            pre = text_clf.predict(x)
            scores = text_clf.predict_proba(x).tolist()[0]
            if max(scores)<0.24:
                pre[0] = 'ошибка'
            #answer=cur_1.execute('SELECT Ответ FROM Категории WHERE Категория=?', (pre[0], )).fetchone()
            parameters = "SELECT * FROM Категории WHERE Категория=%s"
            tuple = (pre[0])
            db_open.cur_1.execute(parameters, tuple)
            answer = db_open.cur_1.fetchone()
            db_open.data.close()
            await message.reply(answer[1], reply_markup=keyboards[pre[0]])

def handlers_text (dp:Dispatcher):
    dp.register_message_handler(cmd_text, staкte = None )