# s = "0123456789"

# print(s[2:5])
# print(s[3:])
# print(s[:4])
# print(s[:])         # 전부다


file = "20200101-104830.jpg"

# print("촬영 날짜" + file[4:6] + "월" + file[6:8] + "일")
# print("촬영 시간" + file[9:11] + "h" + file[11:13] + "m")
# print("확장자" + file[-3:])


# print(file[:4]+" y /"+file[4:6]+" m /"+file[6:8]+" d /")
# print(file[9:11]+" h /"+file[11:13]+" m /"+file[13:15]+" s /")
# print("file type " + file[-3:])


# 날짜형식의 파일명을 인자로 받고
# 날짜파트를 리턴해주는 함수
# 시간파트를 리턴해주는 함수

def get_date_str(info):
    return info[:4]+" y /"+info[4:6]+" m /"+info[6:8]+" d /"

def get_time_str(info):
    return info[9:11]+" h /"+info[11:13]+" m /"+info[13:15]+" s /"
def main():
    print(get_date_str(file), get_time_str(file), sep='\n')


main()