steps = 3
pattern = "10"
num_sp = 0


for i in range(steps, -1, -1):
    print(num_sp * " " + pattern * i + "1")
    num_sp = num_sp+1
