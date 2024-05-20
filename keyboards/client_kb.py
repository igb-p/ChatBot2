from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

MainMenuButton1 = InlineKeyboardButton(text="Оформить кредит", callback_data="кредит")
MainMenuButton2 = InlineKeyboardButton(text="Отделения", callback_data="отделения")
MainMenuButton3 = InlineKeyboardButton(text="Оформить вклад", callback_data="вклад")
MainMenuButton4 = InlineKeyboardButton(text="Подобрать карту", callback_data="карты")

keyboardClient= InlineKeyboardMarkup(row_width=1,resize_keyboard=True, one_time_keyboard=True)

keyboardClient.row(MainMenuButton1)
keyboardClient.row(MainMenuButton2)
keyboardClient.row(MainMenuButton3)
keyboardClient.row(MainMenuButton4)


keyboards={}

creditButton1 = InlineKeyboardButton(text="Кредит наличными", callback_data="кредит наличными")
creditButton2 = InlineKeyboardButton(text="Ипотека", callback_data="ипотека")
creditButton3 = InlineKeyboardButton(text="Автокредит", callback_data="автокредит")

keyboardCredit = InlineKeyboardMarkup(row_width=1,resize_keyboard=True, one_time_keyboard=True)

keyboardCredit.row(creditButton1)
keyboardCredit.row(creditButton2)
keyboardCredit.row(creditButton3)

keyboards['кредит']=keyboardCredit

cardButton1 = InlineKeyboardButton(text="Кредитная карта", callback_data="кредитная карта")
cardButton2 = InlineKeyboardButton(text="Дебетовая карта", callback_data="дебетовая карта")

keyboardCard = InlineKeyboardMarkup(row_width=1,resize_keyboard=True, one_time_keyboard=True)

keyboardCard.row(cardButton1)
keyboardCard.row(cardButton2)

keyboards['карты']=keyboardCard


debitButton1 = InlineKeyboardButton(text="Для ребенка", callback_data="карта для ребенка")
debitButton2 = InlineKeyboardButton(text="Для зарплаты", callback_data="зарплатная карта")
debitButton3 = InlineKeyboardButton(text="Для соц. выплат", callback_data="карта для соц. выплат")

keyboardDebit = InlineKeyboardMarkup(row_width=1,resize_keyboard=True, one_time_keyboard=True)

keyboardDebit.row(debitButton1)
keyboardDebit.row(debitButton2)
keyboardDebit.row(debitButton3)

keyboards['дебетовая карта']=keyboardDebit


departmentButton1 = InlineKeyboardButton(text="Томск", callback_data="Томск")
departmentButton2 = InlineKeyboardButton(text="Северск", callback_data="Северск")
departmentButton3 = InlineKeyboardButton(text="Стрежевой", callback_data="Стрежевой")

keyboardDepartment = InlineKeyboardMarkup(row_width=1,resize_keyboard=True, one_time_keyboard=True)

keyboardDepartment.row(departmentButton1)
keyboardDepartment.row(departmentButton2)
keyboardDepartment.row(departmentButton3)

keyboards['отделения']=keyboardDepartment


keyboards['ошибка']=None
keyboards['автокредит']=None
keyboards['ипотека']=None
keyboards['кредит наличными']=None
keyboards['карта для ребенка']=None
keyboards['зарплатная карта']=None
keyboards['карта для соц. выплат']=None
keyboards['кредитная карта']=None
keyboards['Томск']=None
keyboards['Северск']=None
keyboards['Стрежевой']=None
keyboards['вклад']=None






