# 예외(Exception) -> 복구가 가능
# 에러(Error) -> 복구가 불가능


# try: 
#     #실행할 명령
#     pass
# except:
#     # 에러났을 때 실행되는 코드
#     pass
# else:
#     # 에러가 나지 않았을 때 추가적으로 실행
#     pass


# 예외
# str = '89점'
# try:
#     score = int(str)
#     print(score)
# except:
#     print('예외가 발생했습니다.')
    
# print('작업완료')


# while True:
#     str = input('점수를 입력하세요 : ')
#     try:
#         score = int(str)
#         print('입력한 점수 : ', score)
#         break
#     except:
#         print('점수 형식이 잘못되었습니다.')
# print('작업완료')


str = '89'


try:
    score = int(str)
    print('입력한 점수 : ', score)
    a = str[5]
except ValueError as e:
    print(e)
except IndexError as e:
    print(e)
    print('여기가 실행 뿜뿜뿜')
print('작업완료')

