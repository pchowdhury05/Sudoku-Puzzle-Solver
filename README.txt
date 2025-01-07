Punna Chowdhury
November 12, 2024

Instructions:
- Please run `sudoku_1.py,` `sudoku_2.py,` and `sudoku_3.py` first to define the easy, medium, and hard sudoku puzzles. 
- Then, run `main.py` to execute the solution to the sudoku problems. 
- sudoku_2 and sudoku_3 are the puzzles provided on Canvas Assignment 04, representing medium and hard levels, respectively.
  - I incorporated sudoku_1 to add an easy level

Dependencies Used:
- `copy` is used to display a fresh copy of the unsolved Sudoku puzzle, ensuring that each puzzle starts in its unsolved state. 

Methodology and Assumptions:
- **Backtracking Algorithm**:
  - Backtracking algorithm is used to solve these Sudoku problems. This algorithm will try every possible solution, step-by-step. 
    - It does so by first choosing a section, checking if the choice fits the solution, moving forward with the next decision if valid, and backtracking if the choice is invalid to try another option.
  - Recursive backtracking helps implement the backtracking algorithm by finding a blank cell on the board:
    - For each blank cell, it checks if a number 1 - 9 is valid for that cell.
    - If the number is valid, it places the number in that cell and proceed to recursively check the rest of the board.
    - If it encounters a invalid choice, where the number cannot be placed in a blank cell, it will backtrack by resetting the cell empty (0) again and will try another number.
    - The process continues until the blank cell has a valid number to solve the puzzle.  
  - Heuristics and Constraint:
    - Minimum Remaining Values (MRV) is applied to choose the variable with the fewest legal values in its domain. 
      - Address blank cells with the most constraint early on 
    - Least Constraining Value (LCV) is applied to choose the value that rules out the fewest choices for the neighbors.
    - Forward checking is applied to tracks the domains for the unassigned variables and immediately removes possible bad options. If the domain of any variables is empty, it triggers a backtracking. 
      - For example, if a number is placed in an empty cell, forward checking removes that number being used again in the same row, column, and grid, reducing the searching space. 

- **Assumptions**:
  - We will apply the same traditional Sudoku base, which is a 9 X 9 puzzle grid of nine 3 X 3 regions. Each region, row, and column contain nine cells. 
  - We will assume that each puzzle is unique and therefore has a unique solution. 
  - Each row and column must contain unique numbers from 1 to 9, with no duplicates. In other words, each row and column must only contain a single from number from 1 to 9, with no numbers repeating.
  - Puzzle Preference: User has the choice to select a Sudoku puzzle based on the difficulty of their choosing. 
- **Final Output**:
  - Output: After selecting a Sudoku puzzle, the program will display the unsolved puzzle first, followed by the solved puzzle.
  - Example Output:
      " Choose a Sudoku puzzle to solve:
        Enter 1 for Easy puzzle,
        or 2 for Medium puzzle,
        or 3 for Hard puzzle: 3

        Selected Sudoku Puzzle:
          7   |   4 2 |       
              |     8 | 6 1   
        3 9   |       |     7 
        ------+-------+------
              |     4 |     9 
            3 |       | 7     
        5     | 1     |       
        ------+-------+------
        8     |       |   7 6 
          5 4 | 8     |       
              | 6 1   |   5   

        Solved Sudoku Puzzle:
        1 7 6 | 3 4 2 | 9 8 5 
        4 2 5 | 9 7 8 | 6 1 3 
        3 9 8 | 5 6 1 | 4 2 7 
        ------+-------+------
        2 6 1 | 7 8 4 | 5 3 9 
        9 8 3 | 2 5 6 | 7 4 1 
        5 4 7 | 1 9 3 | 2 6 8 
        ------+-------+------
        8 1 9 | 4 2 5 | 3 7 6 
        6 5 4 | 8 3 7 | 1 9 2 
        7 3 2 | 6 1 9 | 8 5 4 

        Do you want to try another puzzle? (yes/no): " 
    - The user can choose to re-run the algorithm to select a different Sudoku puzzle and view the solution for that puzzle as well.
