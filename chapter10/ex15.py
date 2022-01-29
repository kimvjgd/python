def main():
    scores = [
        ('a',100),
        ('b',20),
        ('c',30),
        ('d',40),
        ('e',50),
        ('f',100)
        ]
    
    for name, score in scores:
        print(f'학생명 : {name}, 성적 : {score}')
    
main()