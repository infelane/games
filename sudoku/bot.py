import matplotlib.pyplot as plt
import numpy as np

from sudoku.example import example1


class Agent(object):
    def __init__(self):
        pass # TODO


class SudokuSimple():
    state = np.zeros((9, 9), dtype=np.uint8)

    def __init__(self, state):

        state_init = np.array(state, dtype=np.uint8)
        assert self.state.shape == state_init.shape

        for i in range(9):
            for j in range(9):
                n = state_init[i, j]
                if 1 <= n <= 9:
                    self.state[i, j] = n

        self.start_state = np.copy(self.state)

    def play(self, i_hor, i_ver, number):
        assert isinstance(i_hor, int)
        assert isinstance(i_ver, int)
        assert isinstance(number, int)
        assert 1 <= i_hor <= 9
        assert 1 <= i_ver <= 9
        assert 1 <= number <= 9

        self.state[i_hor, i_ver] = number



class Board(SudokuSimple):
    def __init__(self, state):
        super().__init__(state)
        pass

    def show(self):
        print(self.state)

    def legit_move(self, state=None):
        if state is None:
            state = self.state

    def rules(self):
        # horizontal unique
        # vertical unique
        # per square unique
        pass

    def play(self, i_hor, i_ver, number):
        super().play(i_hor, i_ver, number)

        self.show()

    def cheque_finish(self):
        # If filled in
        # and legit
        return 1 and self.legit_move()


if __name__ == '__main__':

    board = Board(example1())

    board.show()

    agent = Agent()
