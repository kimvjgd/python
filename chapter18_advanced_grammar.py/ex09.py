# Context Manager 객체
#   __enter__(self): with로 객체를 만들어서 as 에 배정할 때
#   __exit__(self, type, value, tb): with 코드 블럭을 벗어날 때 호출


# 파일 입출력할 때 
# ex)
# with file as f: 로 해서 f.close() 작업을 생략할 수 있었다.



class MyObject:
    def __init__(self) -> None:
        pass
    
    def __enter__(self):
        print('with 코드 블럭에 진입합니다.')
        print('초기화 작업 수행')
        return self                 # enter해서 값을 입력
    
    def __exit__(self, type, value, tb):            # 끝날때 실행된다.
        print('with 코드 블럭 벗어납니다.')
        print('클린업 정리 작업 수행')        
        
def main():
    with MyObject() as obj:         # enter해서 입력되는 객체가 obj가 된다.
        input('마치려면 enter')

    print('작업 완료')
    
main()