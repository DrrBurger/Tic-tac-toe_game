import tkinter
from tkinter import messagebox


class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title('Крестики-нолики')

        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]

        self.create_board()

    def create_board(self):
        self.buttons = []
        for i in range(9):
            button = tkinter.Button(self.master, text=' ', width=5, height=2,
                                    command=lambda idx=i: self.make_move(idx))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def make_move(self, idx):
        if self.board[idx] == ' ':
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)

            if self.check_win():
                self.show_win_message()
            elif self.check_draw():
                self.show_draw_message()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_win(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != ' ':
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != ' ':
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != ' ':
            return True
        elif self.board[2] == self.board[4] == self.board[6] != ' ':
            return True

        return False

    def check_draw(self):
        return ' ' not in self.board

    def show_win_message(self):
        winner = '0' if self.current_player == 'O' else 'X'
        message = f'Победил {winner}!'
        tkinter.messagebox.showinfo('Конец игры', message)
        self.reset()

    def show_draw_message(self):
        tkinter.messagebox.showinfo('Конец игры', 'Ничья!')
        self.reset()

    def reset(self):
        self.current_player = 'X'
        self.board = [' ' for _ in range(9)]
        for button in self.buttons:
            button.config(text=' ')


root = tkinter.Tk()
game = TicTacToe(root)
root.mainloop()
