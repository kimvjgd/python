# 1번 ##################################
# while을 이용하여 list에서 2 를 모두 없애보시오.

list_test_1 = [1,2,3,1,2,3]
value = 2

while value in list_test_1:
    print(value)
    list_test_1.remove(value)
    
print('1번 : ',list_test_1)


# 2번 ##################################
# 리스트 내포를 이용하여 1번의 결과를 array_2에 담으시오
list_test_2 = [1,2,3,1,2,3]

array_2 = [i for i  in list_test_2 if i != 2]
print('2번 : ',array_2)


# 3번 ##################################
# 리스트 내포를 이용하여 구구단 7단의 결과값을 array_3 list에 담으시오. ex) array_3 = [7, 14, 21, 28, 35, 42, 49, 56, 63]
array_3 = [(i+1) * 7 for i in range(9)]
print(array_3)


# 4번 ##################################
# 1-2-3-4-5-6-7-8- ...... 97-98-99-100 을 리스트 내포와 join을 사용하여 만들어보시오.

array = [str(i) for i in range(1, 100+1)]
print("-".join(array))

# 5번 ##################################
# 튜플을 이용하여 a=10, b=20 의 값을 서로 바꿔 a=20, b=10으로 만드시오
a, b =10, 20
print(a,b)
a, b= b, a
print(a,b)


# 6번 ##################################
# power 함수를 이용하면 1-5의 제곱수를 리스트에 담으시오  (map을 이용하시오.)

def power(item):
    return item * item

list_input_6 = list(range(1,6))
output_a = map(power, list_input_6)
print(list(output_a))           # map -> list





# 7번 ##################################
# filter 함수를 이용해서 1-10 리스트에서 짝수만을 골라내시오


def even_func(item):
    return item%2==0
list_input_7 = list(range(1,11))
output_b = filter(even_func, list_input_7)
print(even_func, list(output_b))


# 8번 ##################################
# 6번을 람다식을 이용하여 간단하게 구현하라



list_input_8 = list(range(1,6))
output_8 = map(lambda x : x * x, list_input_8)
print(list(output_8))