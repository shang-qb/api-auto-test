import pymysql
import logging


class DBUtil:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def connect(self):
        """建立数据库连接"""
        try:
            self.conn = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database,
                charset='utf8mb4'
            )
            self.cursor = self.conn.cursor(pymysql.cursors.DictCursor)
            logging.info("数据库连接成功")
        except Exception as e:
            logging.error(f"数据库连接失败: {e}")
            raise

    def query_one(self, sql, params=None):
        """查询单条记录"""
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            logging.info(f"查询成功: {result}")
            return result
        except Exception as e:
            logging.error(f"查询失败: {e}")
            raise

    def query_all(self, sql, params=None):
        """查询所有记录"""
        try:
            self.cursor.execute(sql, params)
            result = self.cursor.fetchall()
            logging.info(f"查询成功，共 {len(result)} 条记录")
            return result
        except Exception as e:
            logging.error(f"查询失败: {e}")
            raise

    def execute(self, sql, params=None):
        """执行增删改"""
        try:
            self.cursor.execute(sql, params)
            self.conn.commit()
            logging.info("执行成功")
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            logging.error(f"执行失败: {e}")
            raise

    def close(self):
        """关闭连接"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        logging.info("数据库连接已关闭")
