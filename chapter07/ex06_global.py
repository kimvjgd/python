# 여기서의 temp는 지역 변수라서 특정 범위에서만 유효하다.

def kim():
    temp = '김과장의 함수'
    print(temp)

def lee():
    temp = 2**10
    return temp

def park(a):
    temp = a*2
    print(temp)
    
kim()
print(lee())
park(6)

# 전역 변수는 어디서든 접근 가능하다
sale_rate = 0.9

def kim():
    print('오늘의 할인율', sale_rate)
    
def lee():
    price = 1000
    print(price * sale_rate)


kim()
print('할인율이 바뀌었습니다. 0.9 -> 0.8')
sale_rate = 0.8
lee()


# !!!!!!!!!!!!!! 중요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 중요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 중요 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! 중요 !!!!!!!!!!!!!!!!!!!!
price = 1000

def sale():
    price = 500
    asd = 1
    print('sale', id(price))
    
sale()
print('global',id(price))
# 서로 다른 것이다. 
# sale에서 가져와서 쓴거다.

# But!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
price = 1000
def sale():
    global price            #global을 통해서 본체를 가져올 수 있다.
    price = 500

sale()
print(price)        

i=0
def plus_1(n):
    result = n + 1
    print(id(result))

while i<10:
    temp = 3
    print(id(plus_1(temp)))
    i += 1

for i in range(5):
    temp = 5
    print(id(plus_1(temp)))
    
while i<10:
    temp = 3
    print(id(plus_1(temp)))
    i += 1
    
for i in range(5):
    temp = 5
    print(id(plus_1(temp)))