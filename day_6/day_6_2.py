import math
def custom_customs():
    with open("input", "r") as file:
        lines = file.read().splitlines()

    res = 0
    ans = []
    group_ans = []
    #Retrieve all the answers
    for line in lines:
        if line == '':
            group_ans.append(ans)
            ans = []
        else:
            ans.append(line)
    #Does not trigger the last line, add the last group answers
    group_ans.append(ans)

    #Loop through group answers, and determine intersection to get answers where everyone answered yes
    for ans in group_ans:
        flag = 0
        for an in ans:
            if flag == 0:
                temp_set = set(an)
                flag = 1
            else:
                temp_set = temp_set.intersection(set(an))
        res += len(temp_set)
    return res

def main():
    print(custom_customs())

if __name__ == '__main__':
    main()