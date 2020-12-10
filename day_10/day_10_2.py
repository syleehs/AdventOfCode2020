#Store each line in the file as integers
with open("input", "r") as file:
    lines = [0] + [int(x) for x in file.read().splitlines()]
lines.sort()
lines.append(lines[len(lines)-1] + 3)

#Some sort of broken fibonacci
def adapter_array():
    dp = [1]+[0]*lines[-1]
    #If value i is not in lines, it will always retain 0, thus having no effect when processing the sack
    for i in lines[1:]: 
        #Always look 3 behind as that is the max jolt jump you can make
        #This is the subproblems
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    return dp[-1]


def main():
    print(adapter_array())

if __name__ == '__main__':
    main()