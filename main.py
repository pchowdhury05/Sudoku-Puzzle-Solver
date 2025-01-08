# import Sudoku puzzles that need to be solved 
from sudoku_1 import puzzle_1
from sudoku_2 import puzzle_2
from sudoku_3 import puzzle_3
# import the copy module to make deep copies of puzzles
import copy  

# this will get a copy of a selected puzzle on user choice 
def get_puzzle(difficulty_level):
    if difficulty_level == '1':
        return copy.deepcopy(puzzle_1)
    elif difficulty_level == '2':
        return copy.deepcopy(puzzle_2)
    elif difficulty_level == '3':
        return copy.deepcopy(puzzle_3)
    else:
        return None

# visually display the Sudoku board 
def sudoku_board(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("------+-------+------")
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(cell if cell != 0 else " ", end=" ")
        print()

# this checks if there are no duplicates in numbers from 1-9
def is_valid(board, row, col, number):
    # check the row and column for duplicates of number
    for i in range(9):
        if board[row][i] == number or board[i][col] == number:
            return False
    # check the 3x3 sub-grid for duplicates of number
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == number:
                return False
    return True

# apply Minimum Remaining Values (MRV) to choose the variable with the fewest legal values in its domain 
def minimum_remaining_value_selection(board):
    # only choose numbers from 1-9 
    min_count = 10   
    selected_cell = None
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                possible_values = [num for num in range(1, 10) if is_valid(board, row, col, num)]
                if len(possible_values) < min_count:
                    min_count = len(possible_values)
                    selected_cell = (row, col)
    return selected_cell

# use Least Constraining Value (LCV) to choose the value that rules out the fewest choices for the neighbors  
def least_constraining_value(board, row, col):
    """Order the possible values for a cell by the least constraining value (LCV) heuristic."""
    possible_values = [num for num in range(1, 10) if is_valid(board, row, col, num)]
    def count_constraints(value):
        constraint_count = 0
        for i in range(9):
            if board[row][i] == 0 and is_valid(board, row, i, value):
                constraint_count += 1
            if board[i][col] == 0 and is_valid(board, i, col, value):
                constraint_count += 1
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == 0 and is_valid(board, start_row + i, start_col + j, value):
                    constraint_count += 1
        return constraint_count
    
    return sorted(possible_values, key=count_constraints)

# use forward checking to track the domains for the unassigned variables and immediately removes possible bad options
# if the domain of any variables is empty, it triggers a backtracking
def forward_check(board, row, col, number):
    original_domains = {}
    for i in range(9):
        if board[row][i] == 0:
            original_domains[(row, i)] = [num for num in range(1, 10) if is_valid(board, row, i, num)]
        if board[i][col] == 0:
            original_domains[(i, col)] = [num for num in range(1, 10) if is_valid(board, i, col, num)]
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == 0:
                original_domains[(start_row + i, start_col + j)] = [num for num in range(1, 10) if is_valid(board, start_row + i, start_col + j, num)]
    for (r, c), domain in original_domains.items():
        if number in domain:
            domain.remove(number)
        if not domain:
            return False, original_domains
    return True, original_domains

# use recursive backtracking with MRV, LCV, and forward checking to solve the puzzle 
def recursive_backtracking(board):
    variable = minimum_remaining_value_selection(board)
    if not variable:
        # Solved puzzle 
        return True 
    row, col = variable
    for value in least_constraining_value(board, row, col):
        if is_valid(board, row, col, value):
            board[row][col] = value
            is_consistent, original_domains = forward_check(board, row, col, value)
            if is_consistent and recursive_backtracking(board):
                return True
            board[row][col] = 0  
    return False

# solved sudoku by using recursive backtracking that includes both MRV, LCV, and forward checking
def solve_sudoku(board):
    return recursive_backtracking(board)

def main():
    while True:
        # user input to select a puzzle difficulty
        print("Choose a Sudoku puzzle to solve:")
        choice = input("Enter 1 for Easy puzzle,\nor 2 for Medium puzzle,\nor 3 for Hard puzzle: ")

        # get the selected puzzle
        puzzle = get_puzzle(choice)
        if puzzle is None:
            print("Invalid choice. Please try again.")
            continue
        # display selected unsolved Sudoku puzzle only
        print("\nSelected Sudoku Puzzle:")
        sudoku_board(puzzle)
        # display selected solved Sudoku puzzle only
        if solve_sudoku(puzzle):
            print("\nSolved Sudoku Puzzle:")
            sudoku_board(puzzle)
        else:
            print("No solution provided for this Sudoku puzzle. Sorry :C")

        # user input that ask if the user wants to try another puzzle
        try_again = input("\nDo you want to try another puzzle? (yes/no): ").strip().lower()
        if try_again != 'yes':
            print("Goodbye!")
            break

main()
