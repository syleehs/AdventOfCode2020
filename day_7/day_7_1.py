def handy_haversacks():
    with open("input", "r") as file:
        lines = file.read().splitlines()
    contained_in = {}
    #loop through each line ("bag")
    for line in lines:
        #split the line, to remove the word contain, tmp[0] is the bag that contains all the bags in tmp[1]
        tmp = line.split("contain")
        #split each of the bags in tmp[1]
        tmp_arr = tmp[1].strip()[:-1].split(",")
        outercolor = tmp[0][:-6].strip()
        #Loop through the inner colors, and store which bags it is contained in
        for i in range(len(tmp_arr)):
            innercolor = tmp_arr[i][2:-4].strip()
            if innercolor in contained_in.keys():
                contained_in[innercolor].append(outercolor)
            else:
                contained_in[innercolor] = [outercolor]

    res = set()

    check_color("shiny gold", contained_in, res)
    return len(res)

#Loop & recurse through to determine each of the bags that contain "shiny gold"
def check_color(color, contained_in, holdsgold):
    if color in contained_in.keys():
        for c in contained_in[color]:
            holdsgold.add(c)
            check_color(c, contained_in, holdsgold)
    
    

def main():
    print(handy_haversacks())

if __name__ == '__main__':
    main()