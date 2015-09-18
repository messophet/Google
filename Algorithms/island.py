import math

def setBoard(st):
	numOfPoints = len(st)
	n = math.sqrt(numOfPoints) #required to form N lists of N elements
	board = list()
	arr = list()
	count = 0
	for i in st:
		if(count!=n):
			arr.append(i)
			count+=1
			if(count==n):
				board.append(arr)
				arr = list()
				count = 0
		else:
			board.append(arr)
			arr = list()
			count = 0
	return board

def iterative_search(board):
	sq = int(math.sqrt(len(game))) # N x N pieces, so N = sqrt(N x N)
	numCount = 0
	for i in range(len(board)):
		for j in range(sq):
			if(board[i][j]=='1'):
				board = recursive_search(board,i,j,sq)
				numCount += 1
	return numCount

def recursive_search(board,i,j,sq):
	board[i][j]='0'

	if(i-1 >= 0):
		if(board[i-1][j]=='1'):
			return recursive_search(board,i-1,j,sq)
	if(i+1<sq):
		if(board[i+1][j]=='1'):
			return recursive_search(board,i+1,j,sq)
	if(j-1>=0):
		if(board[i][j-1]=='1'):
			return recursive_search(board,i,j-1,sq)
	if(j+1<sq):
		if(board[i][j+1]=='1'):
			return recursive_search(board,i,j+1,sq)
	return board

game = '1000001001101011110111111'
board = setBoard(game)

print('###INPUT###')
n=int(math.sqrt(len(game)))
splitStr=[game[i:i+n] for i in range(0, len(game), n)]
for i in splitStr:
	print(i)
print('###ENDINPUT###')

print('Total Islands: {}'.format(iterative_search(board)))