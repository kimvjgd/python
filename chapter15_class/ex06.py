# 온도 센서(온도계)
#   클래스명: Temperature
#     데이터: 온도(value), 기록(온도, 측정시간), 위치, 측정가능 범위
#       기능: 측정하기, 범위 초과시...,  
import random
from datetime import datetime
import time


class Temperature:
    def __init__(self, location, min_value, max_value) -> None:
        self.value = None
        self.records = []
        self.location = location
        self.min_value = min_value
        self.max_value = max_value
        
    def measure(self):
        # min_value, max_value 사이의 랜덤한 값으로 측정되게...
        # 값은 소수점 둘째자리까지...
        self.value = round(random.uniform(self.min_value, self.max_value), 2)
        now = datetime.now()
        
        self.records.append((now, self.value))
        return now, self.value
    
# 히터
#   클래스: Heater
#       데이터: 온도, 장소, 운영 기준 온도
#       동작/기능: 켜기, 끄기, 운영, 온도 설정
class Heater():
    def __init__(self, location) -> None:
        self.temp = Temperature(location, -5, 35)
        self.location = location
        self.std_temp = 19
        self.status = False
    
    def turn_on(self):
        self.status = True
        print(f'{self.temp.value}도가 되어 히터를 켭니다')
    
    def turn_off(self):
        self.status = False
        print(f'{self.temp.value}도가 되어 히터를 끕니다')
        
    def run(self):
        # 온도를 측정해서, 기준 온도 이하이면 보일러 켜기, 기준온도 이상이면 보일러끄기
        now, temp = self.temp.measure()
        if temp <= self.std_temp and self.status == False:
            self.turn_on()
        elif temp > self.std_temp and self.status == True:
            self.turn_off()
        else:
            pass
    
    def set_std_temp(self, temp):
        self.std_temp = temp
        
        
        
        
def main():
    # 1초 간격으로 온도를 측정해서
    # 장소, 측정시간, 온도를 출력하세요.
    heater = Heater('안방')
    heater.set_std_temp(15)
    while True:
        time.sleep(1)
        heater.run()

main()