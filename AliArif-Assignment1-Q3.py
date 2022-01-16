
sum = 0
product = 1
num_count = 0
print("\r\r")
print("This program will take input integers from user until user press 'q' to stop entering integers.")
print("\r\r")
print("Please enter inputer Integers:", end="")
while 1:
    num = input()
    if num == 'q':
        break
    else:
        sum = sum+int(num)
        product = product*int(num)
        num_count = num_count+1

print("Average  of all no.s :", sum/num_count)
print("Product of all no.s:", product)
