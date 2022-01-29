from datetime import datetime

def main():
    now = datetime.now()
    
    print(now)
    print("%d년 %d월 %d일" % (now.year, now.month, now.day))
    print("%d:%d:%d" % (now.hour, now.minute, now.second))
    
main()

