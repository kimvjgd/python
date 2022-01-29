def calstep(begin, end ,step):
    total = 0
    for num in range(begin, end + 1, step):
        total += num
    return total

print(calstep(3,5,1))
print(calstep(begin=3, end=5, step=1))
print(calstep(step = 1, end = 5, begin=3))
print(calstep(3,5,step=1))
