# pip install mysqlclient 하고
# import MySQLdb              # for connecting with mariaDB
import mysql.connector
import sys


try:
    # con = MySQLdb.connect(db='sqldb', host='localhost', user='root', passwd='wjddms12')     # port=자신의 포트번호 (if port 따로 바꿨으면)
    con = mysql.connector.connect(db='iot_db', host='localhost', user='iot', passwd='wjddms12')         # 위에꺼 오류떠서 그냥 다른것 import
    # con = sqlite3.connect('addr.db')
    print('데이터 베이스 연결 성공')
    

except Exception as e:
    print('데이터 베이스 연결에 실패했습니다.')
    print(e)
    sys.exit(0)


# 맥북은 나중에 다시 도전!!!   방법은 맞다 나중에 에러를 찾기로~! 

