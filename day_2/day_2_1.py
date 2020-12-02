def PasswordPhilosophy():
    valid_passwords = 0
    with open("input", "r") as file:
        for line in file:
            parameters = line.split(" ")
            num_range = parameters[0].split("-")
            mini = int(num_range[0])
            maxi = int(num_range[1])
            char = parameters[1][0]
            #Count # of occurrence of the char, and validate that it fits within the range
            count = parameters[2].count(char)
            if count >= mini and count <= maxi:
                valid_passwords += 1
    return valid_passwords

def main():
    print(PasswordPhilosophy())

if __name__ == '__main__':
    main()