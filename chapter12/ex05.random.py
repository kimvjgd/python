import random

def main():
    for i in range(5):
        print(random.random())
    print()
    for i in range(5):
        print(random.randint(1,10))         # 정수 난수 (end 포함)
    print()
    for i in range(5):
        print(random.randrange(1,10))       # 정수 난수 (end미포함)
    print()
    for i in range(5):
        print(random.uniform(1,10))         # 실수 난수 (end미포함)
    
    print()
    print()
    food1 = ('asd','asd','asdas')           # 튜플을 넣어도 된다.
    food = ['짜장면','짬뽕','탕수육','군만두']
    print(random.choice(food))
    
    i = random.randrange(len(food))
    print(food[i])
    random.shuffle(food)
    print(food)
    
    # sample            기본적으로 choice 인데 갯수를 지정해서 여러개 뽑을 수 있다.
    food = ['짜장면','짬뽕','탕수육','군만두']
    print(random.sample(food, 2))
    
    nums = random.sample(range(1, 46), 6)
    nums.sort()
    print(nums)
    
main()