# def calcstep(begin, end, step):
#     total = 0
#     for num in range(begin, end + 1, step):
#         total += num
#     return total

# print(calcstep(3, 5, 1))
# print(calcstep(step=2, end = 5, begin = 1))


# 꼭 눈에 익혀두자.
def calcstep(**args):
    begin = args['begin']
    end = args['end']
    step = args.get('step',1)         # args['step'] 없으면 1
    total = 0
    for num in range(begin, end + 1, step):
        total += num
    return total

print(calcstep(step=2, end=5, begin=1, asdasnfuiaeihfwe='adsabdahs'))   # 다른 인자는 그냥 dict으로 들어가는 것 뿐 ㅋㅋ
print(calcstep(end=5, begin=1, asdasnfuiaeihfwe='adsabdahs'))


