# Homework 2 Question 8
#
# Write a new function to print a ‘cashier receipt’ output for a shop
# (any shop – clothes, food, events etc.).
# It should accept 3 items, then sum them up and print out a detailed receipt with TOTAL.


import random


def random_stuff():
	stuff = ("Brunstarr", "Kristianne", "Idalinnea", "Sissil", "Rödask", "Hedsäv",
         "Leikny", "Tilltalande", "Hallvi", "Sanela", "Malm", "Nordli", "Flekke",
         "Friheten", "Vimle", "Vallentuna", "Ektorp", "Vinliden", "Söderhamn",
         "Ekenäset", "Kivik", "Askeby", "Holmsund", "Alex", "Linnmon", "Dvala",
         "Lönset", "Rosenskärm", "Rumsmalva", "Skogslök", "Lyktfibbla", "Turill",
         "Sarakajsa", "Oddhild", "Bernhardina", "Ingunn", "Evali", "Vallkrassing",
         "Moalie", "Pedersborg", "Resenstad", "Ugilt", "Kattrup", "Törslev",
         "Vistoft", "Råvaror", "Tannisby", "Vadheim", "Idanäs", "Hauga", "Hafslo",
         "Vadsö", "Hokkåsen", "Vatneström", "Tussöy", "Hyllis", "Dröna", "Lekman",
         "Gopån", "Rejsa", "Rissla", "Kuggis", "Pallra", "Hyvens", "Manick", "Flysta")
	return random.choice(stuff)

def shop():
    shopping_basket = []
    no_of_rounds = int(input("How many items do you want to buy? "))
    for rounds in range(no_of_rounds):
        print("There's a sale on at IKEA!")
        stuff_1 = random_stuff()
        stuff_2 = random_stuff()
        stuff_3 = random_stuff()
        print("You see the following stuff to buy:")
        print("Item 1: {}".format(stuff_1))
        print("Item 2: {}".format(stuff_2))
        print("Item 3: {}".format(stuff_3))
        choice = input(
            "Which would you like to choose? (Pick: 1, 2, or 3) ")
        if choice == "1":
            print("{}, good choice! \n".format(stuff_1))
            shopping_basket.append(stuff_1)
        elif choice == "2":
            print("{}, excellent! \n".format(stuff_2))
            shopping_basket.append(stuff_2)
        elif choice == "3":
            print("{}, okay, sure! \n".format(stuff_3))
            shopping_basket.append(stuff_3)
    return shopping_basket

items = shop()
total = 0

print("IKEA RECEIPT".center(20, " "))
for item in items:
    price = random.randint(1, 350)
    print(item.ljust(20, "."), price)
    total += price

print("TOTAL".ljust(20, " "), total)
print("THANK YOU FOR SHOPPING!".center(20, " "))

