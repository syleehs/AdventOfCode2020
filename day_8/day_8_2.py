def handheld_halting():
    with open("input", "r") as file:
        lines = file.read().splitlines()

    for i in range(len(lines)):
        program = lines.copy()
        command = program[i]
        if command.startswith('jmp'):
            program[i] = program[i].replace('jmp', 'nop')
        elif command.startswith('nop'):
            program[i] = program[i].replace('nop', 'jmp')
        res = run_program(program)
        if res:
            break
    return res

def run_program(lines):
    visited = set()
    res = 0
    index = 0
    while True:
        if index in visited:
            return None
        visited.add(index)

        try:
            command, val = lines[index].split(" ")
            if command == "nop":
                index += 1
            elif command == "acc":
                index += 1
                res += int(val)
            elif command == "jmp":
                index += int(val)
        except:
            return res

def main():
    print(handheld_halting())

if __name__ == '__main__':
    main()