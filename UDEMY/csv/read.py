# NO HACER ESTO
# with open("fighters.csv") as file:
#data = file.read()

from csv import reader
from csv import DictReader


# with open("UDEMY/csv/fighters.csv") as file:
#   csv_reader = reader(file)
#     print(f"{fighter[0]} is from {fighter[1]}")
# Cada renglon es una lista
# print(row)

with open("UDEMY/csv/fighters.csv") as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        print(row["Name"])
