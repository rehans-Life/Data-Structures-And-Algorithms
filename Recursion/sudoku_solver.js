board = [
  [3, 0, 6, 5, 0, 8, 4, 0, 0],
  [5, 2, 0, 0, 0, 0, 0, 0, 0],
  [0, 8, 7, 0, 0, 0, 0, 3, 1],
  [0, 0, 3, 0, 1, 0, 0, 8, 0],
  [9, 0, 0, 8, 6, 3, 0, 0, 5],
  [0, 5, 0, 0, 9, 0, 6, 0, 0],
  [1, 3, 0, 0, 0, 0, 2, 5, 0],
  [0, 0, 0, 0, 0, 0, 0, 7, 4],
  [0, 0, 5, 2, 0, 6, 3, 0, 0],
];

function isValid(num, r, c, board) {
  for (let i = 0; i < 9; i++) {
    // We check all other cells of the row.
    if (board[r][i] === num) {
      return false;
    }

    if (board[i][c] === num) {
      return false;
    }

    if (
      board[3 * Math.floor(r / 3) + Math.floor(i / 3)][
        3 * Math.floor(c / 3) + Math.floor(i / 3)
      ] == num
    ) {
      return false;
    }
  }
  return true;
}

function sudoku_solver(board) {
  // Iterating through the board to find the first empty cell

  for (let i = 0; i < board.length; i++) {
    for (let j = 0; j < board[i].length; j++) {
      // Setting up a condition to check for the empty cell.
      if (board[i][j] == 0) {
        // If we find the empty cell then we know we can fill it with numbers
        // from 1 to 9 but the number we choose to fill the empty cell with
        // shouldnt be any of the other cells of the row, column and the 3x3 grid
        // where our empty cell exists inside of.
        for (let num = 1; num < 10; num++) {
          // Checking to see if the number is valid or not through a function
          // which checks its inside of the other cells of row and col and
          // thr 3x3 digits where out empty cell is inside of.
          if (isValid(num, i, j, board)) {
            // Replacing the empty cell with the valid number
            board[i][j] = num;

            // Then making a recursive call to fill out the next empty cell
            if (sudoku_solver(board)) {
              // If the recursive function returns true that means we were
              // able to fill our board completely hence we can return
              // the filled board
              return true;
            } else {
              // It can also return false if we were not able to fill a
              // empty cell with a valid integer cause we made a wrong
              // choice while choosing a valid integer to place in one
              // of our empty cells hence we need to backtrack remove
              // the integer from the empty cell and try out some other
              // valid integer
              board[i][j] = 0;
            }
          }
        }
        // If we were not able to fill an empty cell with a valid integer that
        // means we made a wrong choice while filling up our previous empty
        // cells therefore we return false so we can backtrack and undo our
        // changes and go for some other option.
        return false;
      }
    }
  }
  // If there are not empty cells then that means we have fillled up our board
  // completely so we return true
  return true;
}
console.log(sudoku_solver(board));
console.log(board);
[
  [3, 1, 6, 5, 7, 8, 4, 9, 2],
  [5, 2, 9, 1, 3, 4, 7, 6, 8],
  [4, 8, 7, 6, 2, 9, 5, 3, 1],
  [2, 6, 3, 4, 1, 5, 9, 8, 7],
  [9, 7, 4, 8, 6, 3, 1, 2, 5],
  [8, 5, 1, 7, 9, 2, 6, 4, 3],
  [1, 3, 8, 9, 4, 7, 2, 5, 6],
  [6, 9, 2, 3, 5, 1, 8, 7, 4],
  [7, 4, 5, 2, 8, 6, 3, 1, 9],
];
