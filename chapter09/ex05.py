def main():

    lol = [
        [1,2,3],
        [4,5],
        [6,7,8,8]
    ]

    # print(lol[0])
    # print(lol[2][2])
    print()
    print(lol)
    print()
    print()


    for sub in lol:
        for item in sub:
            print(item, end=' ')
        print()
    print()

main()