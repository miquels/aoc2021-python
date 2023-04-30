import re


class Board:
    def __init__(self, lines):
        self.rows = []
        for line in lines.splitlines():
            row = list(map(int, line.split()))
            self.rows.append(row)

    def __str__(self):
        data = ''
        for r in self.rows:
            data += f'{r[0]:2d} {r[1]:2d} {r[2]:2d} {r[3]:2d} {r[4]:2d}\n'
        return data

    def is_bingo(self, rowidx, colidx):
        # First check the horizontal row for bingo
        if sum(map(lambda x: int((x & 0x80) > 0), self.rows[rowidx])) == 5:
            return True
        # Then the vertical column.
        for row in self.rows:
            if (row[colidx] & 0x80) == 0:
                return False
        return True

    def check(self, number):
        for rowidx in range(0, len(self.rows)):
            row = self.rows[rowidx]
            for colidx in range(0, len(row)):
                if row[colidx] == number:
                    row[colidx] |= 0x80
                    return self.is_bingo(rowidx, colidx)
        return False

    def score(self, num):
        s = 0
        for row in self.rows:
            s += sum(map(lambda x: x if (x & 0x80) == 0 else 0, row))
        return s * num


class Game:
    def __init__(self, input):
        with open(input) as f:
            data = f.read()
            blocks = re.split('\n\n', data)
        self.numbers = list(map(int, re.split(',', blocks.pop(0))))
        self.boards = []
        for block in blocks:
            self.boards.append(Board(block))

    def __str__(self):
        data = ','.join(map(str, self.numbers))
        data += '\n'
        for board in self.boards:
            data += '\n'
            data += board.__str__()
        return data

    def play(self, last=False):
        for num in self.numbers:
            bnum = 0
            while bnum < len(self.boards):
                board = self.boards[bnum]
                if board.check(num):
                    if not last or len(self.boards) == 1:
                        return board.score(num)
                    self.boards.pop(bnum)
                    bnum -= 1
                bnum += 1
        return -1


def play(input, part):
    game = Game(input)
    score = game.play(part == 2)
    print(f'part{part}: score is {score}')


if __name__ == "__main__":
    play("day04-input.txt", 1)
    play("day04-input.txt", 2)
