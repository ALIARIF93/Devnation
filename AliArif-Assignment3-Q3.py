def check_dna_str(str_in):
    for x in range(len(str_in)):
        if(str_in[x] != "A"):
            if(str_in[x] != "C"):
                if(str_in[x] != "G"):
                    if(str_in[x] != "T"):
                        return False
    return True


def reverse(str_in):
    str_rev = []
    str_in_len = len(str_in)
    for x in range(str_in_len-1, -1, -1):
        str_rev.append(str_in[x])
    return str_rev


def complement(str_in):
    str_comp = []
    str_in_len = len(str_in)
    for x in range(str_in_len):
        if(str_in[x] == "A"):
            str_comp.append("T")
        elif(str_in[x] == "T"):
            str_comp.append("A")
        elif(str_in[x] == "C"):
            str_comp.append("G")
        else:
            str_comp.append("C")
    return str_comp


dna_str = []
rev_dna_str = []
comp_dna_str = []
is_dna_valid = bool()

dna_str = input("Please input DNA String: ")
is_dna_valid = check_dna_str(dna_str)
if (is_dna_valid):
    rev_dna_str = reverse(dna_str)
    print("Reverse DNA String: ", rev_dna_str)
    print("\r")
    comp_dna_str = complement(rev_dna_str)
    print("Complement DNA String: ", comp_dna_str)
    print("\r")
else:
    print("Wrong DNA String!!")
    print("\r\r")
    print("DNA is made up of 4 complex organic building blocks called “nucleotides”. The nucleotides are Adenine, Cytosine, Guanine, and Thymine (abbreviated as A, C, G, and T respectively")
