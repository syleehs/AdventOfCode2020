# DP solution
# Calculate each section as "2020 - num" and check within the dictionary if that value has been calculated
def ReportRepair():
    dic = {}
    with open("input.txt", "r") as file:
        for line in file:
            num = int(line)
            if num in dic.keys():
                return num * dic[num]
            dic[2020 - int(line)] = num
    
    
def main():
    print(ReportRepair())

if __name__ == '__main__':
    main()