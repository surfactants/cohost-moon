from datetime import datetime
import time


def log(string: str):
    date = datetime.fromtimestamp(time.time())
    date.replace(second=0, microsecond=0)
    string = date.strftime('%Y-%m-%d %H:%M ') + string + '\n'
    open('log.txt', 'a').write(string)
