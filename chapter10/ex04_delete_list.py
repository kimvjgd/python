score = [88, 96, 57,100,46,764,42,100,1,2,3,4,5,6]

score.remove(100)           # 첫번째 것만 삭제해준다.
print(score)

del(score[2])
print(score)

score[1:4] = []
print(score)





# append 하고 pop을 많이 쓴다!!!!!!!!!   --> stack으로 마지막에 넣고 마지막에서 꺼낸다. LIFO - last in first out 마지막에 들어온것이 처음으로 나간다.
print(score.pop())          # 삭제된 element가 리턴된다.
print(score.pop(2))
print(score)

