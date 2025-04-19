<<<<<<< HEAD
# 🎮 Tic-Tac-Toe with AI 🎲

## 📝 Overview

This is a fully-featured Tic-Tac-Toe game with a graphical user interface built using Python and Tkinter. The game includes two AI implementation options:
=======
Project Info407: A Tic-Tac-Toe is a 2 player game, who take turns marking the spaces in a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game. 

To do to complete this project:
- Apply with graphical interface.
- Apply algorithm alphaBeta with choice 1 for MinMax and alphaBeta.
  
Tic-Tac-Toe.py is the python implementation of the game. 
There are two modes to play:
<ul>
 <li>Single Player (Against Computer)</li>
 <li>2 Players</li>
</ul>
>>>>>>> 53092c78770fbd08d94726de0d3e246090dc26df

1. **MiniMax.py** - Classic minimax algorithm implementation
2. **AlphaBeta.py** - Enhanced minimax with alpha-beta pruning for improved performance

## ✨ Features

- 🎯 **Two Game Modes**:
  - 👤 Single Player - Test your skills against an AI that never makes mistakes
  - 👥 Multiplayer - Play with a friend on the same computer

- 🎭 **Player Options**:
  - 🥇 Play as X (first) or O (second) in single player mode
  - 🔄 Easily switch between game modes

- 🧠 **Two AI Implementation Options**:
  - 🤖 **MiniMax.py** - Classic recursive algorithm that explores all possible game states
  - ⚡ **AlphaBeta.py** - Optimized algorithm that prunes unnecessary branches for faster decisions

- 🎨 **User-Friendly Interface**:
  - Clean, intuitive design
  - Visual feedback for game status
  - Winning combinations get highlighted

## 🚀 How to Run

1. Make sure you have Python installed (3.6 or newer)
2. The game uses Tkinter which comes pre-installed with most Python installations
3. Run either implementation:
   ```
   python MiniMax.py    # For the classic minimax AI
   ```
   OR
   ```
   python AlphaBeta.py  # For the faster alpha-beta pruning AI
   ```

## 🧩 Comparing the AI Implementations

- **MiniMax.py**
  - 📊 Explores the entire game tree
  - 🧮 Makes optimal decisions but may be slower
  - 💻 Simpler implementation to understand

- **AlphaBeta.py**
  - ⚡ Much faster, especially for the opening moves
  - 🎯 Makes identical decisions to minimax
  - 🔍 Intelligently skips evaluating branches that won't affect the final decision

## 🎮 How to Play

1. Launch either version of the game
2. Select your preferred game mode (Single Player or Multiplayer)
3. In Single Player mode, choose whether to play first (X) or second (O)
4. Click on any empty cell to make your move
5. In Single Player mode, the AI will automatically respond
6. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins
7. If all cells are filled with no winner, the game ends in a draw

## 🧩 Game Controls

- **Mouse**: Click on any empty cell to place your mark
- **New Game Button**: Start a fresh game with current settings
- **Exit Button**: Close the game
- **Game Menu**: Access additional options

## 💻 Technical Details

- **Programming Language**: Python 3
- **GUI Framework**: Tkinter
- **AI Algorithms**:
  - Minimax (MiniMax.py)
  - Alpha-Beta Pruning (AlphaBeta.py)
- **Board Representation**: List with values 0 (empty), 1 (O), and -1 (X)

## 🤔 Strategy Tips

- 🎯 Corner cells (particularly the first move) are strategically strong positions
- 🛡️ Block your opponent's potential winning moves
- 🏆 Against either AI implementation, a draw is the best possible outcome with perfect play

## 🔍 Code Structure

- **`__init__`**: Sets up the game window and initializes variables
- **UI Creation Methods**: Build the interface components
- **Game Logic Methods**: Handle player actions and game state
- **AI Methods**: 
  - **MiniMax.py**: `minimax()` implements the standard algorithm
  - **AlphaBeta.py**: `alpha_beta()` implements the optimized version

## 🛠️ Customization

Feel free to modify the code to customize:
- 🎨 Colors and appearance
- 💪 AI difficulty (by limiting the search depth)
- 🏆 Add score tracking between games
- 🔊 Add sound effects

## ⚠️ Known Issues

- The standard minimax algorithm can be slow on first move (evaluating all possible game trees)
- Window size is fixed and may not adapt well to all screen resolutions

## 📜 License

This project is open source and available under the MIT License.

## 👏 Acknowledgments

- Original terminal-based implementation adapted to GUI
- Minimax and Alpha-Beta pruning algorithms implemented for perfect AI play

---

Enjoy the game! 🎮