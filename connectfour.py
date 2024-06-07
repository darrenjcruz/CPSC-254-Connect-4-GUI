# Author: Angel Armendariz, Darren Cruz, Spencer Price
# Emails: angelarmendariz@csu.fullerton.edu, darrencruz@csu.fullerton.edu, spencerprice@csu.fullerton.edu

'''
This module contains the ConnectFour class which includes the game logic
that is needed to play a game of Connect Four.
'''

import collections

# Game Piece Constants

NONE = ' '
RED = 'R'
YELLOW = 'Y'

# Game Board Size Constants

BOARD_COLUMNS = 7
BOARD_ROWS = 6

class ConnectFour:
    '''
    ConnectFour class that contains the necessary game logic for Connect
    Four.
    '''

    def __init__(self):
        self.board = self._new_game_board()
        self.turn = RED
        self.winner = NONE

    # Public Functions

    def print_board(self) -> str:
        '''
        Prints the board as a visual display.
        '''
        num = ''
        for x in range(BOARD_COLUMNS):
            num += str(x+1)
        print('\n\t' + ' '.join(num))

        for row in range(BOARD_ROWS):
            bRow = ''
            for col in range(BOARD_COLUMNS):
                if self.board[col][row] == ' ':
                    bRow += '.'
                elif self.board[col][row] == RED:
                    bRow += RED
                elif self.board[col][row] == YELLOW:
                    bRow += YELLOW
            print ('\t' + ' '.join(bRow))

    def game(self):
        '''
        Runs a game of ConnectFour
        '''
        while True:
            self.print_board()
            self.winning_player()
            if self.winner != NONE or self._any_valid_moves_left() == False:
                self.endgame_statement()
                break
            else:
                self.move()

    def menu(self):
        '''
        Presents a menu for the user to navigate through.
        '''
        print("\nWelcome to ConnectFour!\n")
        while True:
            menu = "\nPlease choose one of the following options:\n" + \
                    "G:  Play a game\n" + \
                    "X:  Exit\n\n" + \
                    "Input: "
            menuChoice = str(input(menu).strip().upper())

            match menuChoice:
                case "G":
                    self.game()
                case "X":
                    print("\nThank you for playing!")
                    break
                case _:
                    print("Please input a valid menu choice.")          

    def move(self):
        '''
        Asks the user for a column to drop a piece in and drops a piece.
        '''
        move = False
        while move == False:
            try:
                column = int(input('\n{} Player: Please enter a column number to drop a piece\n'.format(self.turn)).strip())
                self.drop(column - 1)
            except ValueError:
                print("Please input an integer value.")
            except InvalidMoveError:
                print("That is an invalid move. Please try another column.")
            else:
                move = True

    def endgame_statement(self):
        '''
        Prints an endgame statement; prints the winner if there is one,
        otherwise prints 'Draw'.
        '''
        if self.winner == RED or self.winner == YELLOW:
            print("\nCongratulations! The winner is: {}".format(self.winner))
        else:
            print("It's a Draw!")

    def reset(self):
        '''
        Resets the game; empty game board and Red player starts again.
        '''
        self.board = self._new_game_board()
        self.turn = RED
        self.winner = NONE

    def drop(self, column_number: int):
        '''
        Drops a color piece of the current player's color in the chosen
        column.
        '''
        #these will raise errors if found
        self._require_valid_column_number(column_number)
        self._require_game_not_over()

        empty_row = self._find_bottom_empty_row_in_column(column_number)
        if empty_row == -1:
            raise InvalidMoveError()
        else:
            self.board[column_number][empty_row] = self.turn
            self.turn = self._opposite_turn()

    def winning_player(self):
        '''
        Determines the winning player in the current board, if any. If the
        red player has won, RED is returned; if the yellow player has won,
        YELLOW is returned; if no player has won yet, NONE is returned.
        '''
        for col in range(BOARD_COLUMNS):
            for row in range(BOARD_ROWS):
                if self._winning_sequence_begins_at(col, row):
                    if self.winner == NONE:
                        self.winner = self.board[col][row]

    # Private Functions

    def _new_game_board(self) -> [[str]]:
        '''
        Creates a new game board; An empty game board of size BOARD_COLUMNS
        x BOARD_ROWS.
        '''
        board = []

        for col in range(BOARD_COLUMNS):
            board.append([])
            for row in range(BOARD_ROWS):
                board[-1].append(NONE)

        return board

    def _copy_game_board(self) -> [[str]]:
        '''
        Copies the given game board.
        '''
        board_copy = []

        for col in range(BOARD_COLUMNS):
            board_copy.append([])
            for row in range(BOARD_ROWS):
                board_copy[-1].append(self.board[col][row])

        return board_copy

    def _find_bottom_empty_row_in_column(self, col: int) -> int:
        '''
        Determines the bottommost empty row within a given column. If the
        entire column is filled with pieces, returns -1.
        '''
        for i in range(BOARD_ROWS -1, -1, -1):
            if self.board[col][i] == NONE:
                return i

        return -1

    def _opposite_turn(self) -> str:
        '''
        Given the current player, returns the opposite player.
        '''
        if self.turn == RED:
            return YELLOW
        else:
            return RED

    def _winning_sequence_begins_at(self, col: int, row: int) -> bool:
        '''
        Returns True if a winning sequence of pieces appears on the board
        in the given column & row. returns False otherwise.
        '''
        return self._four_in_a_row(col, row, 0, 1) \
               or self._four_in_a_row(col, row, 1, 1) \
               or self._four_in_a_row(col, row, 1, 0) \
               or self._four_in_a_row(col, row, 1, -1) \
               or self._four_in_a_row(col, row, 0, -1) \
               or self._four_in_a_row(col, row, -1, -1) \
               or self._four_in_a_row(col, row, -1, 0) \
               or self._four_in_a_row(col, row, -1, 1)

    def _four_in_a_row(self, col: int, row: int, coldelta: int, rowdelta: int) -> bool:
        '''
        Returns True if a winning sequence of pieces appears on the board
        begining in the given column and row and extending in a direction
        specified by the coldelta and rowdelta
        '''

        start_cell = self.board[col][row]

        if start_cell == NONE:
            return False
        else:
            for i in range(1, 4):
                if not self._is_valid_column_number(col + coldelta * i) \
                        or not self._is_valid_row_number(row + rowdelta * i) \
                        or self.board[col + coldelta * i][row + rowdelta * i] != start_cell:
                    return False
            return True

    def _require_valid_column_number(self, col: int) -> None:
        '''
        Raises a ValueError if the column number is not a valid column
        number.
        '''
        if type(col) != int or not self._is_valid_column_number(col):
            raise ValueError('column_number must be int between 0 and {}'.format(BOARD_COLUMNS - 1))

    def _require_game_not_over(self) -> None:
        '''
        Raises a GameOverError if the given game state represents a
        situation where the game is over (i.e., there is a winning player).
        '''
        if self.winner != NONE:
            raise GameOverError()
        elif self.winner == NONE and self._any_valid_moves_left() == False:
            raise GameOverError()

    def _is_valid_column_number(self, column_number: int) -> bool:
        '''
        Returns True if the given column number is valid; returns False
        otherwise.
        '''
        return 0 <= column_number < BOARD_COLUMNS

    def _is_valid_row_number(self, row_number: int) -> bool:
        '''
        Returns True if the given row number is valid; returns False
        otherwise.
        '''
        return 0 <= row_number < BOARD_ROWS

    def _any_valid_moves_left(self) -> bool:
        '''
        Returns True if there are still valid moves left; returns False
        otherwise.
        '''
        for col in range(BOARD_COLUMNS):
            if self._find_bottom_empty_row_in_column(col) != -1:
                return True

        return False

# Exceptions

class InvalidMoveError(Exception):
    '''
    Raised whenever an invalid move is made.
    '''
    pass

class GameOverError(Exception):
    '''
    Raised whenever an attempt is made to make a move after the game is
    already over.
    '''
    pass