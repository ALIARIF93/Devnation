# Assignment 2 Q1

num = input("Please enter the input number:")
result = int(num)
collatz_chain = [result]
while(result > 1):
    if (result % 2 == 1):
        result = result*3 + 1
    else:
        result = result/2
    collatz_chain.append(result)

print("collatz_chain:", collatz_chain)

print("collatz_length:", len(collatz_chain))
