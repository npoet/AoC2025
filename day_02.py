def part_one():
    with open("inputs/day_02.txt") as f:
        ranges = f.readline().strip().split(",")
        invalid_ids = 0
        for id_range in ranges:
            id_min, id_max = id_range.split("-")
            for num in range(int(id_min), int(id_max) + 1):
                n = len(str(num))
                if n % 2 != 0:
                    continue
                half = n // 2
                first = str(num)[:half]
                second = str(num)[half:]
                if first == second:
                    invalid_ids += num
    return invalid_ids


if __name__ == "__main__":
    print(part_one())
