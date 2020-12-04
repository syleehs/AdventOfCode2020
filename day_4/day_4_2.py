import re
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
            arr += line.strip().split(" ")

    batch.append(arr)

    for entry in batch:
        res += valid_entry(entry)
    return res

#Check if each entry has 7 valid fields 
def valid_entry(entry):
    count = 0
    for field in entry:
        data = field.split(":")
        if validate_field(data[0], data[1]):
            count += 1
    if count >= 7:
        return 1
    else: 
        return 0

#Returns true if the field & associated value is valid
#Does not care about "cid"
def validate_field(field, value):
    valid = False
    if field == "byr":
        valid = 1920 <= int(value) <= 2002
    elif field == "iyr":
        valid = 2010 <= int(value) <= 2020
    elif field == "eyr":
        valid = 2020 <= int(value) <= 2030
    elif field == "hgt":
        if value[-2:]=="cm":
            val = int(value.split("cm")[0])
            valid = 150 <= val <= 193
        elif value[-2:]=="in":
            val = int(value.split("in")[0])
            valid = 59 <= val <= 76
    elif field == "hcl":
        valid = bool(re.fullmatch("#[0-9a-f]{6}", value))
    elif field == "ecl":
        valid = bool(re.fullmatch("(amb|blu|brn|gry|grn|hzl|oth){1}", value))
    elif field == "pid":
        valid = bool(re.fullmatch("[0-9]{9}", value))
    return valid

def main():
    print(passport_processing())

if __name__ == '__main__':
    main()