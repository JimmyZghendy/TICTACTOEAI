class AIEngine:

    def __init__(self, game_engine ):
        self.game_engine  = game_engine

    def find_best_move(self):
        best_value = -float('inf')
        best_pos = -1

        for i in range(9):
            if self.game_engine .board[i] == 0:  # Empty cell
                self.game_engine .board[i] = 1  # Try placing O
                move_value = self.minimax(self.game_engine .board, 0, False)
                self.game_engine .board[i] = 0  # Undo the move

                if move_value > best_value:
                    best_value = move_value
                    best_pos = i

        return best_pos, best_value

    def minimax(self, board, depth, is_maximizing):
        # Check if there's a winner
        result = self.game_engine .analyze_board(board)

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
                    value = self.minimax(board, depth+1, False)
                    board[i] = 0  # Undo move
                    best_value = max(best_value, value)
            return best_value
        else:  # Player's turn (minimizing)
            best_value = float('inf') 
            for i in range(9):
                if board[i] == 0:
                    board[i] = -1  # Player plays X (-1)
                    value = self.minimax(board, depth+1, True)
                    board[i] = 0  # Undo move
                    best_value = min(best_value, value)
            return best_value