def encoding_error():
    #Store each line in the file as integers
    with open("input", "r") as file:
        lines = [int(x) for x in file.read().splitlines()]
    
    #Loop starting from the 25th index
    for i in range(25, len(lines)):
        #Generate the expected sum * 25 to subtract
        subtract = [lines[i]] * 25
        index = 0
        flag = False
        #Subtract each index from the sum and store it
        for j in range(i-25, i):
            subtract[index] -= lines[j]
            index += 1
        #Determine if it matches the property
        for j in range(i-25, i):
            if lines[j] in subtract:
                flag = True
                break
        if not flag:
            return lines[i]
    return


def main():
    print(encoding_error())

if __name__ == '__main__':
    main()