def handy_haversacks():
    with open("input", "r") as file:
        lines = file.read().splitlines()
    contains = {}
    #loop through each line ("bag")
    for line in lines:
        #split the line, to remove the word contain, tmp[0] is the bag that contains all the bags in tmp[1]
        tmp = line.split("contain")
        #split each of the bags in tmp[1]
        tmp_arr = tmp[1].strip()[:-1].split(",")
        #Store which inner bags the outer bag contains
        for i in range(len(tmp_arr)):
            tmp_arr[i] = tmp_arr[i][:-4].strip()
        outercolor = tmp[0][:-6].strip()
        contains[outercolor] = tmp_arr

    return count_bags("shiny gold", contains)

#Loop and recurse through to determine how many bags the shiny gold bag contains
def count_bags(color, contains):
    total = 0
    if color in contains.keys():
        for c in contains[color]:
            if c != "no other":
                total += int(c[0])
                total += int(c[0]) * count_bags(c[2:], contains)
    return total
    
    

def main():
    print(handy_haversacks())

if __name__ == '__main__':
    main()