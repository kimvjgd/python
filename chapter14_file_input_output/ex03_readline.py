f = open("live.txt", 'rt', encoding='utf-8')
text = ""
line = 1
while True:
    row = f.readline()          # 파일의 끝까지 읽으면 None을 return 한다.
    if not row: break
    if row == '\n': continue
    text += str(line) + " : " + row
    line += 1
    
f.close()
print(text)


# ㄴㅇㅁㄴㅇㅁㄴ\n두번째 문장....\n
# file pointer가 os가 알아서 보고 시작하고 \n에서 끝내고 다음 filepointer 설정
# 파일의 아예 끝은 EOF - End of File 얘를 만났을때 none을 return 한다
