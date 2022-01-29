# 테이블 생성 및 데이터 추가
import sqlite3

def main():
    con = sqlite3.connect('addr.db')
    print('db 연결 성공')
    cursor = con.cursor()
    cursor.execute('DROP TABLE IF EXISTS tblAddr')

    cursor.execute("""
    CREATE TABLE tblAddr(
        name CHAR(16) PRIMARY KEY,
        phone CHAR(16),
        addr TEXT
    )
    """)


    # 데이터 추가(insert 문)
    cursor.execute("INSERT INTO tblAddr VALUES('김상현', '123-4567', '오산')")
    cursor.execute("INSERT INTO tblAddr VALUES('한경은', '341-3456', '군산')")
    cursor.execute("INSERT INTO tblAddr VALUES('뿌뿌잉', '495-4562', '안산')")

    # 200개의 테스트 데이터를 insert 하기
    for ix in range(1, 201):
        sql = f"INSERT INTO tblAddr VALUES('홍길동{ix:03}', '010-1111-{ix:04}', '서울')"
        print(sql)
        cursor.execute(sql)

    
    
    con.commit()                # 메모리 반영
    
    cursor.close()
    con.close()

main()