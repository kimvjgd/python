import sqlite3
from models import TblAddr

def main():
    con = sqlite3.connect('addr.db')
    print('db 연결 성공')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM tblAddr order by name desc")
    
    # contents
    # 따라서 if record == None: break    을 무조건 써줘야한다.   -> 데이터가 없으면 그냥 빈 리스트가 아니라 None으로 반환하기 때문에
    while True:
        record = cursor.fetchone()
        if record == None : break
        record = TblAddr(*record)
        print(f'이름: {record.name}, 전화번호: {record.phone}, 주소: {record.addr}')
    
    cursor.close()
    con.close()
    
main()

