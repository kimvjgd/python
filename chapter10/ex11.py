def main():
    score = [88, 95,100,20,67,100,23]
    # score.sort(reverse=True)
    # print(score)


    country = ["South Korea","japan", "CHINA", 'united KingdoM', 'spain', "america"]

    # country.sort()
    # print(country)

    # country_lower = [con.lower() for con in country]
    # country_lower.sort()
    # print(country_lower)
    
    # country.sort(key=str.lower)       # lower()이 아니고 lower만 썼다. 함수 호출이 아니라 지정 나중에 쓸때 이거 쓰라고 말해주는 것
    # print(country)

    # 문자열의 길이가 긴 순으로 정렬하세요.
    country.sort(key=len, reverse=True)
    print(country)
    
    sorted_score = sorted(score, reverse=True)
    print(score)
    print(sorted_score)
    
    

main()