from time import perf_counter, localtime, strftime
import datetime
from os import system, name
from time import time


end_word = ""


def save_data(data):
    with open("Information.txt", mode="a", encoding="utf-8-sig") as f:
        f.write(data + '\n')

# status = False
#
with open("config.txt", mode="r+", encoding="utf-8-sig") as f:
    text_list = f.readlines()
    if len(text_list) > 0:
        text = text_list[0]
        if input("We found don't saved information. Save? 1 - yes; 2 - no\n") == '1':
            time_end = strftime("%H:%M:%S", localtime()) # время
            timer =  int(time() - float(text.split(";")[1].split("=")[1]))
            result = "Date=" + str(datetime.date.today()) + ";" + "timer=" +\
                    str(int(timer)) + ";" + "time_start=" +\
                    text.split(";")[2].split('=')[1] + ";" + "time_end=" + time_end +\
                     ";" + "name=" + text.split(";")[3].split("=")[1] + ";" +\
                     "Category=" + text.split(";")[4].split("=")[1] + ";"
            save_data(result)
    f.truncate(0)

# clear console system('cls' if name == 'nt' else 'clear')

class EndIter(Exception):
    pass

class EndIterEndSave(Exception):
    pass


def category_file():
    text = ''
    with open("category.txt", mode="r", encoding="utf-8-sig") as f:
        text = f.readlines()[0].split(';')
    return text[0: len(text)-1]


def clear_console():
    system('cls' if name == 'nt' else 'clear')

def Restart(text, first, second, status=False):
    print(text)
    while True:
        check = input(f"1 - {first}; 2 - {second}\n")
        if "1" in check:
            print("Ok.")
            if status:
                raise EndIterEndSave("End iter and save data users for another day")
            break
        elif "2" in check:
            if status:
                break
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
            print('chose your category:')
            choses_category = [str(i+1) for i in range(len(category_file()))]
            print("choose:", "\t".join(category_file()))
            category = input("input: " + "\t".join(choses_category) + "\n")
            if category not in choses_category:
                print("Incorrect category. Try again in another iteration.")
                raise EndIter
            else:
                name_task = input("input name your task\n")
                Restart("You Shure?", "yes", "no")
                timer_start = int(perf_counter()) # таймер
                time_start = strftime("%H:%M:%S", localtime()) # время
                Restart("Timer started. You want to close?", "Yes", "No", True)
                input('For stop press Enter')
                print('Ok.')
                Restart("_______________", "Save", "Delete")
                timer_end = int(perf_counter())
                time_end = strftime("%H:%M:%S", localtime()) # время
                save_data("Date=" + str(datetime.date.today()) + ";" + "timer=" +\
                           str(timer_end - timer_start) + ";" + "time_start=" +\
                           time_start + ";" + "time_end=" + time_end +\
                            ";" + "name=" + name_task + ";" +\
                            "Category=" + category_file()[int(category)-1] + ";")
                print("Data Saved.")
        else:
            print("Data incorrect. Try again!")
        clear_console()
    except EndIter:
        input('Ok. Restart. press Enter\n')
        clear_console()
    except EndIterEndSave:
        print('Ok. Restart.')
        clear_console()
        with open("config.txt", mode="w", encoding="utf-8-sig") as f:
            f.write("Date=" + str(datetime.date.today()) + ";" + "timer=" +\
                       str(time()) + ";" + "time_start=" +\
                       time_start + ";" + "name=" + name_task + ";" +\
                       "Category=" + category_file()[int(category)-1] + ";")
        break

# with open('text.txt', 'w'):
#     pass
