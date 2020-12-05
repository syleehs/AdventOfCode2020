import math
def binary_boarding():
    with open("input", "r") as file:
        lines = file.read().splitlines()
    
    min_id, max_id = 1000, 0
    sum_ids = 0

    for boarding_pass in lines:

        min_row, max_row = 0, 127
        min_col, max_col = 0, 7

        for char in boarding_pass[:7]:
            if char == "F":
                max_row = math.floor((max_row + min_row)/2)
            if char == "B":
                min_row = math.ceil((max_row + min_row)/2)

        for char in boarding_pass[-3:]:
            if char == "L":
                max_col = math.floor((max_col + min_col)/2)
            if char == "R":
                min_col = math.ceil((max_col + min_col)/2)

        seat_id = max_row * 8 + max_col
        sum_ids += seat_id

        if seat_id > max_id:
            max_id = seat_i

        elif seat_id < min_id:
            min_id = seat_id

    total = (max_id + 1) * max_id / 2 - (min_id - 1) * min_id / 2
    res = total - sum_ids

    return res

def main():
    print(binary_boarding())

if __name__ == '__main__':
    main()