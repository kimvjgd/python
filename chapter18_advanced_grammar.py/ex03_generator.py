# 제너레이터
# 객체로 순회가능한 객체를 만드는 것이 귀찮은 작업이다. -> __iter__() & __next__() 둘다 만드는 것 귀찮다.

# 값을 생성해주는 데이터 생성기이다.
# 함수에서 데이터를 연속해서 리턴(yield)
# yield->리턴하는 행위는 같으나 함수의 실행 내역이 유지가 된다.(함수가 아직 안끝나고 값만 리턴해준다.) -> 다음에 또 함수실행하면 yield다음부터 재개가 된다.



def seqgen(data):
    for index in range(0, len(data), 2):
        yield data[index:index+2]                           # yield는 함수를 종료시키지않고 그냥 ㄲㄲ

solarterm = seqgen("입춘우수경칩춘분청명곡우입하소만망종하지소서대서")
# 함수가 실행되는 것이 아님.
# Generator 객체가 만들어지게 됨 (함수에서 yield라는 키워드가 있을때 이런 메카니즘이 일어난다.) 

print(solarterm)                    #-> generator
print(dir(solarterm))

for k in solarterm:
    print(k, end= ',')
    
    
    