import argparse

def printBoard(board):
	g = open(board, "r")
	
	s = g.read()
	
	s = s.split()
	
	numRows = int(s[0])
	numCols = int(s[1])
	b = s[2]
	
	for r in range(numRows):
		print b[r*numCols:r*numCols+numCols]
	

