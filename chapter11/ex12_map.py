def total(s, b):
    return s + b


def main():
    score = [45, 89, 72, 53, 94]
    bonus = [2,3,0,0,5]
    for s in map(total, score, bonus):
        print(s, end=', ')



main()