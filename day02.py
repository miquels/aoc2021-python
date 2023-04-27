def part1(input):
    x = 0
    d = 0
    with open(input) as f:
        for line in f:
            words = line.split(' ')
            amount = int(words[1])
            match words[0]:
                case "forward":
                    x += amount
                case "down":
                    d += amount
                case "up":
                    d -= amount
    print(f'part1: {x} * {d} = {x*d}')


def part2(input):
    x = 0
    d = 0
    aim = 0
    with open(input) as f:
        for line in f:
            words = line.split(' ')
            amount = int(words[1])
            match words[0]:
                case "forward":
                    x += amount
                    d += amount * aim
                case "down":
                    aim += amount
                case "up":
                    aim -= amount
    print(f'part2: {x} * {d} = {x*d}')


if __name__ == "__main__":
    part1("day02-input.txt")
    part2("day02-input.txt")
