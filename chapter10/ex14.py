import time
def gettime():
    now = time.localtime()


    return now.tm_hour, now.tm_min          # 2개의 값을 return 하는게 아니라 tuple 하나를 return 한거다!!!!!!!!!!!!!!!

def main():
    result = gettime()
    print('result {}'.format(result))
    print(f"{result[0]}시 {result[1]}분" )

    hour, minute = gettime()
    print("%d시 %d분" %(hour, minute))

main()