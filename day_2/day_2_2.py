def PasswordPhilosophy():
    valid_passwords = 0
    with open("input", "r") as file:
        for line in file:
            parameters = line.split(" ")
            num_range = parameters[0].split("-")
            char = parameters[1][0]
            stri = parameters[2]
            #Check if the string contains the char at the index
            index_1 = stri[int(num_range[0])-1] == char
            index_2 = stri[int(num_range[1])-1] == char
            #Validate only 1 of the indexes contains the char
            if (index_1 and not index_2) or (index_2 and not index_1):
                valid_passwords += 1
    return valid_passwords

def main():
    print(PasswordPhilosophy())

if __name__ == '__main__':
    main()