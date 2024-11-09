class Connect4:
    def __init__(self):
        # Create a 6x7 board filled with 0 (empty)
        self.board = [[0 for _ in range(7)] for _ in range(6)]
        self.current_player = 1  # Player 1 starts (represented by 1)
    
    def print_board(self):
        """Print the current state of the board."""
        print("-------------")
        for row in self.board:
            print("|", end="")
            for col in row:
                print(f" {col} ", end="|")
            print("\n-------------")

    def drop_disc(self, column):
        """Drop a disc into the given column and return the row index where the disc lands."""
        for row in range(5, -1, -1):  # Start from the bottom row (5 is the last row)
            if self.board[row][column] == 0:  # If the spot is empty
                self.board[row][column] = self.current_player
                return row
        return None  # Column is full
    
    def switch_player(self):
        """Switch the current player."""
        self.current_player = 2 if self.current_player == 1 else 1

    def check_win(self, row, col):
        """Check if the current player has won after a move."""
        # Check horizontal, vertical, and two diagonal directions
        directions = [
            [(0, 1), (0, -1)],  # Horizontal (left-right)
            [(1, 0), (-1, 0)],  # Vertical (up-down)
            [(1, 1), (-1, -1)],  # Diagonal (down-right, up-left)
            [(1, -1), (-1, 1)]   # Diagonal (down-left, up-right)
        ]
        
        for direction in directions:
            count = 1  # Count the current piece
            # Check both directions for this line
            for d in direction:
                r, c = row + d[0], col + d[1]
                while 0 <= r < 6 and 0 <= c < 7 and self.board[r][c] == self.current_player:
                    count += 1
                    r += d[0]
                    c += d[1]
                if count >= 4:
                    return True
        return False

    def get_column_input(self):
        """Validate the user's column input."""
        while True:
            try:
                column = int(input("Choose a column (0-6): "))
                if column < 0 or column > 6:
                    print("Invalid input! Please enter a number between 0 and 6.")
                elif self.board[0][column] != 0:
                    print("Column is full! Try a different column.")
                else:
                    return column
            except ValueError:
                print("Invalid input! Please enter an integer.")

    def play_game(self):
        """Start and run the Connect 4 game loop."""
        while True:
            self.print_board()
            print(f"Player {self.current_player}'s turn")
            column = self.get_column_input()  # Get the valid column input
            row = self.drop_disc(column)
            if self.check_win(row, column):
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break
            self.switch_player()


# Create a game instance and start the game
game = Connect4()
game.play_game()
