# 【关键代码】建立Python与MySQL的连接
# ==============================================
def get_conn():
    try:
        # 此行是连接数据库的核心语句
        conn = pymysql.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("数据库连接失败：", e)
        return None

# 关闭数据库连接与游标
def close(conn, cursor=None):
    if cursor:
        cursor.close()
    if conn:
        conn.close()
