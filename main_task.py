from os import system, name
import graphics


my_data = graphics.Data()
text = my_data.return_data()
print(text)
input()
system("graphics.py")

system('cls' if name == 'nt' else 'clear')
