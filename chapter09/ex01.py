def calc_sum(scores):
    total = 0
    for s in scores:
        total += s
    return total


def print_score(subject, scores):
    total = calc_sum(scores)
    print(f'{subject}총점: {total}')
    # print(f'국어평균: {total/len(kor_score):.2f}')
    average = total/len(scores)
    print(f"{subject}평균 : {average:.2f}")

def main():
    eng_score = [88, 84, 59, 25, 100, 26]
    kor_score = [12, 100, 98, 89, 100, 92]
    
    print_score('영어', eng_score)
    print_score('국어', kor_score)
    

main()