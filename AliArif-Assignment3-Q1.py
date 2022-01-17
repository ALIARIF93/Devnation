def ascii_sum(input_str):
    total_sum = 0
    for x in range(len(input_str)):
        total_sum += ord(input_str[x])
    print("Total ASCII Sum: ", total_sum)


def ascii_sum_odd(input_str):
    total_sum_odd = 0
    for x in range(len(input_str)):
        if ((ord(input_str[x]) % 2) != 0):
            total_sum_odd += ord(input_str[x])
    print("ASCII Sum of odd-numbered characters : ", total_sum_odd)


def ascii_sum_even(input_str):
    total_sum_even = 0
    for x in range(len(input_str)):
        if (ord(input_str[x]) % 2 == 0):
            total_sum_even += ord(input_str[x])
    print("ASCII Sum of even-numbered characters : ", total_sum_even)


input_str = input("Enter a string: ")
ascii_sum(input_str)
ascii_sum_odd(input_str)
ascii_sum_even(input_str)
