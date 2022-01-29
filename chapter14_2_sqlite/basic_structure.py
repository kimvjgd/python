import sqlite3

def main():
    con = sqlite3.connect('addr.db')
    print('db 연결 성공')
    cursor = con.cursor()
    # contents
    cursor.execute("")          # 안에 쿼리 적어줘야함
    
    
    cursor.close()
    con.close()
    
main()