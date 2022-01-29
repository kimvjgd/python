# MP3Player
#   데이터: 노래 목록, song, BASE_FIR, current_index
#   기능: 목록, 재생, 다음, 이전, 종료  --> 메뉴 구성

from baseapp import Application
import eyed3
from file_util import get_file_list
import os
from pygame import mixer




class MP3Player(Application):
    def __init__(self) -> None:
        super().__init__("MP3Player")
        self.DIR_PATH = "/Users/kimdonghyun/Documents/test/music"
        self.song_list = []
        self.song = None
        self.current_index = -1

    
    
    # 멤버 초기화...
    
    # 메뉴 구성
    def create_menu(self):      # 얘가 Application create_menu 오버라이딩으로 덮는다
        self.menu.add_menu('목록',self.print_list)
        self.menu.add_menu('재생',self.play)
        self.menu.add_menu('정지',self.stop)    # 부모 클래스의 exit메서드
        self.menu.add_menu('다음',self.play_next)
        self.menu.add_menu('이전',self.play_prev)
        self.menu.add_menu('종료',self.exit)    # 부모 클래스의 exit메서드

    def print_tag(self, file_path):
        try:
            s = eyed3.load(file_path)
            print (f'가수: {s.tag.artist}')
            print (f'앨범: {s.tag.album}')
            print (f'곡명: {s.tag.title}')
        except:
            pass

    def init(self):
        super().init()      # 내부에서 create_menu() 호출

        mixer.init()
        self.song_list = get_file_list(self.DIR_PATH, '.mp3')
        print(self.song_list)


    def print_list(self):

        for ix, title in enumerate(self.song_list):
            print(f'{ix}] {title}')
        print('\n')
    
    def play(self):
        self.current_index = int(input('선곡 : '))
    
        # 이전에 재생 중이면 먼저 정지
        self.play_music(self.current_index)
        
    def play_music(self, index):
        
        # print(self.song)
        if self.song:                    # 0, false, none,아니면 다 True
            self.song.stop()
        print(self.DIR_PATH)
        print(self.song_list[index])
        song_path = os.path.join(self.DIR_PATH, self.song_list[index])
        self.print_tag(song_path)
        print(f'곡명 : {self.song_list[index]}')
        self.song = mixer.Sound(song_path)           # mixer 모듈 안에 정의된 Sound 클래스의 인스턴스를 생성
        self.song.play()

    def stop(self):
        if self.song:
            self.song.stop()
            print()
        self.song = None
        
    def play_next(self):
        self.current_index += 1
        
        if self.current_index == len(self.song_list):
            self.current_index = 0

        # current_index = (current_index+1) % len(song_list)
        
        self.play_music(self.current_index)

    def play_prev(self):
        self.current_index -= 1
    
        if self.current_index == -1:
            self.current_index = len(self.song_list)-1

        # current_index = (current_index+1) % len(song_list)
        self.play_music(self.current_index)
        

def main():
    app = MP3Player()
    app.run()


main()