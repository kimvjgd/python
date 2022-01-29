score = (1,2,3,4,5)
print(score)
print(type(score))

# 그냥 나열해도 tuple로 인식한다.
score = 88, 85, 49, 100, 99
print(score)
print(type(score))

# , 가 있으면 tuple 로 인식한다.
score = 88,
print(score)
print(type(score))

#
score =88
print(score)
print(type(score))

score = (88)                # 괄호 있어도 int로 인식된다 이떄는 (87+100) * 2 같은 느낌
print(score)
print(type(score))

tu = 1,2,3,4,5,6,7,8,9

print(tu[3])
print(tu[1:4])
print(tu + (6,7))       # 원본에는 변환가 없다.

# 수정과 삭제는 안된다.
# tu[1]= 100
# del tu[1]             

# tuple을 sort하고 싶으면 sort말고 sorted를 써야한다.
# sort는 원본이 변하고 sorted는 변하지 않는다.