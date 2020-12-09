import math
def binary_boarding():
    with open("input", "r") as file:
        lines = file.read().splitlines()
    
    min_id, max_id = 1000, 0
    sum_ids = 0

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

        seat_id = max_row * 8 + max_col
        sum_ids += seat_id
        #Find max id
        if seat_id > max_id:
            max_id = seat_i
        #Find the min id
        elif seat_id < min_id:
            min_id = seat_id

    #Some math here... Determine the expected sum for the range
    total = (max_id + 1) * max_id / 2 - (min_id - 1) * min_id / 2
    #From the sum_ids calculated before, subtract the expected sum with the real sum to determine the missing value
    res = total - sum_ids

    return res

def main():
    print(binary_boarding())

if __name__ == '__main__':
    main()