def main():
    s = "Good morning, my love KIM(김동현123123). ok?"
    
    print(s.lower())
    print(s.upper())
    print(s.swapcase())
    print(s.capitalize())
    print(s.title())
    print(s)
    
    print(s[0])       # 읽는 것은 문제가 되지 않는다.
    # s[0]='a'        # 이건 오류난다. 바꿀꺼면 s를 통째로 바꿔야한다.
    # s = 'asd'
    s=s.lower()       # s자체를 바꾸고 그 값을 저장
    print(s)
    
    
    
main()


