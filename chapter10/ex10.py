def main():
    score = [88, 95,100,20,67,100,23]

    score.sort(reverse=False)
    print(score)

    print('최대 값은 %d'%(score[0]))
    print('최소 값은 %d'%score[-1])

    score.reverse()
    print(score)
    score = [88, 95,100,20,67,100,23]
main()