import pymysql
from CreateBot import bot

def sql_start():
    global data, cur_1
    data = pymysql.connect(host='babuskyb.beget.tech',user='babuskyb_categor',password='z78&pJu*',database='babuskyb_categor', charset='utf8mb4', collation='utf8mb4_general_ci')
    cur_1 = data.cursor()