def adapter_array():
    #Store each line in the file as integers
    with open("input", "r") as file:
        lines = [0] + [int(x) for x in file.read().splitlines()]
    lines.sort()

    one = 0
    #Start count at 1 since the the built-in joltage is always 3 higher than the highest-rated adapter
    three = 1
    for i in range(len(lines)-1):
        if lines[i+1] - lines[i] == 1:
            one += 1
        elif lines[i+1] - lines[i] == 3:
            three += 1
    return one*three


def main():
    print(adapter_array())

if __name__ == '__main__':
    main()