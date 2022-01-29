class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def intro(self):
        print(str(self.age) + "살" + self.name + "입니다.")
        
        
    def __str__(self):              # 자신을 문자열로 표현하라
        return f'<Human name={self.name}, age={self.age}>'

def main():
    kim = Human("김상형", 29)         # __init__() 호출
    kim.intro()

    lee = Human("이승우", 45)         # __init__() 호출
    lee.intro()

    print(kim.name, kim.age)
    print(lee.name, lee.age)
    
    print(kim)                      # __str__ 이럴때 호출된다.      kim.__str__()
    print(lee)                      # lee.__str__()


main()