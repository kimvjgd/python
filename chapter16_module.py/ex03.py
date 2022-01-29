# 모듈 경로
# sys 모듈의 path 리스트를 먼저 조사
# 현재 워킹 디렉토리가 제일 먼저 조사됨
# 그다음 pythonpaht 환경 변수의 디렉토리 검색

import sys

for path in sys.path:
    print(path)
    
# 통칭해서 library라고
# 2022 / 01 / 14 오전수업
# bash폴더말고 zshrc 폴더들어가서 export PYTHONPATH="경로" 하고 저장 후 visual studio 켰다 끄면 된다.
