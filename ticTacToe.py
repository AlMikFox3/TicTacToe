import random

def drawBoard(board):
	print('   |   |')
	print(' '+board[7]+' | '+board[8]+' | '+board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' '+board[4]+' | '+board[5]+' | '+board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' '+board[1]+' | '+board[2]+' | '+board[3])
	print('   |   |')

def inputPlayerLetter():
	letter=''
	while not(letter=='X' or letter =='O'):
		print('Do you want X or O')
		letter=raw_input().upper()
	if(letter=='X'):
		return ['X','O']
	else:
		return ['O','X']

def whoGoesFirst():
	l=random.randint(0,1)
	if(l==1):
		return 'player'
	else:
		return 'computer'

def playAgain():
	print('Do you want to play again? (yes or no)')
	return raw_input('>').lower().startswith('y')

def makeMove(board,letter,move):
	board[move]=letter

def isWinner(bo,le):
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
	(bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
	(bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
	(bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
	(bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
	(bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
	(bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
	(bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
	dupBoard=[]
	for i in board:
		dupBoard.append(i)
	return dupBoard

def isSpaceFree(board,move):
	return board[move] == ' '

def getPlayerMove(board):
	move=' '
	while move not in [1,2,3,4,5,6,7,8,9] or not isSpaceFree(board, int(move)):
		print('Enter your next move (1-9:)')
		move = int(raw_input('>'))
	return move

def chooseRandomMoveFromList(board,moveList):
	possibleMoves=[]
	for i in moveList:
		if(isSpaceFree(board,i)):
			possibleMoves.append(i)
	if(len(possibleMoves)!=0):
		return random.choice(possibleMoves)
	else:
		return None

def getComputerMove(board,computerLetter):
	# Given a board and the computer's letter, determine where to move and return that move.
	if computerLetter == 'X':
		playerLetter = 'O'
	else:
		playerLetter = 'X'

	# Here is our algorithm for our Tic Tac Toe AI:
	# First, check if we can win in the next move
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy, computerLetter):
				return i

	# Check if the player could win on his next move, and block them.
	for i in range(1, 10):
		copy = getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, playerLetter, i)
			if isWinner(copy, playerLetter):
				return i

	# Try to take one of the corners, if they are free.
	move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
	if move != None:
		return move

	# Try to take the center, if it is free.
	if isSpaceFree(board, 5):
		return 5

	# Move on one of the sides.
	return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
	for i in range (1,10):
		if(isSpaceFree(board,i)):
			return False
	return True


print("WELCOME TO TICTACTOE")
while True:
	board=[' ']*10
	playerLetter, computerLetter = inputPlayerLetter()
	turn=whoGoesFirst()
	print('The '+turn+' will go first.')
	gameIsPlaying=True

	while gameIsPlaying:
		if turn == 'player':
			drawBoard(board)
			move = getPlayerMove(board)
			makeMove(board, playerLetter, int(move))

			if isWinner(board, playerLetter):
				drawBoard(board)
				print('Hooray! You have won the game!')
				gameIsPlaying = False
			else:
				if isBoardFull(board):
					drawBoard(board)
					print('The game is a tie!')
					break
				else:
					turn = 'computer'

		else:
			move=getComputerMove(board,computerLetter)
			makeMove(board,computerLetter,move)

			if isWinner(board, computerLetter):
				drawBoard(board)
				print('You have Lost.... Computer Wins')
				gameIsPlaying = False
			else:
				if isBoardFull(board):
					drawBoard(board)
					print('The game is a tie!')
					break
				else:
					turn = 'player'

	if not playAgain():
		break





