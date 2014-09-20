import argparse
import printboard

def main():
	parser = argparse.ArgumentParser(description = "get file")
	parser.add_argument("board")
	parser.add_argument("p1move")
	parser.add_argument("p2move")
	args = parser.parse_args()


	p1move, p2move = args.p1move, args.p2move

	result = ''


	p1loss, p2loss = False,False


	p1position, p2position = [-1,-1],[-1,-1]

	g = open(args.board, "r")

	t = g.read()

	g.close()

	t = t.split()

	numRows = int(t[0])
	numCols = int(t[1])
	b = t[2]

	board = [['!' for x in range(numCols)] for y in range(numRows)]

	for i in range(numRows):
		for j in range(numCols):
			board[i][j] = b[i*numCols + j]
		
			if board[i][j] == '@':
				p1position = [i,j]
			if board[i][j] == '*':
				p2position = [i,j]


	if p1move == 'N':
		p1nextpos = [p1position[0]-1,p1position[1]]
	elif p1move == 'S':
		p1nextpos = [p1position[0]+1,p1position[1]]
	elif p1move == 'E':
		p1nextpos = [p1position[0],p1position[1]+1]
	elif p1move == 'W':
		p1nextpos = [p1position[0],p1position[1]-1]
	
	
	if p2move == 'N':
		p2nextpos = [p2position[0]-1,p2position[1]]
	elif p2move == 'S':
		p2nextpos = [p2position[0]+1,p2position[1]]
	elif p2move == 'E':
		p2nextpos = [p2position[0],p2position[1]+1]
	elif p2move == 'W':
		p2nextpos = [p2position[0],p2position[1]-1]
	
	
	
	if board[p1nextpos[0]][p1nextpos[1]] != 'O':
		p1loss = True
	
	if board[p2nextpos[0]][p2nextpos[1]] != 'O':
		p2loss = True
	
	if p1nextpos == p2nextpos:
		p1loss = True
		p2loss = True


	if p1loss == True:
		if p2loss == True:
			print 'Tie'
			return False
		else:
			print 'Player 2 wins'
			return False
	elif p2loss == 'True':
		print 'Player 1 wins'
		return False


	board[p1position[0]][p1position[1]] = '1'
	board[p2position[0]][p2position[1]] = '2'
	
	board[p1nextpos[0]][p1nextpos[1]] = '@'
	board[p2nextpos[0]][p2nextpos[1]] = '*'
	
	
	s = str(numRows) + ' ' + str(numCols) + ' '
	
	for i in range(numRows):
		for j in range(numCols):
			s += board[i][j]
	
	
	g = open(args.board, "w")
	g.write(s)
	g.close()
	
	printboard.printBoard('board.txt')

	return True





#execute if run as a script
if __name__ == "__main__":
	main()
	










