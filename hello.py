#db 연결하기
import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='fullstack7', charset='utf8')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tbl_bbs WHERE memberId = 'tester2'")
    result = cursor.fetchall()
    for row in result:
        print(row)
except Exception as e:
    print(e)

finally:
    conn.close()
