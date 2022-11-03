from os import system, name


class Data:
    def __init__(self):
        self.text = list()
        self.text_elem_dict = dict()
        text = ''
        with open("Information.txt", "r", encoding="utf-8-sig") as f:
            text = list(f.readlines())

        for line in text:
            for elem in line.split(";"):
                if elem[0] != '\n':
                    self.text_elem_dict[elem.split("=")[0]] = elem.split("=")[1]
            self.text.append(self.text_elem_dict.copy())
            self.text_elem_dict = dict()

    def return_data(self):
        return self.text

    def date_set(self):
        date_inf = []
        for elem in self.text:
            date_inf.append(elem["Date"])
        date_inf = list(set(date_inf))
        date_inf.sort()
        return date_inf

    def __str__(self):
        return str(self.text)



my_text = Data()
format_text = my_text.return_data()
counter = 0
for i in my_text.date_set():
    print(f"____________{i}____________")
    for elem in format_text:
        if elem["Date"] == i:
            hours = int(elem["timer"]) // 60 // 60
            minutes = str(int(elem["timer"]) // 60)
            counter = int(elem["time_start"].split(":")[0])
            if hours == 0:
                print(counter * "-" + "1" + (24 - counter - hours) * "-", " -- " + elem['name'],  minutes + "=minutes")
            else:
                print(counter * "-" + hours * "1" + (24 - counter - hours) * "-", " -- " + elem['name'],  minutes + "=minutes")
    counter = 0
print(f"____________End Script____________")
input("For stop press Enter")
system('cls' if name == 'nt' else 'clear')
