from dataclasses import dataclass
from database import con

# 데이터베이스를 위한 모델 클래스명 관례
# 클래스명 관례 준수
# 테이블명
@dataclass
class TblAddr:
    name : str
    phone : str
    addr : str
    
    # CRUD 작업 메서드를 출력
    def insert(self):          # 아래의 쿼리문에서 모두 '' 로 묶어줘야한다.
        sql = f"INSERT INTO tblAddr values('{self.name}', '{self.phone}', '{self.addr}')"
        cursor = con.cursor()
        con.execute(sql)
        cursor.close()
    
    # select 는 인스턴스와는 무관하다.   
    # -> static method & class method
    @classmethod
    def all(cls):
        cursor = con.cursor()
        sql = 'SELECT * FROM tblAddr'
        cursor.execute(sql)
        records = cursor.fetchall()
        records = list(map(lambda r: cls(*r), records))         # 튜플을 모델 클래스 인스턴스로 변환
        cursor.close()
        return records
        
    # key column으로 1개 찾는거...
    @classmethod
    def get(cls, pk):
        cursor = con.cursor()
        sql = f"SELECT * FROM tblAddr Where name = '{pk}'"
        cursor.execute(sql)
        record = cursor.fetchone()
        if record:      # 존재하면 모델 클래스 인스턴스로 변환
            record = cls(*record)

        return record
    
    
    def update(self):
        cursor = con.cursor()
        sql = f"""
            UPDATE tblAddr
            SET
                phone = '{self.phone}',
                addr = '{self.addr}'
            where name = '{self.name}'
        """
        cursor.execute(sql)
        con.commit()
        cursor.close()
        
    
    def remove(self):
        cursor = con.cursor()
        sql = f"DELETE FROM tblAddr WHERE name = '{self.name}'"
        cursor.execute(sql)
        con.commit()
        cursor.close()
        
        
    
    
    
    
    
    
if __name__ == '__main__':
    record = ('김상형', '010-1111-2222', '부산')
    print(record)
    print(*record)

    a = TblAddr(*record)
    print(a)
