from pygame import mixer
import sys
import eyed3
import os
from file_util import get_file_list

DIR_PATH = "/Users/kimdonghyun/Documents/test/music"
song_list = []
song = None
current_index = -1

# 메뉴
# 목록 재생 정지 이전 다음 종료

def print_tag(file_path):
    try:
        s = eyed3.load(file_path)
        print (f'가수: {s.tag.artist}')
        print (f'앨범: {s.tag.album}')
        print (f'곡명: {s.tag.title}')
    except:
        pass

def init():
    global song_list
    mixer.init()
    song_list = get_file_list(DIR_PATH, '.mp3')
    print(song_list)

# 목록 보여주기
def print_list():
    for ix, title in enumerate(song_list):
        print(f'{ix}] {title}')
    print('\n')

def play():
    # 선곡 : 2
    global current_index, song                  # 전역변수 쫌 잘 기억하자.... 혼자했으면 또 까먹고 지나갈 뻔 했다.
    current_index = int(input('선곡 : '))
    
    # 이전에 재생 중이면 먼저 정지
    play_music(current_index)

def play_music(index):
    global song
    
    if song:                    # 0, false, none,아니면 다 True
        song.stop()
    
    song_path = os.path.join(DIR_PATH, song_list[index])
    print_tag(song_path)
    print(f'곡명 : {song_list[index]}')
    song = mixer.Sound(song_path)           # mixer 모듈 안에 정의된 Sound 클래스의 인스턴스를 생성
    song.play()





def stop():
    global song
    if song:
        song.stop()
        print()
    song = None
    
    
def play_prev():
    global song, current_index
    current_index -= 1
    
    if current_index == -1:
        current_index = len(song_list)-1

    # current_index = (current_index+1) % len(song_list)
    play_music(current_index)
    

def play_next():
    global song, current_index
    current_index += 1
    
    if current_index == len(song_list):
        current_index = 0

    # current_index = (current_index+1) % len(song_list)
    
    play_music(current_index)

    

def exit():
    sys.exit(0)

def print_menu():
    print('='*45)
    print("목록 || 재생 || 정지 || 이전 || 다음 || 종료")
    print('='*45)

def main():
    init()
    while True:
        print_menu()
        select = input("메뉴를 입력하세요  > ")
        if select == "목록":
            print_list()
        elif select == "재생":
            play()
        elif select == "정지":
            stop()
        elif select == "이전":
            play_prev()
        elif select == "다음":
            play_next()
        elif select == "종료":
            exit()
        else:
            print('잘못된 명령입니다.')

    # song1 = mixer.Sound(song_path1)
    # song1.play()
    # input('정리하려면 엔터')
    # song1.stop()

    
main()