import random

dice_sides = 6
def roll_dice1():
    dice1: int = random.randint(1,dice_sides)
    dice2: int = random.randint(1,dice_sides)
    total_die =  dice1 + dice2
    print(f"Total of two dice: {total_die}")

def roll_die2():
    die1: int = 10
    print("die1 in main() starts as: " + str(die1))
    roll_dice1()
    roll_dice1()
    print("die1 in main() ends as: " + str(die1))

    
if __name__ == '__main__':
    roll_die2()