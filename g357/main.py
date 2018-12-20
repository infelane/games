class Board():
    def __init__(self):
        self.rows = [3, 5, 7]

    def print_state(self):
        for row in self.rows:
            print('|'*row)

    def moves_available(self):
        moves = []
        for i in range(len(self.rows)):
            row = self.rows[i]
            if row > 0:
                moves.append(i)
        # print('available moves:', *moves)
        return moves

    def sticks_remove(self, i_row):
        moves = []
        for i in range(self.rows[i_row]):
            moves.append(i+1)
        #     row = self.rows[i]
        #     if row > 0:
        #         moves.append(i)
        # print('available moves:', *moves)
        return moves
    
    def remove(self, i_row, n_sticks):
        self.rows[i_row] -= n_sticks

    def ask_input(self, acceptable):
        str_acceptable = [str(a) for a in acceptable]
        str_output = "Available inputs: {}".format(', '.join(str_acceptable))
        print(str_output)
        text = input('enter: ')
        while text not in str_acceptable:
            text = input('enter: ')
        return text

    def next_play(self):
        self.print_state()
        moves = self.moves_available()

        i_row = int(self.ask_input(moves))
        moves = self.sticks_remove(i_row)
        n_sticks = int(self.ask_input(moves))
        
        self.remove(i_row, n_sticks)
        
        if self.check_lost():
            print('You lost')
            return 0
        return 1
        
    def check_lost(self):
        return not bool(self.moves_available())


def main():
    board = Board()

    while board.next_play():
        pass
    # print('1')
    # board.next_play()
    # print('2')
    # board.next_play()

    print('Done')

if __name__ == '__main__':
    main()