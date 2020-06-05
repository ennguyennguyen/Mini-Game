class my_dictionary(dict):
    def __init__(self):
        self = dict()

    def add(self, key, value):
        self[key] = value



import random

my_list = my_dictionary()
while True:
    my_list.key = input("Word: ")
    my_list.value = input("Definition: ")

    my_list.add(my_list.key, my_list.value)

    cont = input("Do you want to continue?(Y/N): ")

    if cont == "N" or cont == "n":
        break

print(my_list)
random_word = random.choice(my_list)
print("The word is ", random_word)

