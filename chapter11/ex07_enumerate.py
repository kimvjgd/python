race = ['저그', '테란', '프로토스']

print(list(enumerate(race)))

score = [88, 96, 69, 100, 99]

for no, s in enumerate(score,1):                # 부터 배정 -> ,1은 1부터 배정
    print(str(no) + "번 학생의 성적 : " , s)