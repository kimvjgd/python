def main():

    # print([n for n in range(1,10)])

    # nums = [n*2 for n in range(1,11)]
    # for i in nums:
    #     print(i, end=', ')
        
    # print()


    # # list comprehension 안쓰면
    # nums = []
    
    # for n in range(1,11):
    #     nums.append(n*2)
        
    # print(nums)



    # print([n for n in range(1, 11) if n % 3 == 0])
    
    
    # print([n for n in range(1,101) if n % 2 == 0])

    odd_num_list = [n for n in range(1,101) if n % 2 == 1]
    even_num_list = [n for n in range(1,101) if n % 2 == 0]
    
    print('odd num list',odd_num_list)
    print('even num list',even_num_list)

main()