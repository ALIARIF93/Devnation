steps = int(input("Please enter any odd number:"))
num_sp = int(steps/2)
num_st = int(steps % 2)
increment_range = steps - int(steps/2)   # 7-3=4
decrement_range = steps - increment_range  # 7-4=3
for i in range(increment_range):
    print(num_sp * " " + num_st*"*")
    num_sp = num_sp-1
    num_st = num_st+2
# num_st = 5
num_sp = num_sp+2
num_st = num_st-4

for i in range(decrement_range):
    print(num_sp * " " + num_st*"*")
    num_sp = num_sp+1
    num_st = num_st-2
