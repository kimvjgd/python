from time_util import get_elapse_time

def work1():
    for a in range(1000):
        print(a)

def work2():
    sum = 0
    for i in range(1, 100001):
        sum+=i


def main():
    get_elapse_time(work1)
    # 1~ 1000까지의 합을 구하는데 걸리는 시간
    # 시간을 출력하세요.

    get_elapse_time(work2)

main()