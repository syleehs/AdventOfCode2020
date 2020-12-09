#Store each line in the file as integers
with open("input", "r") as file:
    lines = [int(x) for x in file.read().splitlines()]

def encoding_error():    
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

def encryption_weakness(val):
    #Similarly as before, generate the expected value for each index in lines
    subtract = [val] * len(lines)
    upper_bound = 0
    lower_bound = 0
    length = len(lines)
    #Loop through each index
    for i in range(1, length):
        #Subtract one index at a time
        for j in range(i, length):
            subtract[j] -= lines[j-i]
        #Determine if we can sum up to the value, if so store the index at which it occurs
        for j in range(i, length):
            for x in range(j-i, j):
                if lines[x] in subtract[j-i: j]:
                    upper_bound = x
        #Once the upper-bound index is found, store the lower-bound index
        if upper_bound != 0:
            lower_bound = i
            break
    largest = lines[upper_bound-lower_bound]
    smallest = largest
    #Iterate through to determine smallest and largest value within the range
    for i in range(upper_bound-lower_bound, upper_bound):
        if lines[i] > largest:
            largest = lines[i]
        elif lines[i] < smallest:
            smallest = lines[i]
    #Return the encryption weakness
    return largest+smallest


def main():
    print(encryption_weakness(encoding_error()))

if __name__ == '__main__':
    main()