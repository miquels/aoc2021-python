import re


def signum(num: int) -> int:
    if num > 0:
        return 1
    if num < 0:
        return -1
    return 0


class Vent:
    def __init__(self, line: str) -> None:
        nums = re.match('^(\d+),(\d+) -> (\d+),(\d+)$', line).groups()
        self.x1 = int(nums[0])
        self.y1 = int(nums[1])
        self.x2 = int(nums[2])
        self.y2 = int(nums[3])


def irange(start: int, end: int):
    if start > end:
        start, end = end, start
    return range(start, end + 1)


class Vents:
    def __init__(self, filename: str) -> None:
        self.grid = []
        self.vents = []
        with open(filename) as f:
            for line in f.readlines():
                self.vents.append(Vent(line))

    def inc_element(self, x: int, y: int) -> None:
        for _ in range(len(self.grid), y + 1):
            self.grid.append([])
        row = self.grid[y]
        for _ in range(len(row), x + 1):
            row.append(0)
        row[x] += 1

    def draw_vents(self) -> None:
        self.grid = []
        for vent in self.vents:
            if vent.x1 == vent.x2:
                for y in irange(vent.y1, vent.y2):
                    self.inc_element(vent.x1, y)
            elif vent.y1 == vent.y2:
                for x in irange(vent.x1, vent.x2):
                    self.inc_element(x, vent.y1)

    def draw_vents_all(self) -> None:
        self.grid = []
        for vent in self.vents:
            x1, y1, x2, y2 = vent.x1, vent.y1, vent.x2, vent.y2
            dx = signum(x2 - x1)
            dy = signum(y2 - y1)
            while True:
                self.inc_element(x1, y1)
                if x1 == x2 and y1 == y2:
                    break
                x1 += dx
                y1 += dy

    def overlaps(self) -> int:
        overlaps = 0
        for row in self.grid:
            for elem in row:
                if elem >= 2:
                    overlaps += 1
        return overlaps


if __name__ == "__main__":
    v = Vents('day05-input.txt')
    v.draw_vents()
    overlaps = v.overlaps()
    print(f'part1: {overlaps} overlaps')
    v.draw_vents_all()
    overlaps = v.overlaps()
    print(f'part2: {overlaps} overlaps')
