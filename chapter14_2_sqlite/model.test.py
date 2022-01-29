from models import TblAddr

import sqlite3
con = sqlite3.connect('addr.db')

# 전체 목록 얻기 테스트
book = TblAddr.all()
for a in book:
    print(a)

# 단일 데이터 추출
item = TblAddr.get('홍길동197')
print(item)

item = TblAddr.get('홍길동397')
print(item)

# insert 테스트
print('insert 테스트')
item = TblAddr('김동현', '010-0000-0000','향동')              # 두번째 실행할때는 에러가 뜬다.
item.insert()
item = TblAddr.get('김동현')
print(item)

# update 테스트
print('update 테스트')
item.phone = '010-2222-4444'
item.update()
item = TblAddr.get('김동현')
print(item)

# remove 테스트
print('remove 테스트')
item.remove()
item = TblAddr.get('김동현')
print(item)



con.close()