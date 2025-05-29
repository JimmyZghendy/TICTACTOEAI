import sys
import os
import time
import tkinter as tk
from tkinter import messagebox
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.ui import create_menu, create_mode_selection, create_game_board, create_status_bar, create_control_buttons, show_about
from utils.game_engine import GameLogic
from ai_engine import AIEngine

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game")
        self.root.resizable(False, False)

        # Initialize game components
        self.game_engine = GameLogic()
        self.ai_engine = AIEngine(self.game_engine)

        self.buttons = []
        self.game_mode = 1  # Default: 1 for single player, 2 for multiplayer
        self.player_turn = True  # True if it's player's turn in single player mode

        # AI timing variables
        self.ai_move_times = []  # Store all AI move times
        self.current_move_start_time = None

        # Create the UI
        create_menu(self)
        create_mode_selection(self)
        create_game_board(self)
        create_status_bar(self)
        create_control_buttons(self)

    def change_mode(self):
        self.game_mode = self.mode_var.get()
        self.reset_game()

    def reset_game(self):
        self.game_engine.reset_board()

        # Reset AI timing data
        self.ai_move_times = []
        self.current_move_start_time = None

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
        if not self.game_engine.is_valid_move(index):
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
        if self.game_engine.make_move(index, player):
            if player == -1:  # X
                self.buttons[index].config(text="X", disabledforeground="blue")
            else:  # O
                self.buttons[index].config(text="O", disabledforeground="red")
            self.buttons[index].config(state=tk.DISABLED)

    def computer_move(self):
        if self.game_engine.game_over:
            return

        start_time = time.time()
        best_pos, _ = self.ai_engine.find_best_move()

        end_time = time.time()
        move_duration = end_time - start_time

        self.ai_move_times.append(move_duration)
        print(f"AI move {len(self.ai_move_times)}: {move_duration:.4f} seconds")

        self.make_move(best_pos, 1)  # Computer plays as O (1)

        if not self.check_game_end():
            self.player_turn = True
            self.status_label.config(text="Your turn (X)")

    def check_game_end(self):
        """Check if the game has ended and update UI accordingly"""
        result = self.game_engine.check_game_end()

        if result['status'] == 'win':
            winner = "O" if result['winner'] == 1 else "X"
            self.highlight_winning_combination()
            self.status_label.config(text=f"Player {winner} wins!")
            
            # Print AI timing statistics if there were AI moves
            self.print_ai_timing_stats()
            
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            return True
        elif result['status'] == 'draw':
            self.status_label.config(text="It's a draw!")
            
            # Print AI timing statistics if there were AI moves
            self.print_ai_timing_stats()
            
            messagebox.showinfo("Game Over", "It's a draw!")
            return True
        
        return False

    def print_ai_timing_stats(self):
        if self.ai_move_times and self.game_mode == 1:  # Only for single player mode
            total_time = sum(self.ai_move_times)
            average_time = total_time / len(self.ai_move_times)
            print(f"\n--- Round Finished ---")
            print(f"Average time per move: {average_time:.4f} seconds\n")

    def highlight_winning_combination(self):
        winning_combo = self.game_engine.get_winning_combination()
        if winning_combo:
            for idx in winning_combo:
                self.buttons[idx].config(bg="light green")

    def show_about(self):
        show_about()

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()