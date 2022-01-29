# 파일 관리함수

# shutil.copy(a, b)
# shutil.move(a, b)
# shutil.rmtree(path)
# shutil.chown(f, u, g)

# os.rename(a, b)
# os.remove(f)
# os.chmod(f, m)
# os.link(a, b)
# os.symlink(a, b)

# os.chdir(d)   -working directory
# os.mkdir(d)
# os.rmdir(d)
# os.getcwd()

# os.listdir(d) 디렉토리 경로를 리턴해달라
# glob.glob(pattern)

# os.path.isabs(f)   - 절대 경로냐?
# os.path.abspath(f)    - 상대경로를 절대 경로로 바꿔달라
# os.path.realpath(f)
# os.path.exists(f) 
# os.path.isfile(f) 
# os.path.isdir(f)  


import os
# files = os.listdir('/Users/kimdonghyun/Documents/test/music')
# for f in files:
#     if f.endswith('mp3'):
#     # if f.split('.')[-1]=='mp3':
#         print(f)

# 위의 방법보다 이것이 훨씬 낫다. 

def get_file_list(dir_paht, ext):
    files = os.listdir(dir_paht)
    files = list(filter(lambda name: name.endswith(ext), files))
    return files

def main():
    DIR_PATH = '/Users/kimdonghyun/Documents/test/music'
    songs = get_file_list(DIR_PATH, 'mp3')
    # os.path.getsize(파일경로)  파일의 크기로 return 해준다.
    for f in songs:
        # print(f)                        # 파일명으로 출력
        print(os.path.join(DIR_PATH, f))# 절대경로로 출력


main()

        
# Permitted Error 뜨면        

# To access folder and files.

# Go to system preferences
# go to security and privacy.
# In the privacy tab, select the files and folders in the left dialog. Unlock the make changes and select the terminal.

# 시스템 환경설정 들어가서
# 보완 및 개인 정보보호 들어가고
# 개인 정보 보호탭에서
# 전체 디스크 접근 권한 안의
# visual studio code 체크해주면 된다