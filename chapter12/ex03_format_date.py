from time_util import get_time_filename
import time

# 다음 함수를 정의하세요
# 함수명 : capture()
# 리턴값 : 20220110-130023.jpg (현재날짜-시간.jpg)

def capture(seq=1):
    file_name = get_time_filename('jpg', seq)
    return file_name

    
def main():
    for ix in range(5):
        file_name = capture(ix+1)
        print(file_name)
        time.sleep(1)

    while True:
        # 온도 측정
        time.sleep(10)
    
main()