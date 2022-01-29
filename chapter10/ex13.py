def main():
    names = '이순신','김유신','강감찬'
    name_list = ['이순신','김유신','강감찬']
    lee, kim, kang = names                      # unpack - 튜플도 되고
    lee, kim, kang = name_list                  # unpack - 리스트도 된다.

    print(lee)
    print(kim)
    print(kang)
    print(names)

    a, b = 12, 34
    print(a, b)
    a, b = b, a
    print(a, b)
main()