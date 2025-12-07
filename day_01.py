def part_one():
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


def part_two():
    dial = 50
    zeros = 0
    with open("./inputs/day_01.txt") as f:
        lines = f.readlines()
        for line in lines:
            dir = line[0]
            move = int(line[1:])
            if dir == "R":
                full, rem = divmod(move, 100)
                new = dial + rem
                crossed = int(dial != 0 and not (0 < new < 100))
                zeros += full + crossed
                dial = new % 100
            elif dir == "L":
                full, rem = divmod(move, 100)
                new = dial - rem
                crossed = int(dial != 0 and not (0 < new < 100))
                zeros += full + crossed
                dial = new % 100
    return zeros


if __name__ == "__main__":
    print(part_one())
    print(part_two())
