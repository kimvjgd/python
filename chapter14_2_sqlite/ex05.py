# SELECT 빼고 INSERT UPDATE DELETE는 commit()을 해줘야한다.!!!

import sqlite3

def main():
    con = sqlite3.connect('addr.db')
    print('db 연결 성공')
    cursor = con.cursor()
    # contents
    cursor.execute("UPDATE tblAddr SET addr = '제주도' WHERE name = '김상현'")          # 안에 쿼리 적어줘야함
    con.commit()
    
    
    cursor.close()
    con.close()
    
main()