import random as ran

diceSize = int(input("what dice do you want to roll?[4/6/8/10/12/20/100]"))

if( diceSize != 4 or 6 or 8 or 10 or 12 or 20 or 100):
    diceSize = int(input("what dice do you want to roll?[4/6/8/10/12/20/100]"))

print(ran.randrange(diceSize) + 1)