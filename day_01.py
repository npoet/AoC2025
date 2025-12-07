def handle_lines():
    dial = 50
    zeros = 0
    with open("./inputs/day_01.txt") as f:
        lines = f.readlines()
        for line in lines:
            dir = line[0]
            move = int(line[1:])
            if dir == "R":
                dial = (dial + move) % 100
            elif dir == "L":
                dial = (dial - move) % 100
            if dial == 0:
                zeros += 1
    return zeros


if __name__ == "__main__":
    print(handle_lines())
