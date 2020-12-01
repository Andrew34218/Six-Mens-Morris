import math
from IPython.display import clear_output

# Board array
board = [["0" for tj in range(4)] for ti in range(5)]
board[0][3], board[1][3], board[3][3], board[4][3] = "Q", "Q", "Q", "Q"

player_turn = "1"
max_depth = 4

locations = ["OTL", "OTM", "OTR", "OML", "OBL", "OBM", "OBR", "OMR",
             "ITL", "ITM", "ITR", "IML", "IMR", "IBL", "IBM", "IBR"]

# Function to print the board
def print_board(board):
    clear_output()
    print("{}---------{}---------{}".format(board[0][0], board[0][1], board[0][2]))
    print("|         |         |")
    print("|     {}---{}---{}     |".format(board[1][0], board[1][1], board[1][2]))
    print("|     |       |     |")
    print("{}-----{}       {}-----{}".format(board[2][0], board[2][1], board[2][2], board[2][3]))
    print("|     |       |     |")
    print("|     {}---{}---{}     |".format(board[3][0], board[3][1], board[3][2]))
    print("|         |         |")
    print("{}---------{}---------{}".format(board[4][0], board[4][1], board[4][2]))


# Function to find placement for the user
def placement(user_input):
    if user_input == "OTL":
        return [0, 0]
    if user_input == "OTM":
        return [0, 1]
    if user_input == "OTR":
        return [0, 2]
    if user_input == "OML":
        return [2, 0]
    if user_input == "OBL":
        return [4, 0]
    if user_input == "OBM":
        return [4, 1]
    if user_input == "OBR":
        return [4, 2]
    if user_input == "OMR":
        return [2, 3]
    if user_input == "ITL":
        return [1, 0]
    if user_input == "ITM":
        return [1, 1]
    if user_input == "ITR":
        return [1, 2]
    if user_input == "IML":
        return [2, 1]
    if user_input == "IMR":
        return [2, 2]
    if user_input == "IBL":
        return [3, 0]
    if user_input == "IBM":
        return [3, 1]
    if user_input == "IBR":
        return [3, 2]


# Function to change turn of players
def change_turn():
    global player_turn
    if player_turn == '2':
        player_turn = '1'
    else:
        player_turn = '2'


# Function to check if a player has connected three pieces
def test_connect(cur):
    # Check for a connection of 3 in outer rows
    if cur[0][0] == cur[0][1] and cur[0][1] == cur[0][2] and cur[0][0] != "0":
        return cur[0][0]
    if cur[4][0] == cur[4][1] and cur[4][1] == cur[4][2] and cur[4][0] != "0":
        return cur[4][0]

    # Check for a connection of 3 in inner rows
    if cur[1][0] == cur[1][1] and cur[1][1] == cur[1][2] and cur[1][0] != "0":
        return cur[1][0]
    if cur[3][0] == cur[3][1] and cur[3][1] == cur[3][2] and cur[3][0] != "0":
        return cur[3][0]

    # Check for a connection of 3 in outer columns
    if cur[0][0] == cur[2][0] and cur[2][0] == cur[4][0] and cur[0][0] != "0":
        return cur[0][0]
    if cur[0][2] == cur[2][3] and cur[2][3] == cur[4][2] and cur[0][2] != "0":
        return cur[0][2]

    # Check for a connection of 3 in inner columns
    if cur[1][0] == cur[2][1] and cur[2][1] == cur[3][0] and cur[1][0] != "0":
        return cur[1][0]
    if cur[1][2] == cur[2][2] and cur[2][2] == cur[3][2] and cur[1][2] != "0":
        return cur[1][2]


def check_connect(cur):
    # check if X won
    if test_connect(cur) == '1':
        print("Player 1 has made a connection")
        return True
    # check if O won
    if test_connect(cur) == '2':
        print("Player 2 has made a connection")
        return True
    return False


# MiniMax Algorithm
def eval_state(cur):
    s1 = 0
    s2 = 0

    # Check for a connection of 3 in outer rows
    if cur[0][0] in ['0', '1'] and cur[0][1] in ['0', '1'] and cur[0][2] in ['0', '1']:
        s1 += 1
    if cur[0][0] in ['0', '2'] and cur[0][1] in ['0', '2'] and cur[0][2] in ['0', '2']:
        s2 += 1
    if cur[4][0] in ['0', '1'] and cur[4][1] in ['0', '1'] and cur[4][2] in ['0', '1']:
        s1 += 1
    if cur[4][0] in ['0', '2'] and cur[4][1] in ['0', '2'] and cur[4][2] in ['0', '2']:
        s2 += 1

    # Check for a connection of 3 in inner rows
    if cur[1][0] in ['0', '1'] and cur[1][1] in ['0', '1'] and cur[1][2] in ['0', '1']:
        s1 += 1
    if cur[1][0] in ['0', '2'] and cur[1][1] in ['0', '2'] and cur[1][2] in ['0', '2']:
        s2 += 1
    if cur[3][0] in ['0', '1'] and cur[3][1] in ['0', '1'] and cur[3][2] in ['0', '1']:
        s1 += 1
    if cur[3][0] in ['0', '2'] and cur[3][1] in ['0', '2'] and cur[3][2] in ['0', '2']:
        s2 += 1

    # Check for a connection of 3 in outer columns
    if cur[0][0] in ['0', '1'] and cur[2][0] in ['0', '1'] and cur[4][0] in ['0', '1']:
        s1 += 1
    if cur[0][0] in ['0', '2'] and cur[2][0] in ['0', '2'] and cur[4][0] in ['0', '2']:
        s2 += 1
    if cur[0][2] in ['0', '1'] and cur[2][3] in ['0', '1'] and cur[4][2] in ['0', '1']:
        s1 += 1
    if cur[0][2] in ['0', '2'] and cur[2][3] in ['0', '2'] and cur[4][2] in ['0', '2']:
        s2 += 1

    # Check for a connection of 3 in inner columns
    if cur[1][0] in ['0', '1'] and cur[2][1] in ['0', '1'] and cur[3][0] in ['0', '1']:
        s1 += 1
    if cur[1][0] in ['0', '2'] and cur[2][1] in ['0', '2'] and cur[3][0] in ['0', '2']:
        s2 += 1
    if cur[1][2] in ['0', '1'] and cur[2][2] in ['0', '1'] and cur[3][2] in ['0', '1']:
        s1 += 1
    if cur[1][2] in ['0', '2'] and cur[2][2] in ['0', '2'] and cur[3][2] in ['0', '2']:
        s2 += 1

    return s1 - s2


# The main function
def minimax_decision(cur):
    # check the Max value for all possible actions
    max_val = -math.inf
    action_I = 0
    action_J = 0
    s = 0
    n = 0
    if count < 12:
        for i in range(5):
            for j in range(4):
                if cur[i][j] == '0':  # it is a possible action
                    # create the nextState and send it to MinValue
                    next_state = [[cur[ti][tj] for tj in range(4)] for ti in range(5)]
                    next_state[0][3], next_state[1][3], next_state[3][3], next_state[4][3] = "Q", "Q", "Q", "Q"
                    next_state[i][j] = '2'
                    val = min_value(next_state, -math.inf, math.inf, max_depth, s, n)
                    if val > max_val:
                        max_val = val
                        action_I = i
                        action_J = j
                # if count >= 12:
    if count >= 12:
        for i in range(5):
            for j in range(4):
                if cur[i][j] == '2':  # It is a possible action
                    next_state, s, n = is_valid_move_ai(cur, i, j, s, n)
                    val = min_value(next_state, -math.inf, math.inf, max_depth, s, n)
                    if val > max_val:
                        max_val = val
                        action_I = i
                        action_J = j

    # return the action that maximizes the output
    return action_I, action_J, s, n
    # v ← Max-Value (state)


# return the action in successors(state) with value v
def max_value(cur, alpha, beta, depth, s, n):
    # we have 3 terminal states: X O Draw
    if test_connect(cur) == '2':
        return 10
    if test_connect(cur) == '1':
        return -10
    if depth == 0:
        return eval_state(cur)
    # check the Max value for all possible actions
    max_val = -math.inf
    if count < 12:
        for i in range(5):
            for j in range(4):
                if cur[i][j] == '0':  # it is a possible action
                    # create the nextState and send it to MinValue
                    next_state = [[cur[ti][tj] for tj in range(4)] for ti in range(5)]
                    next_state[0][3], next_state[1][3], next_state[3][3], next_state[4][3] = "Q", "Q", "Q", "Q"
                    next_state[i][j] = '2'
                    val = min_value(next_state, alpha, beta, depth - 1, s, n)
                    if val > max_val:
                        max_val = val
                    if val >= beta:
                        return val
                    if val > alpha:
                        alpha = val
    if count >= 12:
        for i in range(5):
            for j in range(4):
                if cur[i][j] == '2':  # It is a possible action
                    next_state, s, n = is_valid_move_ai(cur, i, j, s, n)
                    val = min_value(next_state, alpha, beta, depth - 1, s, n)
                    if val < max_val:
                        max_val = val
                    if val >= beta:
                        return val
                    if val > alpha:
                        alpha = val
    return max_val


def min_value(cur, alpha, beta, depth, s, n):
    # we have 3 terminal states: X O Draw
    if test_connect(cur) == '2':
        return 10
    if test_connect(cur) == '1':
        return -10
    if depth == 0:
        return eval_state(cur)
    # check the Max value for all possible actions
    min_val = math.inf
    if count < 12:
        for i in range(5):
            for j in range(4):
                if cur[i][j] == '0':  # it is a possible action
                    # create the nextState and send it to MinValue
                    next_state = [[cur[ti][tj] for tj in range(4)] for ti in range(5)]
                    next_state[0][3], next_state[1][3], next_state[3][3], next_state[4][3] = "Q", "Q", "Q", "Q"
                    next_state[i][j] = '1'
                    val = max_value(next_state, alpha, beta, depth - 1, s, n)
                    if val < min_val:
                        min_val = val
                    if val <= alpha:
                        return val
                    if val < beta:
                        beta = val
    if count >= 12:
        for i in range(5):
            for j in range(4):
                if cur[i][j] == '1':  # It is a possible action
                    next_state, s, n = is_valid_move_human(cur, i, j, s, n)
                    val = max_value(next_state, alpha, beta, depth - 1, s, n)
                    if val < min_val:
                        min_val = val
                    if val <= alpha:
                        return val
                    if val < beta:
                        beta = val
    return min_val


def is_valid_move_ai(cur, i, j, s, n):
    next_state = [[cur[ti][tj] for tj in range(4)] for ti in range(5)]
    next_state[0][3], next_state[1][3], next_state[3][3], next_state[4][3] = "Q", "Q", "Q", "Q"

    # can move up
    # column 1
    if i == 4 and j == 0 and cur[2][0] == "0":
        next_state[i][j], next_state[2][0] = "0", "2"
        s, n = 2, 0
    if i == 2 and j == 0 and cur[0][0] == "0":
        next_state[i][j], next_state[0][0] = "0", "2"
        s, n = 0, 0
    # column 2
    if i == 3 and j == 0 and cur[2][1] == "0":
        next_state[i][j], next_state[2][1] = "0", "2"
        s, n = 2, 1
    if i == 2 and j == 1 and cur[1][0] == "0":
        next_state[i][j], next_state[1][0] = "0", "2"
        s, n = 1, 0
    # column 3
    if i == 4 and j == 1 and cur[3][1] == "0":
        next_state[i][j], next_state[3][1] = "0", "2"
        s, n = 3, 1
    if i == 1 and j == 1 and cur[0][1] == "0":
        next_state[i][j], next_state[0][1] = "0", "2"
        s, n = 0, 1
    # column 4
    if i == 3 and j == 2 and cur[2][2] == "0":
        next_state[i][j], next_state[2][2] = "0", "2"
        s, n = 2, 2
    if i == 2 and j == 2 and cur[1][2] == "0":
        next_state[i][j], next_state[1][2] = "0", "2"
        s, n = 1, 2
    # column 5
    if i == 4 and j == 2 and cur[2][3] == "0":
        next_state[i][j], next_state[2][3] = "0", "2"
        s, n = 2, 3
    if i == 2 and j == 3 and cur[0][2] == "0":
        next_state[i][j], next_state[0][2] = "0", "2"
        s, n = 0, 2
    # can move down
    # column 1
    if i == 2 and j == 0 and cur[4][0] == "0":
        next_state[i][j], next_state[4][0] = "0", "2"
        s, n = 4, 0
    if i == 0 and j == 0 and cur[2][0] == "0":
        next_state[i][j], next_state[2][0] = "0", "2"
        s, n = 2, 0
    # column 2
    if i == 2 and j == 1 and cur[3][0] == "0":
        next_state[i][j], next_state[3][0] = "0", "2"
        s, n = 3, 0
    if i == 1 and j == 0 and cur[2][1] == "0":
        next_state[i][j], next_state[2][1] = "0", "2"
        s, n = 2, 1
    # column 3
    if i == 3 and j == 1 and cur[4][1] == "0":
        next_state[i][j], next_state[4][1] = "0", "2"
        s, n = 4, 1
    if i == 0 and j == 1 and cur[1][1] == "0":
        next_state[i][j], next_state[1][1] = "0", "2"
        s, n = 1, 1
    # column 4
    if i == 2 and j == 2 and cur[3][2] == "0":
        next_state[i][j], next_state[3][2] = "0", "2"
        s, n = 3, 2
    if i == 1 and j == 2 and cur[2][2] == "0":
        next_state[i][j], next_state[2][2] = "0", "2"
        s, n = 2, 2
    # column 5
    if i == 2 and j == 3 and cur[4][2] == "0":
        next_state[i][j], next_state[4][2] = "0", "2"
        s, n = 4, 2
    if i == 0 and j == 2 and cur[2][3] == "0":
        next_state[i][j], next_state[2][3] = "0", "2"
        s, n = 2, 3
    # can move right
    # row 1
    if i == 0 and j == 0 and cur[0][1] == "0":
        next_state[i][j], next_state[0][1] = "0", "2"
        s, n = 0, 1
    if i == 0 and j == 1 and cur[0][2] == "0":
        next_state[i][j], next_state[0][2] = "0", "2"
        s, n = 0, 2
    # row 2
    if i == 1 and j == 0 and cur[1][1] == "0":
        next_state[i][j], next_state[1][1] = "0", "2"
        s, n = 1, 1
    if i == 1 and j == 1 and cur[1][2] == "0":
        next_state[i][j], next_state[1][2] = "0", "2"
        s, n = 1, 2
    # row 3
    if i == 2 and j == 0 and cur[2][1] == "0":
        next_state[i][j], next_state[2][1] = "0", "2"
        s, n = 2, 1
    if i == 2 and j == 2 and cur[2][3] == "0":
        next_state[i][j], next_state[2][3] = "0", "2"
        s, n = 2, 3
    # row 4
    if i == 3 and j == 0 and cur[3][1] == "0":
        next_state[i][j], next_state[3][1] = "0", "2"
        s, n = 3, 1
    if i == 3 and j == 1 and cur[3][2] == "0":
        next_state[i][j], next_state[3][2] = "0", "2"
        s, n = 3, 2
    # row 5
    if i == 4 and j == 0 and cur[4][1] == "0":
        next_state[i][j], next_state[4][1] = "0", "2"
        s, n = 4, 1
    if i == 4 and j == 1 and cur[4][2] == "0":
        next_state[i][j], next_state[4][2] = "0", "2"
        s, n = 4, 2
    # can move left
    # row 1
    if i == 0 and j == 1 and cur[0][0] == "0":
        next_state[i][j], next_state[0][0] = "0", "2"
        s, n = 0, 0
    if i == 0 and j == 2 and cur[0][1] == "0":
        next_state[i][j], next_state[0][1] = "0", "2"
        s, n = 0, 1
    # row 2
    if i == 1 and j == 1 and cur[1][0] == "0":
        next_state[i][j], next_state[1][0] = "0", "2"
        s, n = 1, 0
    if i == 1 and j == 2 and cur[1][1] == "0":
        next_state[i][j], next_state[1][1] = "0", "2"
        s, n = 1, 1
    # row 3
    if i == 2 and j == 1 and cur[2][0] == "0":
        next_state[i][j], next_state[2][0] = "0", "2"
        s, n = 2, 0
    if i == 2 and j == 3 and cur[2][2] == "0":
        next_state[i][j], next_state[2][2] = "0", "2"
        s, n = 2, 2
    # row 4
    if i == 3 and j == 1 and cur[3][0] == "0":
        next_state[i][j], next_state[3][0] = "0", "2"
        s, n = 3, 0
    if i == 3 and j == 2 and cur[3][1] == "0":
        next_state[i][j], next_state[3][1] = "0", "2"
        s, n = 3, 1
    # row 5
    if i == 4 and j == 1 and cur[4][0] == "0":
        next_state[i][j], next_state[4][0] = "0", "2"
        s, n = 4, 0
    if i == 4 and j == 2 and cur[4][1] == "0":
        next_state[i][j], next_state[4][1] = "0", "2"
        s, n = 4, 1
    return next_state, s, n


def is_valid_move_human(cur, i, j, s, n):
    next_state = [[cur[ti][tj] for tj in range(4)] for ti in range(5)]
    next_state[0][3], next_state[1][3], next_state[3][3], next_state[4][3] = "Q", "Q", "Q", "Q"

    # create next state and send to MinValue

    # can move up
    # column 1
    if i == 4 and j == 0 and cur[2][0] == "0":
        next_state[i][j], next_state[2][0] = "0", "1"
        s, n = 2, 0
    if i == 2 and j == 0 and cur[0][0] == "0":
        next_state[i][j], next_state[0][0] = "0", "1"
        s, n = 0, 0
    # column 2
    if i == 3 and j == 0 and cur[2][1] == "0":
        next_state[i][j], next_state[2][1] = "0", "1"
        s, n = 2, 1
    if i == 2 and j == 1 and cur[1][0] == "0":
        next_state[i][j], next_state[1][0] = "0", "1"
        s, n = 1, 0
    # column 3
    if i == 4 and j == 1 and cur[3][1] == "0":
        next_state[i][j], next_state[3][1] = "0", "1"
        s, n = 3, 1
    if i == 1 and j == 1 and cur[0][1] == "0":
        next_state[i][j], next_state[0][1] = "0", "1"
        s, n = 0, 1
    # column 4
    if i == 3 and j == 2 and cur[2][2] == "0":
        next_state[i][j], next_state[2][2] = "0", "1"
        s, n = 2, 2
    if i == 2 and j == 2 and cur[1][2] == "0":
        next_state[i][j], next_state[1][2] = "0", "1"
        s, n = 1, 2
    # column 5
    if i == 4 and j == 2 and cur[2][3] == "0":
        next_state[i][j], next_state[2][3] = "0", "1"
        s, n = 2, 3
    if i == 2 and j == 3 and cur[0][2] == "0":
        next_state[i][j], next_state[0][2] = "0", "1"
        s, n = 0, 2
    # can move down
    # column 1
    if i == 2 and j == 0 and cur[4][0] == "0":
        next_state[i][j], next_state[4][0] = "0", "1"
        s, n = 4, 0
    if i == 0 and j == 0 and cur[2][0] == "0":
        next_state[i][j], next_state[2][0] = "0", "1"
        s, n = 2, 0
    # column 2
    if i == 2 and j == 1 and cur[3][0] == "0":
        next_state[i][j], next_state[3][0] = "0", "1"
        s, n = 3, 0
    if i == 1 and j == 0 and cur[2][1] == "0":
        next_state[i][j], next_state[2][1] = "0", "1"
        s, n = 2, 1
    # column 3
    if i == 3 and j == 1 and cur[4][1] == "0":
        next_state[i][j], next_state[4][1] = "0", "1"
        s, n = 4, 1
    if i == 0 and j == 1 and cur[1][1] == "0":
        next_state[i][j], next_state[1][1] = "0", "1"
        s, n = 1, 1
    # column 4
    if i == 2 and j == 2 and cur[3][2] == "0":
        next_state[i][j], next_state[3][2] = "0", "1"
        s, n = 3, 2
    if i == 1 and j == 2 and cur[2][2] == "0":
        next_state[i][j], next_state[2][2] = "0", "1"
        s, n = 2, 2
    # column 5
    if i == 2 and j == 3 and cur[4][2] == "0":
        next_state[i][j], next_state[4][2] = "0", "1"
        s, n = 4, 2
    if i == 0 and j == 2 and cur[2][3] == "0":
        next_state[i][j], next_state[2][3] = "0", "1"
        s, n = 2, 3
    # can move right
    # row 1
    if i == 0 and j == 0 and cur[0][1] == "0":
        next_state[i][j], next_state[0][1] = "0", "1"
        s, n = 0, 1
    if i == 0 and j == 1 and cur[0][2] == "0":
        next_state[i][j], next_state[0][2] = "0", "1"
        s, n = 0, 2
    # row 2
    if i == 1 and j == 0 and cur[1][1] == "0":
        next_state[i][j], next_state[1][1] = "0", "1"
        s, n = 1, 1
    if i == 1 and j == 1 and cur[1][2] == "0":
        next_state[i][j], next_state[1][2] = "0", "1"
        s, n = 1, 2
    # row 3
    if i == 2 and j == 0 and cur[2][1] == "0":
        next_state[i][j], next_state[2][1] = "0", "1"
        s, n = 2, 1
    if i == 2 and j == 2 and cur[2][3] == "0":
        next_state[i][j], next_state[2][3] = "0", "1"
        s, n = 2, 3
    # row 4
    if i == 3 and j == 0 and cur[3][1] == "0":
        next_state[i][j], next_state[3][1] = "0", "1"
        s, n = 3, 1
    if i == 3 and j == 1 and cur[3][2] == "0":
        next_state[i][j], next_state[3][2] = "0", "1"
        s, n = 3, 2
    # row 5
    if i == 4 and j == 0 and cur[4][1] == "0":
        next_state[i][j], next_state[4][1] = "0", "1"
        s, n = 4, 1
    if i == 4 and j == 1 and cur[4][2] == "0":
        next_state[i][j], next_state[4][2] = "0", "1"
        s, n = 4, 2
    # can move left
    # row 1
    if i == 0 and j == 1 and cur[0][0] == "0":
        next_state[i][j], next_state[0][0] = "0", "1"
        s, n = 0, 0
    if i == 0 and j == 2 and cur[0][1] == "0":
        next_state[i][j], next_state[0][1] = "0", "1"
        s, n = 0, 1
    # row 2
    if i == 1 and j == 1 and cur[1][0] == "0":
        next_state[i][j], next_state[1][0] = "0", "1"
        s, n = 1, 0
    if i == 1 and j == 2 and cur[1][1] == "0":
        next_state[i][j], next_state[1][1] = "0", "1"
        s, n = 1, 1
    # row 3
    if i == 2 and j == 1 and cur[2][0] == "0":
        next_state[i][j], next_state[2][0] = "0", "1"
        s, n = 2, 0
    if i == 2 and j == 3 and cur[2][2] == "0":
        next_state[i][j], next_state[2][2] = "0", "1"
        s, n = 2, 2
    # row 4
    if i == 3 and j == 1 and cur[3][0] == "0":
        next_state[i][j], next_state[3][0] = "0", "1"
        s, n = 3, 0
    if i == 3 and j == 2 and cur[3][1] == "0":
        next_state[i][j], next_state[3][1] = "0", "1"
        s, n = 3, 1
    # row 5
    if i == 4 and j == 1 and cur[4][0] == "0":
        next_state[i][j], next_state[4][0] = "0", "1"
        s, n = 4, 0
    if i == 4 and j == 2 and cur[4][1] == "0":
        next_state[i][j], next_state[4][1] = "0", "1"
        s, n = 4, 1
    return next_state, s, n


count = 0
while True:

    if player_turn == '2':
        if count <= 12:
            # Player X move - AI
            rMove, cMove, s, n = minimax_decision(board)
            # now we have a valid X move
            board[rMove][cMove] = '2'
            # Print gameBoard()
            print_board(board)
            if check_connect(board):
                '''code to remove a piece'''
                break
            count += 1
            print(count)
            change_turn()
        if count > 12:
            # Player X move - AI
            rMove, cMove, s, n = minimax_decision(board)
            # now we have a valid X move
            print(rMove)
            print(cMove)
            print(s)
            print(n)
            board[rMove][cMove] = '0'
            board[s][n] = "2"
            # Print gameBoard()
            print_board(board)
            if check_connect(board):
                '''code to remove a piece'''
                break
            count += 1
            print(count)
            change_turn()
    else:
        if count < 12:
            # Player Y move
            user_input = input("What position on the board would you like to capture? :")
            while user_input.upper() not in locations:
                user_input = input("Invalid move: Location does Not Exist. What position on the board would you like "
                                   "to capture? :")
            while board[placement(user_input.upper())[0]][placement(user_input.upper())[1]] != "0":
                user_input = input("Invalid move: Not an Empty Space. What position on the board would you like to "
                                   "capture? :")
                position = placement(user_input.upper())
                rMove = position[0]
                cMove = position[1]
            position = placement(user_input.upper())
            rMove = position[0]
            cMove = position[1]
            board[rMove][cMove] = '1'
            # Print gameBoard()
            print_board(board)
            if check_connect(board):
                '''code to remove a piece'''
                break
            count += 1
            print(count)
            change_turn()
        if count >= 12:
            user_input = input("What position would you like to move? :")
            while user_input.upper() not in locations:
                user_input = input(
                    "Invalid move: Location does Not Exist. What position on the board would you like to "
                    "capture? :")
            while board[placement(user_input.upper())[0]][placement(user_input.upper())[1]] != "1":
                user_input = input(
                    "Invalid move: Not one of your captured spaces. What position on the board would you like to "
                    "capture? :")
            user_new = input("What way would you like to move the piece? :")
            while user_new.upper() not in locations:
                user_new = input("Invalid move: Location does Not Exist. What position on the board would you like to "
                                 "capture? :")
            while board[placement(user_new.upper())[0]][placement(user_new.upper())[1]] != "0":
                user_new = input("Invalid move: Not an Empty Space. What position on the board would you like to "
                                 "capture? :")
            position = placement(user_input.upper())
            rMove = position[0]
            cMove = position[1]
            new_position = placement(user_new.upper())
            rMove_new = new_position[0]
            cMove_new = new_position[1]
            # now we have a valid X move
            board[rMove][cMove] = '0'
            board[rMove_new][cMove_new] = "1"
            # Print gameBoard()
            print_board(board)
            if check_connect(board):
                '''code to remove a piece'''
                break
            count += 1
            print(count)
            change_turn()
