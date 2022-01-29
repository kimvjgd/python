def main():
    ff1 = 12.3456
    print(f'f1의 값은 {ff1}입니다.')
    
    result1 = f'{ff1:.2f}'              # 소수점 2번째 자리에서 반올림
    print(result1)
    
    year = 2022
    month = 1
    day = 6
    
    # 작성일 : 2022-01-06
    
    print(f'작성일 ; {year}-{month:02}-{day:02}')

main()