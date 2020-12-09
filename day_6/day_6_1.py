import math
def custom_customs():
    with open("input", "r") as file:
        lines = file.read().splitlines()

    res = 0
    ans = ''
    group_ans = []
    #Retrieve all the answers
    for line in lines:
        if line == '':
            group_ans.append(ans)
            ans = ''
        else:
            ans += line
    #Does not trigger the last line, add the last group answers
    group_ans.append(ans)

    #Based on the combined answers, count total of all answers
    for combined_ans in group_ans:
        res += len(set(combined_ans))
    return res

def main():
    print(custom_customs())

if __name__ == '__main__':
    main() 