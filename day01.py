def part1(input):
    count = 0
    last = 0
    with open(input) as f:
        for line in f:
            num = int(line)
            # print(num)
            if num > last and last != 0:
                count += 1
            last = num
    print(f"part1: {count}")


def part2(input):
    count = 0
    last = 0
    with open(input) as f:
        nums = list(map(int, f.read().splitlines()))
        for i in range(0, len(nums) - 2):
            num = sum(nums[i:i+3])
            # print(num)
            if num > last and last != 0:
                count += 1
            last = num
    print(f'part2: {count}')


if __name__ == "__main__":
    part1("day01-input.txt")
    part2("day01-input.txt")
