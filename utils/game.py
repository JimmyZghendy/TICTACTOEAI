class GameLogic:

    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # 0: empty // 1: O // -1: X
        self.game_over = False

    def reset_board(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.game_over = False

    def is_valid_move(self, index):
        return not self.game_over and self.board[index] == 0

    def make_move(self, index, player):
        if self.is_valid_move(index):
            self.board[index] = player
            return True
        return False

    def analyze_board(self, board=None):
        if board is None:
            board = self.board

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
        result = self.analyze_board()

        if result != 0:
            self.game_over = True
            return {'status': 'win', 'winner': result}

        if 0 not in self.board:
            self.game_over = True
            return {'status': 'draw'}

        return {'status': 'ongoing'}

    def get_winning_combination(self):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combo in winning_combos:
            if (self.board[combo[0]] != 0 and
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                return combo
        return None