import random
print("Today's Lottery Numbers are as follows \n");
for x in range(1, 7):
    x = random.randint(1,49);
    print("\t" ,x,);
