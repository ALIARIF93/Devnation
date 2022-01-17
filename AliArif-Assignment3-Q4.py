def is_prime(str_in):
    num_in = int(str_in)
    if (num_in == 1):
        return False
    elif (num_in == 2):
        return True
    else:
        for x in range(2, num_in):
            if ((num_in % x) == 0):
                return False
        return True

def factors(str_in):
    num_in = int(str_in)
    arr_fact = [1]
    for x in range(2, num_in, 1):
        if (num_in % x == 0):
            arr_fact.append(x)
    arr_fact.append(num_in)
    return arr_fact


def prime_factors(str_in):
    arr_fact = factors(str_in)
    arr_fact_prime = []
    for x in range(0, len(arr_fact), 1):
        if(is_prime(arr_fact[x])):
            arr_fact_prime.append(arr_fact[x])
    return arr_fact_prime


num = input("Please enter your number: ")
print("\r\r")
print("\r\r")
if (is_prime(num)):
    print(num, " is Prime Number")
else:
    print(num, " is not a Prime Number")
print("\r\r")
print("Factors of ", num, ": ", factors(num))
print("\r\r")
print("Prime Factors of ", num, ": ", prime_factors(num))
