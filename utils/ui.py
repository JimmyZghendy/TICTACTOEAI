import tkinter as tk
from tkinter import messagebox

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

def show_about(self):
    """Show information about the game"""
    messagebox.showinfo("About Tic-Tac-Toe", 
                        "Tic-Tac-Toe Game with Alpha-Beta Pruning AI\n\n" +
                        "Single Player: Play against the computer\n" +
                        "Multiplayer: Play against another person\n\n" +
                        "Created with Python and Tkinter")
