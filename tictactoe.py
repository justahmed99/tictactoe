theBoard = {'a0':'1', 'a1':'4', 'a2':'7', 'b0':'2', 'b1':'5', 'b2':'8', 'c0':'3', 'c1':'6', 'c2':'9'}
def drawBoard(board) :
	print(' ' + board['a0'] + ' | ' + board['b0'] + ' | ' + board['c0'] + ' ')
	print('---+---+---')
	print(' ' + board['a1'] + ' | ' + board['b1'] + ' | ' + board['c1'] + ' ')
	print('---+---+---')
	print(' ' + board['a2'] + ' | ' + board['b2'] + ' | ' + board['c2'] + ' ')

def playerInput() :
	turn = 9
	player = 'O'
	winState = False
	while turn != 0 :
		print('Turn for player \'' + player + '\'.')
		playerInput = int(input('Where do you want to move ? '))
		if playerInput >= 1 and playerInput <= 3:
			theBoard[chr(ord('a')+ (playerInput-1) % 3) + '0'] = player
		if playerInput >= 4 and playerInput <=6 :
			theBoard[chr(ord('a') + (playerInput-1) % 3) + '1'] = player
		if playerInput >= 7 and playerInput <=9 :
			theBoard[chr(ord('a') + (playerInput-1) % 3) + '2'] = player
			
		drawBoard(theBoard)
		winState = theWinner(theBoard, winState)
		if winState == True :
			print(player + ' is won!')
			break
		player = switchPlayer(player)
		turn = turn - 1

def winStatus(wState) :
	wState = True
	return wState

def theWinner(board, state) :
	if board['a0'] == board['b0'] and board['b0'] == board['c0'] :
		state = winStatus(state)
	if board['a1'] == board['b1'] and board['b1'] == board['c1'] :
		state = winStatus(state)
	if board['a2'] == board['b2'] and board['b2'] == board['c2'] :
		state = winStatus(state)
	if board['a0'] == board['a1'] and board['a1'] == board['a2'] :
		state = winStatus(state)
	if board['b0'] == board['b1'] and board['b1'] == board['b2'] :
		state = winStatus(state)
	if board['c0'] == board['c1'] and board['c1'] == board['c2'] :
		state = winStatus(state)
	if board['a0'] == board['b1'] and board['b1'] == board['c2'] :
		state = winStatus(state)
	if board['a2'] == board['b1'] and board['b1'] == board['c0'] :
		state = winStatus(state)
	
	return state
	
	
def whoIsTheWinner(board, player, winState) :
	#first probability
	for i in range(0,3) :
		if board['a' + str(i)] == board['b' + str(i)] and board['b' + str(i)] == board['c' + str(i)] :
			print(player + ' is won!')
			winState = winStatus(winState)
			print(winState)
	
	#second probability
	for i in range(0,3) :
		if board[chr(ord('a') + i) + '0'] == board[chr(ord('a') + i) + '1'] and board[chr(ord('a') + i) + '1'] == board[chr(ord('a') + i) + '2'] :
			print(player + ' is won!')	
			winStatus(winState)

	#third probability
	if board['a0'] == board['b1'] and board['b1'] == board['c2'] :
		print(player + ' is won!')
		winStatus(winState)
	elif board['c0'] == board['b1'] and board['b1'] == board['a2'] :
		print(player + ' is won!')
		winStatus(winState)
	
	return winState

def switchPlayer(player) :
	if player == 'O' :
		return 'X'
	elif player == 'X' :
		return 'O'

def main() :
	drawBoard(theBoard)
	playerInput()

if __name__ == '__main__' :
	main()
