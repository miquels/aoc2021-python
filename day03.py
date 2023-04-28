from functools import reduce


def part1(input):
    lines = 0
    ones = []
    with open(input) as f:
        for line in f:
            lines += 1
            digits = [*line.strip()]
            for i in range(0, len(digits)):
                if len(ones) == i:
                    ones.append(0)
                if digits[i] == '1':
                    ones[i] += 1
    gamma = 0
    epsilon = 0
    for i in range(0, len(ones)):
        gamma <<= 1
        epsilon <<= 1
        if ones[i] >= lines / 2:
            gamma |= 1
        else:
            epsilon |= 1
    print(
        f'part1: gamma {gamma} epsilon {epsilon} power consumption: {gamma*epsilon}')


def filter_list(list, index, is_oxy):
    ones = reduce(lambda accum, x: accum + int(x[index] == '1'), list, 0)
    if is_oxy:
        digit = '1' if ones >= len(list) / 2 else '0'
    else:
        digit = '1' if ones < len(list) / 2 else '0'
    return [x for x in list if x[index] == digit]


def reduce_list(list, is_oxy):
    index = 0
    while len(list) > 1:
        list = filter_list(list, index, is_oxy)
        index += 1
    return int(''.join(list[0]), 2)


def part2(input):
    list = []
    with open(input) as f:
        for line in f:
            digits = [*line.strip()]
            list.append(digits)
    oxy = reduce_list(list, True)
    co2 = reduce_list(list, False)
    print(f'part2: oxy: {oxy}, co2: {co2}, life support rating: {oxy*co2}')


if __name__ == "__main__":
    part1("day03-input.txt")
    part2("day03-input.txt")
