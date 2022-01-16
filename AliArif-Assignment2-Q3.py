# Assignment 2 Q3
import random
num = int(input("How many times do you want to roll a dice?: "))
# setting the first dice to 0 initially.
dice1 = 0
# setting the second dice to 0 initially.
dice2 = 0
# Counting the number when dice sum was 7
is_sum_7 = 0
for x in range(1, num+1):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("dice roll", x, "sum: ", dice1+dice2)
    print("(", dice1, ",", dice2, ")")
    if(dice1+dice2 == 7):
        is_sum_7 = is_sum_7+1
print("You rolled lucky 7 ", is_sum_7, "times")
