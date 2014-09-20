#make a game board and write it to board.txt
#board will be stored as numRows numCols string_of_chars

import argparse

parser = argparse.ArgumentParser(description = "get file")
parser.add_argument("board")
parser.add_argument("numRows")
parser.add_argument("numCols")
args = parser.parse_args()


numRows = int(args.numRows)
numCols = int(args.numCols)

row = '#'

for i in range(numCols - 2):
	row += 'O'

row += '#'

endRow = ''

for i in range(numCols):
	endRow += '#'

midRow = '#'

for i in range(numCols/4 - 1):
	midRow += 'O'

midRow += '@'

while len(midRow) < numCols - numCols/4 - 1:
	midRow += 'O'

midRow += '*'

while len(midRow) < numCols - 1:
	midRow += 'O'

midRow += '#'

board = str(numRows) + ' ' + str(numCols) + ' '

board += endRow

rows = 1

for i in range(numRows/2 - 1):
	board += row
	rows += 1

board += midRow
rows += 1

while rows < numRows - 1:
	board+= row
	rows += 1

board += endRow


g = open(args.board, "w")
g.write(board)
g.close()


#board = [[0 for x in range(52)] for x in range(52)]
#
#for i in range(52):
#	board[0][i] = '#'
#	board[51][i] = '#'
#	board[i][0] = '#'
#	board[0][i] = '#'

