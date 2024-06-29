# encoding=utf-8

import pymysql
from pymongo import MongoClient
from rediscluster import RedisCluster

from Utils.Log import Msg


log_msg = Msg(name='sql_log')


class Mysql:
    def __init__(self, host, user, pwd, port=3306, db='', charset='utf8'):
        self.host = host
        self.db = db
        self.user = user
        self.pwd = pwd
        self.port = port
        self.charset = charset

    def connect(self):
        try:
            db = pymysql.connect(host=self.host, database=self.db, user=self.user, password=self.pwd, port=self.port,
                                 charset=self.charset)
            return db
        except Exception:
            raise Exception('数据库连接失败')

    def select_sql(self, sql, data='one'):
        db = self.connect()
        cursor = db.cursor()
        cursor.execute(sql)
        log_msg.info(f"执行sql语句：{sql}")
        if data == 'one':
            ret = cursor.fetchone()
        else:
            ret = cursor.fetchall()
        cursor.close()
        db.close()
        return ret

    def sql_perform(self, sql):
        db = self.connect()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            log_msg.info(f"执行sql语句：{sql}")
            db.commit()
        except Exception as e:
            print(e)
        cursor.close()
        db.close()


class Mongo:
    def __init__(self, host, username="", password="", port=27017, db_name="", table_name=""):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.coon = MongoClient(host=self.host, port=self.port, username=self.username, password=self.password,
                                retrywrites=False)  # 解决不支持可重写报错

        self.db = self.coon[f'{db_name}']
        self.cl = self.db[f'{table_name}']

    def update_(self, filters, up_date):
        odl_ = filters
        new_ = {"$set": up_date}
        ret = self.cl.update_many(odl_, new_)
        print('更新数据条数:', ret.modified_count)

    def update_one(self, filters, up_date):
        odl_ = filters
        new_ = {"$set": up_date}
        ret = self.cl.update_one(odl_, new_)
        print('更新数据条数:', ret.modified_count)

    def delete_(self, filters):
        odl_ = filters
        self.cl.delete_one(odl_)
        print('MongoDB语句执行成功')

    def close(self):
        self.coon.close()


class Redis:
    def __init__(self, host):
        startup_nodes = host
        try:
            self.rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True, skip_full_coverage_check=True)
            print('redis connection succeeded')
        except Exception as e:
            print(f'redis连接错误:error {e}')

    def delete_(self, key):
        ret = self.rc.delete(key)
        print(ret)


# if __name__ == '__main__':
#     msg = get_base('pre', 'us')
#     # mongo = Mongo(host=msg['mongo_host'], username=msg['mongo_user'], password=msg['mongo_pwd'], db_name='oas',
#     #               table_name='oas_mkt_user_option')
#     # mongo.update_(filters={"bizId": "8"}, up_date={"activityId": 321})
#     # mongo.close()
#     redis_ = Redis(host=msg['redis'])
#     redis_.delete_(key="oas.activity.act_eedd")
