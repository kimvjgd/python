from datetime import datetime
import time

def get_time_filename(ext, seq=1):
    now = datetime.now()

    file_name = f'{now.year}{now.month:02}{now.day:02}-{now.hour:02}{now.minute:02}{now.second}-{seq:03}.{ext}'
    return file_name

def get_elapse_time(func):
    start = time.time()
    func()
    end = time.time()

    print(end-start)