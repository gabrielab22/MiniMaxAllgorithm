# -1 - GAME IN PROGRESS
# 1 - PLAYER
# 2 - COMPUTER


class Sticks:

    _picks = [1, 2]

    def __init__(self):
        self._sticks = 11
        self._turn = 1

    def __str__(self):
        return "Remaining sticks: " + str(self._sticks)

    def move(self, numOfSticks):
        self._sticks = self._sticks - numOfSticks
        # move is played, change who plays next
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = 1

    def undo(self, numOfSticks):
        self._sticks = self._sticks + numOfSticks
        if self._turn == 1:
            self._turn = 2
        else:
            self._turn = -1

    def game_over(self):
        if self._sticks == 2:
            return self._turn
        elif self._sticks == 1:
            if self._turn == 1:
                result = 2
            else:
                result = 1
            return result
        else:
            return -1


def minimax(game):
    rez = game.game_over()
    if rez != -1:  # -1 -> game in progress
        if rez == 2:
            return 1000, None
        elif rez == 1:
            return -1000, None
        else:
            return 0, None
    if game._turn == 2:
        maxv, maxm = -10000, None
        for m in game._picks:
            game.move(m)
            v, _ = minimax(game)
            game.undo(m)
            if maxv < v:
                maxv, maxm = v, m
        return maxv, maxm
    else:
        minv, minm = 10000, None
        for m in game._picks:
            game.move(m)
            v, _ = minimax(game)
            game.undo(m)
            if minv > v:
                minv, minm = v, m
        return minv, minm


def main():
    sticks = Sticks()
    while sticks.game_over() == -1:
        print(sticks)
        if (sticks._turn == 1):
            pick = int(input("1 or 2 -> "))
            sticks.move(pick)
        else:
            v, m = minimax(sticks)
            print("COMPUTER PICKED", m,  "STICK/S")
            sticks.move(m)

    print(sticks._sticks, " STICK/S LEFT AT THE END")
    if sticks.game_over() == 1:
        print("YOU WON!!")
    else:
        print("COMPUTER WON!!")


main()
