import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")
        self.root.resizable(False, False)
        
        # Game state variables
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0: empty, 1: O, -1: X
        self.buttons = []
        self.game_over = False
        self.game_mode = 1  # Default: 1 for single player, 2 for multiplayer
        self.player_turn = True  # True if it's player's turn in single player mode
        
        # Create the game layout
        self.create_menu()
        self.create_mode_selection()
        self.create_game_board()
        self.create_status_bar()
        self.create_control_buttons()

    def create_menu(self):
        """Create the application menu"""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)
        
        game_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Game", menu=game_menu)
        game_menu.add_command(label="New Game", command=self.reset_game)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.root.quit)
        
        help_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def create_mode_selection(self):
        """Create the game mode selection frame"""
        mode_frame = tk.Frame(self.root, pady=10)
        mode_frame.pack()
        
        tk.Label(mode_frame, text="Game Mode:", font=('Arial', 12)).pack(side=tk.LEFT)
        
        self.mode_var = tk.IntVar(value=1)  # Default to single player
        tk.Radiobutton(mode_frame, text="Single Player", variable=self.mode_var, value=1, 
                       command=self.change_mode).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(mode_frame, text="Multiplayer", variable=self.mode_var, value=2, 
                       command=self.change_mode).pack(side=tk.LEFT, padx=10)
        
        # Player selection for single player mode
        self.player_choice_frame = tk.Frame(self.root, pady=5)
        self.player_choice_frame.pack()
        
        tk.Label(self.player_choice_frame, text="Play as:", font=('Arial', 12)).pack(side=tk.LEFT)
        
        self.player_var = tk.IntVar(value=1)  # Default to play first
        tk.Radiobutton(self.player_choice_frame, text="First (X)", variable=self.player_var, value=1).pack(side=tk.LEFT, padx=10)
        tk.Radiobutton(self.player_choice_frame, text="Second (O)", variable=self.player_var, value=2).pack(side=tk.LEFT, padx=10)

    def create_game_board(self):
        """Create the 3x3 game board with buttons"""
        self.board_frame = tk.Frame(self.root)
        self.board_frame.pack(pady=10)
        
        for i in range(9):
            button = tk.Button(self.board_frame, text="", width=5, height=2, font=('Arial', 24),
                              command=lambda idx=i: self.on_button_click(idx))
            button.grid(row=i//3, column=i%3, padx=2, pady=2)
            self.buttons.append(button)

    def create_status_bar(self):
        """Create the status bar to display game information"""
        self.status_frame = tk.Frame(self.root, pady=5)
        self.status_frame.pack()
        
        self.status_label = tk.Label(self.status_frame, text="Start a new game", font=('Arial', 12))
        self.status_label.pack()

    def create_control_buttons(self):
        """Create control buttons for the game"""
        control_frame = tk.Frame(self.root, pady=10)
        control_frame.pack()
        
        tk.Button(control_frame, text="New Game", command=self.reset_game, 
                 font=('Arial', 12)).pack(side=tk.LEFT, padx=10)
        tk.Button(control_frame, text="Exit", command=self.root.quit, 
                 font=('Arial', 12)).pack(side=tk.LEFT, padx=10)

    def change_mode(self):
        """Handle the change of game mode"""
        self.game_mode = self.mode_var.get()
        self.reset_game()

    def reset_game(self):
        """Reset the game to its initial state"""
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.game_over = False
        
        # Reset all buttons
        for button in self.buttons:
            button.config(text="", state=tk.NORMAL, bg="SystemButtonFace")
        
        # Set up game based on selected mode
        if self.game_mode == 1:  # Single player
            player_choice = self.player_var.get()
            self.player_turn = (player_choice == 1)  # player goes first if they chose 1
            
            if not self.player_turn:  # Computer goes first
                self.status_label.config(text="Computer's turn (O)")
                self.root.after(500, self.computer_move)
            else:
                self.status_label.config(text="Your turn (X)")
        else:  # Multiplayer
            self.player_turn = True  # X always goes first in multiplayer
            self.status_label.config(text="Player X's turn")

    def on_button_click(self, index):
        """Handle button clicks on the game board"""
        if self.game_over or self.board[index] != 0:
            return
        
        if self.game_mode == 1:  # Single player mode
            if self.player_turn:
                self.make_move(index, -1)  # Player plays as X (-1)
                if not self.check_game_end():
                    self.player_turn = False
                    self.status_label.config(text="Computer's turn (O)")
                    self.root.after(500, self.computer_move)
        else:  # Multiplayer mode
            if self.player_turn:
                self.make_move(index, -1)  # Player X plays (-1)
                if not self.check_game_end():
                    self.player_turn = False
                    self.status_label.config(text="Player O's turn")
            else:
                self.make_move(index, 1)  # Player O plays (1)
                if not self.check_game_end():
                    self.player_turn = True
                    self.status_label.config(text="Player X's turn")

    def make_move(self, index, player):
        """Make a move on the board for the specified player"""
        self.board[index] = player
        
        # Update button appearance
        if player == -1:  # X
            self.buttons[index].config(text="X", disabledforeground="blue")
        else:  # O
            self.buttons[index].config(text="O", disabledforeground="red")
            
        self.buttons[index].config(state=tk.DISABLED)

    def computer_move(self):
        """Let the computer make its move using the alpha-beta algorithm"""
        if self.game_over:
            return
            
        # Find the best move using alpha-beta pruning
        best_pos = self.find_best_move()
        self.make_move(best_pos, 1)  # Computer plays as O (1)
        
        if not self.check_game_end():
            self.player_turn = True
            self.status_label.config(text="Your turn (X)")

    def find_best_move(self):
        """Find the best move for the computer using alpha-beta pruning"""
        best_value = -float('inf')
        best_pos = -1
        
        for i in range(9):
            if self.board[i] == 0:  # Empty cell
                self.board[i] = 1  # Try placing O
                # Call alpha-beta with initial alpha=-infinity, beta=infinity
                move_value = self.alpha_beta(self.board, 0, False, -float('inf'), float('inf'))
                self.board[i] = 0  # Undo the move
                
                if move_value > best_value:
                    best_value = move_value
                    best_pos = i
                    
        return best_pos
                
    def alpha_beta(self, board, depth, is_maximizing, alpha, beta):
        """Implementation of alpha-beta pruning algorithm"""
        # Check if there's a winner
        result = self.analyze_board(board)
        
        if result != 0:
            return result
            
        # Check if it's a draw
        if 0 not in board:
            return 0
            
        if is_maximizing:  # Computer's turn (maximizing)
            best_value = -float('inf')
            for i in range(9):
                if board[i] == 0:
                    board[i] = 1  # Computer plays O (1)
                    value = self.alpha_beta(board, depth+1, False, alpha, beta)
                    board[i] = 0  # Undo move
                    best_value = max(best_value, value)
                    
                    # Alpha-beta pruning
                    alpha = max(alpha, best_value)
                    if beta <= alpha:
                        break  # Beta cutoff
                        
            return best_value
        else:  # Player's turn (minimizing)
            best_value = float('inf')
            for i in range(9):
                if board[i] == 0:
                    board[i] = -1  # Player plays X (-1)
                    value = self.alpha_beta(board, depth+1, True, alpha, beta)
                    board[i] = 0  # Undo move
                    best_value = min(best_value, value)
                    
                    # Alpha-beta pruning
                    beta = min(beta, best_value)
                    if beta <= alpha:
                        break  # Alpha cutoff
                        
            return best_value

    def analyze_board(self, board):
        """Check if there's a winner in the current board state"""
        # Check winning combinations
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combos:
            if board[combo[0]] != 0 and board[combo[0]] == board[combo[1]] == board[combo[2]]:
                return board[combo[0]]  # Return the winner (1 for O, -1 for X)
                
        return 0  # No winner yet

    def check_game_end(self):
        """Check if the game has ended and update UI accordingly"""
        result = self.analyze_board(self.board)
        
        # Check for winner
        if result != 0:
            winner = "O" if result == 1 else "X"
            self.highlight_winning_combination()
            self.status_label.config(text=f"Player {winner} wins!")
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            self.game_over = True
            return True
            
        # Check for draw
        if 0 not in self.board:
            self.status_label.config(text="It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
            self.game_over = True
            return True
            
        return False

    def highlight_winning_combination(self):
        """Highlight the winning combination of cells"""
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combos:
            if (self.board[combo[0]] != 0 and 
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                # Highlight these buttons
                for idx in combo:
                    self.buttons[idx].config(bg="light green")
                break

    def show_about(self):
        """Show information about the game"""
        messagebox.showinfo("About Tic-Tac-Toe", 
                           "Tic-Tac-Toe Game with Alpha-Beta Pruning AI\n\n" +
                           "Single Player: Play against the computer\n" +
                           "Multiplayer: Play against another person\n\n" +
                           "Created with Python and Tkinter")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()