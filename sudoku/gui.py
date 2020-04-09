import tkinter as tk


WIDTH_SQUARE = 100
class GridSquare(tk.Canvas):
    def __init__(self, *args, ** kwargs):
        super().__init__(*args,
                         # borderwidth=0, highlightthickness=0,
                         **kwargs)

        self.create_rectangle(0, 0, WIDTH_SQUARE, WIDTH_SQUARE, fill='lightgrey')
        self.text = self.create_text((50, 50),
                                     width=WIDTH_SQUARE,
                                     text="TODO")

    def set_text(self, text, fill=None, fontsize=None, **kwargs):
        self.itemconfig(self.text, text=text, fill=fill, font=(None, fontsize), **kwargs)


class App(tk.Tk):
    def __init__(self, *args, ** kwargs):
        super().__init__(*args, **kwargs)

        # self.attributes('-alpha', 0)
        # self.attributes("-transparentcolor", "lightgrey")


        self.canvas = tk.Canvas(self, width=WIDTH_SQUARE*9, height=WIDTH_SQUARE*9,
                                # borderwidth=0, highlightthickness=0,
                                )
        self.canvas.pack(side="top",
                         fill="both",
                         expand="true",
                         )

        # self.canvas.config(bg='systemTransparent')

        self.canvas.grid_rowconfigure(1, weight=1)
        self.canvas.grid_columnconfigure(1, weight=1)
        self.grid = {}

        n = 9
        for row in range(n):
            for col in range(n):
                gs = GridSquare(self.canvas, width=WIDTH_SQUARE, height=WIDTH_SQUARE)

                gs.grid(row=row, column=col, sticky="nsew")

                self.grid[row, col] = gs

        for i in range(9+1):
            width = 2 if i % 3 == 0 else 1
            self.canvas.create_line(i*WIDTH_SQUARE, 0, i*WIDTH_SQUARE, WIDTH_SQUARE*9, width=width)
            self.canvas.create_line(0, i*WIDTH_SQUARE, WIDTH_SQUARE*9, i*WIDTH_SQUARE, width=width)

    def set_board(self, board):
        self.board = board

        def foo(*args):
            for i in range(9):
                for j in range(9):
                    val = self.board.state[i, j]
                    if val != 0:
                        # rows is y, columns is x

                        # Start values (black)
                        co = 'black' if self.board.start_state[i, j] != 0 else 'blue'

                        self.grid[i, j].set_text(val, fill=co, fontsize=30)

                    else:
                        center_vals = ','.join(map(str, self.board.center_lst[i][j]))

                        self.grid[i, j].set_text(center_vals, fill='blue', fontsize=12)

        self.board.show = foo   # overwrite function

    def set_agent(self, agent):

        self.agent = agent

    def play(self):
        print("play")

        # agent.solve(self.board)
        self.agent.play(self.board)

    def autoplay(self, wait=100):

        self.play()
        self.board.show()

        if self.board.chech_finished():
            print('Finished')
            return

        self.after(wait, lambda: self.autoplay())


if __name__ == '__main__':

    app = App()

    print(1)

    from sudoku.bot import Agent, Board
    from sudoku.example import example2

    app.set_board(Board(example2()))
    app.set_agent(Agent())

    app.autoplay()

    app.mainloop()

    print(2)
