def passport_processing():
    res = 0
    arr = []
    batch = []

    with open("input", "r") as file:
        lines = file.readlines()

    for line in lines:
        if line == "\n":
            batch.append(arr)
            arr = []
        else:
            entries = line.strip().split(" ")
            for entry in entries:
                arr.append(entry[:3])

    batch.append(arr)

    for entry in batch:
        if "cid" in entry:
            if len(entry) == 8:
                res += 1
        else:
            if len(entry) == 7:
                res += 1
    return res

def main():
    print(passport_processing())

if __name__ == '__main__':
    main()