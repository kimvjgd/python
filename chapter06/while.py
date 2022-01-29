# num = 1;
# sum = 0;

# while num<101:
#     sum += num
#     num += 1


# print(sum)

# 홀수의 합과 짝수의 합을 따로 출력하라


# sum_odd = 0
# sum_even = 0
# i = 1
# while i <101:
#     if(i % 2 != 0) :
#         sum_odd += i
#     else:
#         sum_even += i
#     i += 1
# print("홀수의 합 : {}, 짝수의 합{}".format(sum_odd, sum_even))
# print('asdas')


# 입력 시작값 : 20 종료값 : 40
# 출력 20~40까지의 합 : xxxx
# start = int(input('시작값 > '))
# end = int(input('종료값 > '))
# sum = 0
# while start <= end:
#     sum += start
#     start += 1
# print(sum)


names = ['홍길동', '고길동', '둘리', '뚜치']

while True:
    search_name = input('검색 이름 : ')
    if search_name == 'exit':
        break
    
    search_result = False
    index = 0
    for name in names:
        if name == search_name:
            search_result = True
            break
        index += 1
    
    if search_result:
        print(search_name, '은', (index+1), '번째에 있습니다.')
    else:
        print(search_name, '은 목록에 없습니다.')
        
    

