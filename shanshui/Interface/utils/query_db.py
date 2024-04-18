import pymysql as pymysql

from Interface.utils.log_util import logger
from Interface.utils.read_data import GetData


class QueryDB:

    @classmethod
    def query_db_one(cls, sql):
        db_info = GetData.get_data_yaml("config/mysql_conf.yaml")
        conn = pymysql.connect(host=db_info['host'],
                               port=db_info['port'],
                               user=db_info['user'],
                               password=db_info['password'],
                               database=db_info['database'],
                               charset=db_info['charset'])
        logger.info("连接数据库")
        cursor = conn.cursor()
        logger.info(f"执行SQL：{sql}")
        cursor.execute(sql)
        data = cursor.fetchone()
        logger.info(f"执行结果：{data}")
        cursor.close()
        logger.info("断开数据库连接")
        conn.close()
        return data[0]

    @classmethod
    def query_db_all(cls, sql):
        db_info = GetData.get_data_yaml("config/mysql_conf.yaml")
        conn = pymysql.connect(host=db_info['host'],
                               port=db_info['port'],
                               user=db_info['user'],
                               password=db_info['password'],
                               database=db_info['database'],
                               charset=db_info['charset'])
        logger.info("连接数据库")
        cursor = conn.cursor()
        logger.info(f"执行SQL：{sql}")
        cursor.execute(sql)
        datas = cursor.fetchall()
        logger.info(f"执行结果：{datas}")
        cursor.close()
        logger.info("断开数据库连接")
        conn.close()
        return datas

    @classmethod
    def query_db_old(cls, sql, database_info):
        conn = pymysql.connect(**database_info)
        logger.info("连接数据库")
        cursor = conn.cursor()
        logger.info(f"执行SQL：{sql}")
        cursor.execute(sql)
        datas = cursor.fetchall()
        logger.info(f"执行结果：{datas}")
        cursor.close()
        logger.info("断开数据库连接")
        conn.close()
        return datas
