import math
def toboggan_trajectory():
    trees_encountered = {(1, 1): 0, (3, 1): 0, (5, 1): 0, (7, 1): 0, (1, 2): 0}

    with open("input", "r") as file:
        lines = file.readlines()
    width = len(lines[0]) - 1

    for slope in trees_encountered.keys():
        x, y = 0, 0
        down = slope[1]
        right = slope[0]
        for i in range(0, math.ceil(len(lines)/(slope[1]))):
            char = lines[y][x]
            if char == "#":
                trees_encountered[slope] += 1
            x = (x + right) % width
            y += down

    res = 1
    for trees_slope in trees_encountered.values():
        res *= trees_slope
    return res


def main():
    print(toboggan_trajectory())

if __name__ == '__main__':
    main()