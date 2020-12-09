with open("input", "r") as file:
    lines = [int(x) for x in file.read().splitlines()]

def encoding_error():    
    for i in range(25, len(lines)):
        subtract = [lines[i]] * 25
        index = 0
        flag = False
        for j in range(i-25, i):
            subtract[index] -= lines[j]
            index += 1
        for j in range(i-25, i):
            if lines[j] in subtract:
                flag = True
                break
        if not flag:
            return lines[i]
    return

def encryption_weakness(val):
    subtract = [val] * len(lines)
    x = 0
    y = 0
    length = len(lines)
    for i in range(1, length):
        for j in range(i, length):
            subtract[j] -= lines[j-i]
        for j in range(i, length):
            for z in range(j-i, j):
                if lines[z] in subtract[j-i: j]:
                    x = z
        if x != 0:
            y = i
            break
    largest = lines[x-y]
    smallest = lines[x-y]
    for i in range(x-y, x):
        if lines[i] > largest:
            largest = lines[i]
        elif lines[i] < smallest:
            smallest = lines[i]
    
    return largest+smallest


def main():
    print(encryption_weakness(encoding_error()))

if __name__ == '__main__':
    main()