# ** 기호로 지정하여 타입은 dictionary가 된다.
def calstep(**args):
    begin = args['begin']
    end = args['end']
    step = args['step']
    
    total = 0
    for num in range(begin, end+1, step):
        total += num
    return total
    
print(calstep(begin=3, end=5, step=1))

