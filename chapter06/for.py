# sum = 0
# start = int(input('시작 > '))
# end = int(input('끝 > '))

# for i in range(start, end+1):
#     sum += i
    
# print(sum)


# for a in range(0,5):
#     print(a+1)

# for x in range(1, 51):
#     if (x % 10) == 0:
#         print('+', end='')
#     else:
#         print('-',end='')

#평균구하기
# scores = [34, 78, 90, 35, 100]

# sum = 0


# for score in scores:
#     sum += score

# average = sum / len(scores)
# print(round(average, 2))
# print(min(scores))
# print(max(scores))


# names = ['홍길동', '고길동', '둘리', '뚜치']
# search_result = False
# order = 0

# # 리스트에 이름이 있는지 확인하시오

# input_name = input('이름을 입력하시오 : ')

# for name in names:
#     if(name == input_name):
#         search_result = True
#         break;
#     else:
#         pass
#     order+=1
    
    
# if search_result==True:
#     print('{}번째 존재'.format(order+1))
# else:
#     print('존재 x')

# score = [92, 86, 68, -1, 56]
# for s in score:
#     if s == -1:
#         continue
#     print(s)
# print('성적처리끝')


# scores = [92, 86, 68, -1, 67, -30, 90, 140, 90]
# sum = 0
# count = 0

# for score in scores:
#     if score <0 or score > 100:
#         continue
#     sum += score
#     count += 1

# print(round(sum / count,2))

# 구구단 출력
# dan = int(input('구구단 몇 단 ? > '))
# for i in range(1,10):
#     print(dan,'x',i,'=',dan*i)

# for i in range(2,10):
#     for j in range(1,10):
#         print(i,'x',j,'=',i*j)

# for i in range(1, 9):
#     print('*'*i)

# for i in range(9,0,-1):
#     print('*'*i)
    
# for i in range(9, 0, -1):
#     for j in range(i):
#         print('*', end='')
#     print()

# for i in range(1,10):
#     print('*'*i)
    
# for i in range(1, 10):
#     for j in range(i):
#         print('*', end='')
#     print()
