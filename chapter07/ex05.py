def calscore(name, *score, **option):
    print(name)
    total = 0
    for s in score:
        total += s
    print(total)
    if(option['avg']==True):
        print(total/len(score))
    print('\n\n\n')
    
def main():
    calscore("홍길동", 88, 99, 77, avg=True)
    calscore("홍길동", 88, 99, 77, 90, 30, 40, avg=False)

main()