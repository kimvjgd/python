s = "korea" + str(2000)

print(s)
print(type(s))

print(bool(0))

print(10 + float("22.5"))

print(int("1a", 16))                # 16진수로
print(int("15", 8))                 # 8진수로

# print(int("10.0"))                # 에러뜬다. 
print(int(10.5))                    # 이건 가능하지
print(int(float("10.0")))           # 아니면 float로 바꾸고 int로 바꾸던가
