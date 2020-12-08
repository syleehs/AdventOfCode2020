def handy_haversacks():
    with open("input", "r") as file:
        lines = file.read().splitlines()
    contained_in = {}

    for line in lines:
        tmp = line.split("contain")
        tmp_arr = tmp[1].strip()[:-1].split(",")
        outercolor = tmp[0][:-6].strip()
        for i in range(len(tmp_arr)):
            innercolor = tmp_arr[i][2:-4].strip()
            if innercolor in contained_in.keys():
                contained_in[innercolor].append(outercolor)
            else:
                contained_in[innercolor] = [outercolor]

    res = set()

    check_color("shiny gold", contained_in, res)
    return len(res)

    
def check_color(color, contained_in, holdsgold):
    if color in contained_in.keys():
        for c in contained_in[color]:
            holdsgold.add(c)
            check_color(c, contained_in, holdsgold)
    
    

def main():
    print(handy_haversacks())

if __name__ == '__main__':
    main()