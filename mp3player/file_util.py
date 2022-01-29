# pickle
# 파이썬 자료형 그대로 저장하고, 그대로 로드(복원)
# 반드시 binary 모드로 오픈해야 함
# 다른 언어와 호환성은 없음

# dump : 저장 (가공안하고 그 모양 그대로 더미로 )     pickle.dump(data, file)    data: 저장할 데이터 file: 'bw'로 오픈한 파일객체
# load : 로드                                 pickle.load(file)         file: 'br' 그대로 오픈한 파일 객체, data: 복원한 데이터

import pickle
import json         # binary 말고 text형태로 보내야 할때가 있다!!
import os

def save(file_name, data):
    try:
        with open(file_name, 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        print(e)

def load(file_name):
    try:
        with open(file_name, 'rb') as file:
            data = pickle.load(file)
            return data
    except Exception as e:
        print(e)



# pickle 대신에 json을 쓴다.    & b -> t         json 은 text이다
# json은 다른언어간에 호환성이 높다. 
def save_json(file_name, data):
    try:
        with open(file_name, 'wt') as file:
            json.dump(data, file)
    except Exception as e:
        print(e)

def load_json(file_name):
    try:
        with open(file_name, 'rt') as file:
            data = json.load(file)
            return data
    except Exception as e:
        print(e)

def get_file_list(dir_paht, ext):
    files = os.listdir(dir_paht)
    files = list(filter(lambda name: name.endswith(ext), files))
    return files





# if 다른 언어와의 호환성이 필요하면 json을 무조건 쓰고 
# python에서만 쓰고 데이터 노출이 싫으면 pickle을 사용해야한다.
