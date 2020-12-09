import math
def binary_boarding():
    res = 0
    with open("input", "r") as file:
        lines = file.read().splitlines()
    #Loop through each line from the input
    for boarding_pass in lines:
        min_row, max_row = 0, 127
        min_col, max_col = 0, 7
        #Go through each char in the first 7 chars to determine the row
        for char in boarding_pass[:7]:
            if char == "F":
                max_row = math.floor((max_row + min_row)/2)
            if char == "B":
                min_row = math.ceil((max_row + min_row)/2)
        #Go through the last 3 char to determine the column
        for char in boarding_pass[-3:]:
            if char == "L":
                max_col = math.floor((max_col + min_col)/2)
            if char == "R":
                min_col = math.ceil((max_col + min_col)/2)
        #Determine the highest seat ID
        if (max_row * 8 + max_col) > res:
            res = max_row * 8 + max_col
    return res

def main():
    print(binary_boarding())

if __name__ == '__main__':
    main()