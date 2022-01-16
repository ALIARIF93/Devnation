# Assignment 2 Q2
def draw_flag():
    flag_height = int(input("How long is your flag?"))
    flag_width = int(input("How wide is your flag?"))
    flagpole_height = int(input("How long is your flagpole?"))
    flagpole_width = int(input("How wide is your flagpole?"))

    for x in range(flag_height):
        for y in range(flag_width):
            print("*", end="")
        print("\r")
    for i in range(flagpole_height):
        for j in range(flagpole_width):
            print("*", end="")
        print("\r")


draw_flag()
