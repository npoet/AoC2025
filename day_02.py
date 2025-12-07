def part_one():
    with open("inputs/day_02.txt") as f:
        ranges = f.readline().strip().split(",")
    return ranges

if __name__ == "__main__":
    print(part_one())
