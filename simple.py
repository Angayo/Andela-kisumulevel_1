import random

print ("Choice ([34,56,89,12,5,7]:)", random.choice([34,56,89,12,5,7]))

print("\n Shuffle() Method");

items = [45,2,5,23,78,9];
random.shuffle(items)

print("Reshuffle the items: ",items);

#============Randint===================
# randint()method

for x in range(1 , 7):
    x = random.randint(1, 49)
    print("\t", x);


