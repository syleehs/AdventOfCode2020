def toboggan_trajectory():
    x = 0
    trees_encountered = 0
    with open("input", "r") as file:
        for line in file:
            if (line[x % (len(line)-1)] == "#"):
                trees_encountered += 1
            x += 3
    return trees_encountered


def main():
    print(toboggan_trajectory())

if __name__ == '__main__':
    main()