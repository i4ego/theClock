import time as cat
import time_modern, date_modern
from os import system



while 1:
    system("cls")
    line_length = int()
    for line in time_modern.getTime():
        line_length = len(line)
        print(line)
    print("_"*line_length)

    line_length = int()
    for line in date_modern.getDate():
        line_length = len(line)
        print(line)
    print("_"*line_length)
    cat.sleep(2)