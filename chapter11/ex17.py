def main():
    list0 = ['a', 'b']
    list1 = [list0, 1, 2]    # [['a', 'b'], 1, 2] 아.... list0의 참조값을 갖고 있는 거구나....  그러니 list0자체가 바뀌고 list2의[0] 성분이 변함에 따라 list1[0]도 바뀌는구나..
    list2 = list1.copy()

    list2[0][1] = 'c'
    list2[1] = 1000
    print(list1)
    print(list2)
    
    
    # 원본도 변한다.
    
main()