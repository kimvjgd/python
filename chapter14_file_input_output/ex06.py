# w모드는 파일의 시작부터 시작
# a모드는 파일의 끝부터 시작

f = open('live.txt', 'at', encoding='utf-8')
f.write('\n\n서시... 윤동주')
f.close()