from . import db_models
from fastapi import FastAPI, File, UploadFile,Request
import pymysql
import time

def open():
    return pymysql.connect(host='localhost',
                        user='root',
                        password='',
                        database='uso_dev')

def fetch(sql:str):
    # 打开数据库连接
    db = open()
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        return cursor.fetchall()
    except pymysql.Error as e:  
        print(e.args[0], e.args[1])
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()

def exec(sql:str):
    # 打开数据库连接
    db = open()
    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e: 
        print(e.args[0], e.args[1])
        # 发生错误时回滚
        db.rollback()
    finally:
        # 关闭数据库连接
        db.close()


def GetCreative(creative_id:int):
    dbModel = db_models.DBMaskCreative
    sql = "SELECT * FROM tb_mask_creative \
        WHERE creative_id = %d" % creative_id
    re = dbModel.toModelFirstLine(dbModel,fetch(sql))
    return re

def CreateTask(task_id:str,creative_id:int):
    # SQL 插入语句
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    sql = "INSERT INTO tb_mask_task VALUES ('%s',%d,%d,'','%s');" % (task_id,creative_id,0,now)
    re = exec(sql)
    return re

def UpdateTask(status:int,task_id:str,video_src:str):
    # SQL 插入语句
    sql ="""UPDATE tb_mask_task SET status = %d, out_video_src= '%s' WHERE task_uuid = '%s';""" %(status,video_src,task_id)
    re = exec(sql)
    return re
