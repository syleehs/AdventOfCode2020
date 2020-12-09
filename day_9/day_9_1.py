def encoding_error():
    with open("input", "r") as file:
        lines = [int(x) for x in file.read().splitlines()]
    
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

    

def main():
    print(encoding_error())

if __name__ == '__main__':
    main()