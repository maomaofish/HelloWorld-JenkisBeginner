import MySQLdb


conn = MySQLdb.connect(host='localhost', user='root',passwd='1234')
cursor = conn.cursor()
try:
    cursor.execute("CREATE DATABASE IF NOT EXISTS 'myblogdb'")
    conn.commit()
    print("OK")
except Exception as e:
    conn.rollback()
    conn.close()
    print(e)

