print("Please enter for number: ")
num = int(input())

result = num
if (num > 0):
    i = num-1
    while(i > 0):
        result = result*i
        i = i-1
    print("Factorial result: ", result)
elif (num < 0):

    i = num+1
    while(i < 0):
        result = -1 * (result*i)
        i = i+1
    print("Factorial result: ", result)

else:
    result = 1
    print("Factorial result: ", result)
