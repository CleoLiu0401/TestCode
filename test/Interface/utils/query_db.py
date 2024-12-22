import pymysql as pymysql
from Interface.utils.read_data import GetData
from Interface.utils.log_util import logger


class QueryDB:

    def __init__(self):
        self.cursor = None
        self.conn = None

    def _connect_db(self):
        db_info = GetData().get_data_yaml("config/mysql.yaml")
        conn = pymysql.Connect(host=db_info['host'],
                               port=db_info['port'],
                               user=db_info['user'],
                               password=db_info['password'],
                               database=db_info['database'],
                               charset=db_info['charset'])
        logger.info("连接数据库")
        self.cursor = conn.cursor()

    def _close_db(self):
        logger.info("关闭数据库连接")
        self.cursor.close()
        self.conn.close()

    def query_catch_one(self, sql):
        logger.info("执行SQL语句：{}".format(sql))
        self._connect_db().execute(sql)
        data = self.cursor.fetchone()
        logger.info("执行结果：{}".format(data))
        self._close_db()
        return data[0]

    def query_catch_all(self, sql):
        logger.info("执行SQL语句：{}".format(sql))
        self._connect_db().execute(sql)
        datas = self.cursor.fetchall()
        logger.info("执行结果：{}".format(datas))
        self._close_db()
        return datas

    def execute_sql(self, sql):
        logger.info("执行SQL语句：{}".format(sql))
        self._connect_db().execute(sql)
        self.conn.commit()
        self._close_db()