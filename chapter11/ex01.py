dic1 = {
    'boy': '소년',
    'school':'학교',
    'book': '책',
}

print(dic1)



print(dic1['boy'])
print(dic1.get('boy','없는 단어입니다.'))            # get을 권장한다.
print(dic1.get('girl','없는 단어입니다.'))


if 'school' in dic1:
    print(dic1['school'])
else:
    print('사전에 없는 단어입니다.')
    
del dic1['book']            # 삭제된다.
print(dic1.keys())
print(list(dic1))                # keys값과 동일하다.
print(dic1.values())
print(dic1.items())

key_list = dic1.keys()
for key in key_list:
    print(key,' - ', dic1[key])

for key, value in dic1.items():
    print(key, ' & ',value)
    
dic2 = {
    'boy' : '소년1',             # 겹치면 그냥 덮어쓰여진다.
    'queen' : '여왕',
    'pass' : '통과하다',
    'Korea' : '한국',
}

dic1.update(dic2)
print(dic1)

