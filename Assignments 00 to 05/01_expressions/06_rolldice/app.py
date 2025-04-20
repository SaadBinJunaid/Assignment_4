import random

dice_sides = 6

die1 = random.randint(1, dice_sides)
die2 = random.randint(1, dice_sides)

total_sum_of_dics = die1 + die2
print("Dice have", dice_sides, "sides each.")
print("First die:", die1)
print("Second die:", die2)
print("Total of two dice:", total_sum_of_dics)