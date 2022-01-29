# 가상환경(Virtual Environment)

# 파이썬에서는 한 라이브러리에 대해 하나의 버젼만 설치가 가능
# 여러개의 프로젝트를 진행하는 겨우
    # 프로젝트마다 동일 패키지에 대해 다른 라이브러리를 사용하는 경우 문제
# 이를 방지하기 위한 격리된 독립적인 가상환경을 제공
# 일반적으로 프로젝트마다 다른 하나의 가상환경을 생성한 후 작업을 시작


# 가상환경을 만드는 대표적인 모듈
# venv : python 3.3 버젼 이후부터 기본 모듈에 포함
# virtualenv : python2 버젼부터 사용(예전 것)
# conda         <- 우리가 쓰는것
# pyenv

# 가상환경 목록 보기
    # 터미널에 conda env list
    
# 가상환경 만들기
    # conda create --name <가상환경 이름> python=<파이썬 버젼>
    # conda create --name python-study python=3.9.7

# 활성화/ 비활성화
# conda activate python-study
# conda deactivate

# 가상환경 살제
# conda remove --name <가상환경 이름> --all
# conda remove --name python-study --all
# all option을 안주면 목록에서만 빠지는 것이다.


# f1  -> python: select interpreter
