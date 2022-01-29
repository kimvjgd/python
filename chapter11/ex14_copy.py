# 정수 데이터와 리스트 데이터를 다르게 관리하고 있다.
# 파이썬이 메모리를 어떻게 관리하고 있는가?
# 변수 : 데이터를 저장하는 메모리 공간에 대한 이름
# 컴퓨터는 이진수만 저장할 수 있다. => 숫자가 아닌 정보는 숫자로 표현해서 저장

# 문자 코드 넘버링 하듯이 공간에 넘버링을 했다
# 공간을 구분 -> memory address !!!!!!!!!!!!!!!!!!

# CPU와 memory( ex)2^32 )사이 전선 다발을   -Address Bus라고 한다.
# 컴퓨터에 따라서 32bit, 64bit              - Data bus
# Read Write Wait 하고 할꺼냐 결정          - Control bus
# 그런 Bus들을 System Bus라고 한다.



a = 10
b = a
print(a, b)

a = 20
print(a, b)


print('\n\n')
list1 = [1,2,3]
list2 = list1               # 참조의 복사

print(list1 == list2)

list2[1] = 100

print(list1)
print(list2)

print(list1 == list2)



# a 의 address가 주소100에 10을 저장
# b 의 address가 주소104에 20을 저장

# list는 그떄 그떄 필요한 메모리 크기가 다르다.
# 변수는 메모리 잡은 곳에 넣었지만
# 리스트는 실제 데이터가 있는 주소값을 list1에 저장한다. 
# 그 주소값을 참조(Reference)라고 부른다.

# 일반 변수 : 값 자체를 저장
# 참조 변수 : 값이 있는 메모리 주소를 저장

print('\n')
list1 = [1,2,3,4,5]
list2 = list1.copy()
print(id(list1))
print(id(list2))
print(list1 == list2)

list2[1] = 100
print(list1)
print(list2)

print(list1 == list2)


