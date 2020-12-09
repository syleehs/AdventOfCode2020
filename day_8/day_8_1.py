def handheld_halting():
    with open("input", "r") as file:
        lines = file.read().splitlines()

    res = run_program(lines)
    return res

def run_program(lines):
    visited = set()
    res = 0
    index = 0
    while index not in visited:
        command, val = lines[index].split(" ")
        visited.add(index)
        if command == "nop":
            index += 1
        elif command == "acc":
            index += 1
            res += int(val)
        elif command == "jmp":
            index += int(val)
    return res 

def main():
    print(handheld_halting())

if __name__ == '__main__':
    main()