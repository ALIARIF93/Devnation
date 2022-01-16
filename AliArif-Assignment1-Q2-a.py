num = input("Input a * triangle height in steps (for ex. 5):")

num = int(num)

i = 1

while(i <= num):

    for x in range(0, i):

        print("*", end=" ")

    print("")

    i = i+1