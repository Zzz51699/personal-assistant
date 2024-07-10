import pymysql
from pymysql import cursors
import sqlite3
import datetime

conn = pymysql.connect(
    host='rm-2ze3v8kp5vs872zrmoo.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='Root123456',
    db='assistant',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

def query_user_by_username(username):
    sql = "select * from sys_user where username = %s"
    cur = conn.cursor()
    cur.execute(sql,[username])
    result = cur.fetchone()
    if result is None:
        return False  # 用户不存在
    else:
        return True  # 用户存在

def add_user(username,password):
    sql = "insert into sys_user (username,password) values (%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,[username,password])
    conn.commit()

def select_user(username):
    sql = "select * from sys_user where username = %s"
    cur = conn.cursor()
    cur.execute(sql,[username])
    res = cur.fetchone()
    return res

def query_message_by_user_id(user_id):
    sql = "select * from chat_message where user_id = %s order by message_time asc"
    cur = conn.cursor()
    cur.execute(sql, [user_id])
    # 字典类型的列表[{},{},{}]
    list = cur.fetchall()
    return list

def insert_chat_message(user_id,message,role,message_time):
    sql = "insert into chat_message (user_id, message,role,message_time) values (%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql,[user_id,message,role,message_time])
    conn.commit()
    last_row_id = cur.lastrowid
    return last_row_id

# 3、根据修改密码更新密码
def update_data(newpassword,username):
    # 准备SQL更新语句
    sql = "UPDATE sys_user SET password = %s WHERE username = %s"
    val = (newpassword, username)

    # 执行SQL语句
    cur = conn.cursor()
    cur.execute(sql, val)

def add_chat_message(user_id, message, role):
    sql = "insert into chat_message (user_id, message, role,message_time) values (%s,%s,%s,%s)"
    cur = conn.cursor()
    cur.execute(sql, [user_id, message, role, datetime.datetime.now()])
    conn.commit()

    # 提交到数据库执行
    conn.commit()