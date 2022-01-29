import sqlite3
from models import TblAddr

def main():
    con = sqlite3.connect('addr.db')
    print('db 연결 성공')
    cursor = con.cursor()
    
    # contents
    cursor.execute("SELECT * FROM tblAddr WHERE name = '김상현'")
    
    record = cursor.fetchone()
    if record: 
        record = TblAddr(*record)
        print(f"김상현은 {record.addr}에 살고 있습니다.")
    else : print("김상현은 없는 이름입니다.")
    
    cursor.close()
    con.close()
    
main()