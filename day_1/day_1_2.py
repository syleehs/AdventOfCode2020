#Similar to a 3SUM problem
def report_repair():
    dic = {}
    nums = []
    with open("input", "r") as file:
        for line in file:
            nums.append(int(line))
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            dic[2020 - nums[i] - nums[j]] = nums[i] * nums[j]
    for num in nums:
        if num in dic.keys():
            return dic[num] * num
    
def main():
    print(report_repair())

if __name__ == '__main__':
    main()