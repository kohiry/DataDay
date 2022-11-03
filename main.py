from time import perf_counter, localtime, strftime
import datetime
from os import system, name


end_word = ""

# clear console system('cls' if name == 'nt' else 'clear')

class EndIter(Exception):
    pass

def save_data(data):
    with open("Information.txt", mode="a", encoding="utf-8-sig") as f:
        f.write(data + '\n')

def Restart(text, first, second):
    print(text)
    while True:
        check = input(f"1 - {first}; 2 - {second}\n")
        if "1" in check:
            print("Ok.")
            break
        elif "2" in check:
            raise EndIter("Don't like note")
        else:
            print('Error, try again')





while True:
    try:
        end_word = input("'1' - start writing; '2' - end script;  '3' - open graphics;\n")
        if '3' in end_word:
            system('graphics.py')
        if '2' in end_word:
            break
        elif "1" in end_word:
            name_task = input("input name your task\n")
            Restart("You Shure?", "yes", "no")
            timer_start = int(perf_counter()) # таймер
            time_start = strftime("%H:%M:%S", localtime()) # время
            input('Timer started. For stop press Enter')
            print('Ok.')
            Restart("_______________", "Save", "Delete")
            timer_end = int(perf_counter())
            time_end = strftime("%H:%M:%S", localtime()) # время
            save_data("Date=" + str(datetime.date.today()) + ";" + "timer=" +\
                       str(timer_end - timer_start) + ";" + "time_start=" +\
                       time_start + ";" + "time_end=" + time_end +\
                        ";" + "name=" + name_task + ";")
            print("Data Saved.")
        else:
            print("Data incorrect. Try again!")
        system('cls' if name == 'nt' else 'clear')
    except EndIter:
        print('Ok. Restart.')
        system('cls' if name == 'nt' else 'clear')

# with open('text.txt', 'w'):
#     pass
