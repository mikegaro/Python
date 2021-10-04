with open("historia.txt", "a") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.close()

file = open("historia.txt")
print(file.read())
