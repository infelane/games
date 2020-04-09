import matplotlib.pyplot as plt
import numpy as np

from sudoku.example import example1


class Agent(object):
    def __init__(self):

        # Everything is possible init
        self.possibilities = [[range(1, 9 + 1) for _ in range(9)] for _ in range(9)]

    def solve(self, board):

        while not board.chech_finished():
            # go over all possibilities

            self.play()

            # Show possibilities
            print(self.possibilities)
            board.show()

            input("pause")

    def next(self):
        if not hasattr(self, 'i'):
            # init
            self.i = 0
            self.j = 0
        else:
            self.i += 1
            if self.i >= 9:
                self.i = 0
                self.j += 1
            if self.j >= 9:
                self.j = 0

            """
            TODO if j at 9, don't know what to do
                a) reset
                b) do nothing "and stop"
            """

        return self.i, self.j

    def play(self, board):

        i, j = self.next()

        def foo(i, j):
            poss = self.possibilities[i][j]
            poss_valid = []
            for val in poss:
                state_copy = np.copy(board.state)
                if state_copy[i, j] == 0:
                    state_copy[i, j] = val

                    if board.legit_move(state_copy):
                        poss_valid.append(val)

            if len(poss_valid) == 1:
                board.play(i + 1, j + 1, poss_valid[0])
                self.possibilities[i][j] = []  # empty
            else:
                # Update possiblities
                self.possibilities[i][j] = poss_valid
                board.center(i, j, poss_valid)

        # for i in range(9):
        #     for j in range(9):
        #         foo(i, j)
        foo(i, j)


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
        """
        Between 1 and 9
        :param i_hor:
        :param i_ver:
        :param number:
        :return:
        """
        assert isinstance(i_hor, int)
        assert isinstance(i_ver, int)
        assert isinstance(number, int)
        assert 1 <= i_hor <= 9
        assert 1 <= i_ver <= 9
        assert 1 <= number <= 9

        self.state[i_hor-1, i_ver-1] = number


class Board(SudokuSimple):
    def __init__(self, state):
        super().__init__(state)

        self.center_lst = [[[] for _ in range(9)] for _ in range(9)]

        # plt.ion()
        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111)

    def show(self):

        plt.xlim((0, 9))
        plt.ylim((9, 0))
        plt.axis('off')
        for i in range(0, 9+1):
            linewidth = 2 if (i % 3 == 0) else 1
            plt.plot((0, 9), (i, i), linewidth=linewidth, color='black')
            plt.plot((i, i), (0, 9), linewidth=linewidth, color='black')
            del(linewidth)

        self.ax.axis('equal')

        for i in range(9):
            for j in range(9):
                val = self.state[i, j]
                if val != 0:
                    # rows is y, columns is x

                    # Start values (black)
                    co = 'black' if self.start_state[i, j] != 0 else 'blue'
                    self.ax.text(j+.5, i+.5, val,
                                 color=co,
                                 horizontalalignment='center',
                                 verticalalignment='center',
                                 )

                else:
                    center_vals = ','.join(map(str, self.center_lst[i][j]))
                    self.ax.text(j+.5, i+.5, center_vals,
                                 fontsize=6,
                                 color = 'blue',
                                 horizontalalignment='center',
                                 verticalalignment='center',
                                 )

        plt.show(block=False)

        # print(self.state)

    def chech_finished(self, state=None):

        if state is None:
            state = self.state

        lst = list(state.flatten())
        l_nonzero = list(filter(lambda x: x != 0, lst))
        b_everything_filled = len(l_nonzero) == 9*9

        return b_everything_filled and self.legit_move(state)

    def legit_move(self, state=None):
        def unique(lst):
            lst = list(lst.flatten())
            l_nonzero = list(filter(lambda x: x != 0, lst))
            return len(l_nonzero) == len(set(l_nonzero))

        if state is None:
            state = self.state

        # no duplicates in row
        for i in range(9):
            row = state[i, :]
            if unique(row) is False:
                return False

        # no duplicates in column
        for j in range(9):
            col = state[:, j]
            if unique(col) is False:
                return False

        # no duplicates in square
        for i in range(3):
            for j in range(3):
                sq = state[i*3:(i+1)*3, j*3:(j+1)*3]
                if unique(sq) is False:
                    return False

        return True # Everything is fine

    def rules(self):
        # horizontal unique
        # vertical unique
        # per square unique
        pass

    def play(self, i_hor, i_ver, number):
        super().play(i_hor, i_ver, number)

        self.show()

    def center(self, i, j, poss_valid):

        assert 0 <= i < 9
        assert 0 <= j < 9
        assert isinstance(poss_valid, list)
        for a in poss_valid:
            assert isinstance(a, int)

        self.center_lst[i][j] = poss_valid

    def cheque_finish(self):
        # If filled in
        # and legit
        return 1 and self.legit_move()


if __name__ == '__main__':

    board = Board(example1())

    print(board.legit_move())

    print(board.legit_move())

    board.show()

    agent = Agent()
    agent.solve(board)

    input("finished")
    plt.show()
