import pymysql as pymysql


class QueryDB:
    def query_db(self, sql, database_info):
        conn = pymysql.Connect(**database_info)
        cursor = conn.cursor()
        cursor.execute(sql)
        datas = cursor.fetchall()
        cursor.close()
        conn.close()
        return datas