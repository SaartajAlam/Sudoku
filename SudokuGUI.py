import tkinter as tk

from sudoku import print_board, find_empty, solve, ok

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")

        # Create a 9x9 grid of entry widgets for user input
        self.entries = [[tk.Entry(root, width=2) for _ in range(9)] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j].grid(row=i, column=j)

        # Create a Solve button
        solve_button = tk.Button(root, text="Solve", command=self.solve_sudoku)
        solve_button.grid(row=9, column=4)

    def solve_sudoku(self):
        # Retrieve the user-input Sudoku puzzle from entry widgets
        user_input = [[int(entry.get()) if entry.get() else 0 for entry in row] for row in self.entries]

        # Call your existing solve function with the user input
        solve(user_input)

        # Display the solved Sudoku puzzle in the entry widgets
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(user_input[i][j]))

if __name__ == "__main__":
    root = tk.Tk()
    sudoku_gui = SudokuGUI(root)
    root.mainloop()
