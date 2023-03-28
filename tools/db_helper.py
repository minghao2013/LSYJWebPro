import pymysql
from dbutils.pooled_db import PooledDB


class DBHelper(object):

    def __init__(self):
        # TODO 此处配置，可以去配置文件中读取。
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=5,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=3,  # 链接池中最多闲置的链接，0和None不限制
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host='sjwaiwang.mysql.rds.aliyuncs.com',
            port=3306,
            user='liangshiyaji',
            password='Liangshiyaji2018',
            database='liangshiyaji',
            charset='utf8'
        )

    def get_conn_cursor(self):
        conn = self.pool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn, cursor

    def close_conn_cursor(self, *args):
        for item in args:
            item.close()

    # 执行sql增 删,改 语句,返回受影响的条数
    def exec(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()

        result_count = cursor.execute(sql, kwargs)
        conn.commit()

        self.close_conn_cursor(conn, cursor)
        return result_count

    # 查询单个返回值
    def fetch_one(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()

        cursor.execute(sql, kwargs)
        result = cursor.fetchone()

        self.close_conn_cursor(conn, cursor)
        return result

    # 查询所有的返回值
    def fetch_all(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()

        cursor.execute(sql, kwargs)
        result = cursor.fetchall()

        self.close_conn_cursor(conn, cursor)

        return result


if __name__ == '__main__':
    db = DBHelper()
    mobile = "13145456767"
    sql = "delete from  ob_member where  mobile='13145456767'"
    print(sql)
    result = db.fetch_one(sql)
    print(result)
