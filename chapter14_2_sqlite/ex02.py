import sqlite3
from models import TblAddr

def main():
    con = sqlite3.connect('addr.db')          # 혹시 마리아 db용으로 하겠다면 여기 커넥션 객체만 바꿔주면 된다.   아래의 나머지 것들은 파이썬의 표준이다. 
    print('db 연결 성공')
    cursor = con.cursor()
    
    cursor.execute("SELECT * FROM tblAddr")             
    # cursor.execute("SELECT * FROM tblAddr where name='쀼뀨꺄아'")              # 이런 db가 없으면 비어있는 list가 된다. 안전하게 된다.
    
    table = cursor.fetchall()      # 데이터 베이스 불러와서 여기서 읽어와야함      # list 안에 개개인은 튜플로 정보저장되어있다.
    # 한개씩 뽑아서 보여면 cursor.fetchone() 이 있다.    -> fetchall은 없는것 불러오면 빈 리스트지만 fetchone은 none이 된다.
    # print(type(table))
    # print(type(table[0]))
    # print(table[0][0])

    # 해당 tuple을 -> 모델클래스로 변환해서 사용하는 것을 권장
    table = list(map(lambda r: TblAddr(*r), table))
    
    
        
    
    
    
    for record in table:
        
        print(f'이름: {record.name}, 전화번호: {record.phone}, 주소: {record.addr}')
    
    cursor.close()
    con.close()
    
main()