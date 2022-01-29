def main():
    scores = [70, 30, -10, 100, 150, 90]
    
    # 음수 또는 100초과 데이터를 제외한 합계를 구하세요
    # comprehension을 이용해서...
    
    scores = [n for n in scores if 0<=n and n<=100]
    print(sum(scores))
    
main()