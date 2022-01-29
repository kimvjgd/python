score = [88,95,60,100,99]

score.append(50)

print('큐', score)
print('큐', score.pop(0))               # 넣은 데이터 놔두고 처음 데이터를 없애준다.
print('큐', score)

score = [88,95,60,100,99]

score.append(50)
print('스택', score)
print('스택', score.pop())              # 맨뒤에서 넣은 값을 꺼냄
print('스택', score)

