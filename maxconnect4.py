# Sample Implementation of Assignment 3, Task 1
# (c) Vamsikrishna Gopikrishna, PhD
# University of Texas at Arlington.

import sys #To extract cmd line arguments and for exit func
from copy import deepcopy #for copying objects
from random import shuffle #for randomizing the move order (not necessary for assignment)

class gameState: #data structure to store a game board
	def __init__(self, state, cPlayer, maxPlayer):
		self.state = state
		self.cPlayer = cPlayer
		self.maxPlayer = maxPlayer
		self.pieceCount = sum(1 for row in state for piece in row if piece)
	
	def __str__(self): #returns string representation of game board and other game information
		res = '\t-----------------\n'
		for i in range(6):
			res = res + '\t|'
			for j in range(7):
				res = res + ' ' + str(self.state[i][j])
			res = res +' |\n'
		res = res + '\t-----------------\n'
		res = res + 'Current Player: '+str(self.cPlayer)+' MAX Player: '+str(self.maxPlayer)+' Moves Made: '+str(self.pieceCount)+'\n'
		[score1,score2] = self.checkPatterns([1]*4,[2]*4)
		if score1 > score2:
			res = res + 'Player 1 Leading. Score: '+str(score1)+'-'+str(score2)
		elif score2 > score1:
			res = res + 'Player 2 Leading. Score: '+str(score1)+'-'+str(score2)
		else:
			res = res + 'Player 1 & 2 Tied. Score: '+str(score1)+'-'+str(score2)
		return res
	
	def __cmp__(self,other): #allows you to compare two game states (not necessary for assignment)
		return cmp(self.eval(),other.eval())
	
	def playPiece(self, column): #returns the game state that results from playing a move in particular game state (null if move not possible).
		tState = deepcopy(self.state)
		if not tState[0][column]:
			for i in range(5, -1, -1):
				if not tState[i][column]:
					tState[i][column] = self.cPlayer
					if self.cPlayer == 1:
						return gameState(tState, 2, self.maxPlayer)
					else:
						return gameState(tState, 1, self.maxPlayer)
		return None

	def checkPatterns (self, pattern1, pattern2): #check how many instances of specific patters for player 1 and 2 are present in the game board.
		num1 = 0
		num2 = 0
		#Horizontal
		for row in self.state:
			#For Player 1
			tmp = row[0:4]
			tmp.sort()
			if  tmp == pattern1:
				num1 += 1
			tmp = row[1:5]
			tmp.sort()
			if tmp == pattern1:
				num1 += 1
			tmp = row[2:6]
			tmp.sort()
			if tmp == pattern1:
				num1 += 1
			tmp = row[3:7]
			tmp.sort()
			if tmp == pattern1:
				num1 += 1
			#For Player 2
			tmp = row[0:4]
			tmp.sort()
			if  tmp == pattern2:
				num2 += 1
			tmp = row[1:5]
			tmp.sort()
			if tmp == pattern2:
				num2 += 1
			tmp = row[2:6]
			tmp.sort()
			if tmp == pattern2:
				num2 += 1
			tmp = row[3:7]
			tmp.sort()
			if tmp == pattern2:
				num2 += 1
		#Vertical
		for j in range(7):
			tmp = [self.state[0][j], self.state[1][j], self.state[2][j], self.state[3][j]]
			tmp.sort()
			#For Player 1
			if tmp == pattern1:
				num1 += 1
			#For Player 2
			if tmp == pattern2:
				num2 += 1
			tmp = [self.state[1][j], self.state[2][j], self.state[3][j], self.state[4][j]]
			tmp.sort()
			#For Player 1
			if tmp == pattern1:
				num1 += 1
			#For Player 2
			if tmp == pattern2:
				num2 += 1
			tmp = [self.state[2][j], self.state[3][j], self.state[4][j], self.state[5][j]]
			tmp.sort()
			#For Player 1
			if tmp == pattern1:
				num1 += 1
			#For Player 2
			if tmp == pattern2:
				num2 += 1
		#Diagonal BL to TR
		tmp = [self.state[0][0], self.state[1][1], self.state[2][2], self.state[3][3]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][0], self.state[2][1], self.state[3][2], self.state[4][3]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][0], self.state[3][1], self.state[4][2], self.state[5][3]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[0][1], self.state[1][2], self.state[2][3], self.state[3][4]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][1], self.state[2][2], self.state[3][3], self.state[4][4]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][1], self.state[3][2], self.state[4][3], self.state[5][4]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[0][2], self.state[1][3], self.state[2][4], self.state[3][5]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][2], self.state[2][3], self.state[3][4], self.state[4][5]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][2], self.state[3][3], self.state[4][4], self.state[5][5]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[0][3], self.state[1][4], self.state[2][5], self.state[3][6]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][3], self.state[2][4], self.state[3][5], self.state[4][6]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][3], self.state[3][4], self.state[4][5], self.state[5][6]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		#Diagonal TL to BR
		tmp = [self.state[0][6], self.state[1][5], self.state[2][4], self.state[3][3]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][6], self.state[2][5], self.state[3][4], self.state[4][3]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][6], self.state[3][5], self.state[4][4], self.state[5][3]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[0][5], self.state[1][4], self.state[2][3], self.state[3][2]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][5], self.state[2][4], self.state[3][3], self.state[4][2]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][5], self.state[3][4], self.state[4][3], self.state[5][2]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[0][4], self.state[1][3], self.state[2][2], self.state[3][1]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][4], self.state[2][3], self.state[3][2], self.state[4][1]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][4], self.state[3][3], self.state[4][2], self.state[5][1]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[0][3], self.state[1][2], self.state[2][1], self.state[3][0]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[1][3], self.state[2][2], self.state[3][1], self.state[4][0]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		tmp = [self.state[2][3], self.state[3][2], self.state[4][1], self.state[5][0]]
		tmp.sort()
		#For Player 1
		if tmp == pattern1:
			num1 += 1
		#For Player 2
		if tmp == pattern2:
			num2 += 1
		return [num1, num2]
	
	def eval(self): #eval function (functions as utiltiy fn also when called on a terminal state)
		weight3Row = (1.0/7.0) #weight for 3 in a row along with 1 blank space
		weight2Row = (1.0/7.0) ** 2 #weight for 2 in a row along with 2 blank space
		weight1Row = (1.0/7.0) ** 3 #weight for 1 in a row along with 3 blank space
		#Checking 4 in a rows:
		[score1_4Row,score2_4Row] = self.checkPatterns([1]*4,[2]*4)
		#Checking 3 in a rows (with 1 blank):
		[score1_3Row,score2_3Row] = self.checkPatterns([0,1,1,1],[0,2,2,2])
		#Checking 2 in a rows (with 2 blank):
		[score1_2Row,score2_2Row] = self.checkPatterns([0,0,1,1],[0,0,2,2])
		#Checking 1 in a rows (with 3 blank):
		[score1_1Row,score2_1Row] = self.checkPatterns([0,0,0,1],[0,0,0,2])
		score1 = score1_4Row + weight3Row * score1_3Row + weight2Row * score1_2Row + weight1Row * score1_1Row
		score2 = score2_4Row + weight3Row * score2_3Row + weight2Row * score2_2Row + weight1Row * score2_1Row
		if self.maxPlayer == 1:
			return float(score1-score2)
		else:
			return float(score2-score1)
			
def minMaxDecision(cState):
	if cState.pieceCount == 42: #Trying to minmax on a already terminal state will return null
		return [None, -1]
	alpha = float('-Inf')
	beta = float('Inf')
	optMove = -1 #best move so far
	val = float('-Inf') #best payoff so far
	actions = range(7)
	shuffle(actions) #randomize order of actions (not necessary for assignment)
	for a in actions:
		succ = cState.playPiece(a) #generate successor
		if succ is not None:
			if dumpValues: print 'MAX['+str(alpha)+', '+str(beta)+'] exploring action '+str(a)+'...'
			tVal = minVal(succ,alpha,beta,1) #start minmax exploration of successor
			if tVal > val:
				val = tVal #update payoff and action if necessary
				optMove = a 
				if val > alpha: #update alpha if necessary
					alpha = val
	if dumpValues: print '...MAX['+str(alpha)+', '+str(beta)+'] returns '+str(optMove)
	return [optMove, val]

def minVal(gState,alpha,beta,d): #find minmax value of min nodes
	dStr = ''
	for i in range(d):
		dStr = dStr + '     '
	if (gState.pieceCount == 42) or (d == depthLimit): #depth limit reached or terminal node
		val = gState.eval()
		if dumpValues: print dStr + 'MIN['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' returns Eval: '+str(val)
		return val
	val = float('Inf') #lowest values so far
	actions = range(7)
	shuffle(actions) #randomize order of actions (not necessary for assignment)
	for a in actions:
		succ = gState.playPiece(a) #generate succesor
		if succ is not None:
			if dumpValues: print dStr + 'MIN['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' exploring action '+str(a)+'...'
			tVal = maxVal(succ,alpha,beta,d+1) #explore successor
			if tVal < val:
				val = tVal #update value if necessary
				if val <= alpha: #check if remaing branches can be pruned
					if dumpValues: print dStr + '...MIN['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' returns Value: '+str(val)+' due to pruning'
					return val
				if val < beta: #update beta if necssary
					beta = val
	if dumpValues: print dStr + '...MIN['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' returns Value: '+str(val)
	return val #return minamax value

def maxVal(gState,alpha,beta,d): #find minmax value of max nodes (except for root node)
	dStr = ''
	for i in range(d):
		dStr = dStr + '     '
	if (gState.pieceCount == 42) or (d == depthLimit): #depth limit reached or terminal node
		val = gState.eval()
		if dumpValues: print dStr + 'MAX['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' returns Eval: '+str(val)
		return val
	val = float('-Inf') #highest values so far
	actions = range(7)
	shuffle(actions) #randomize order of actions (not necessary for assignment)
	for a in actions:
		succ = gState.playPiece(a) #generate successor
		if succ is not None:
			if dumpValues: print dStr + 'MAX['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' exploring action '+str(a)+'...'
			tVal = minVal(succ,alpha,beta,d+1) #explore successor
			if tVal > val:
				val = tVal #update value if necessary
				if val >= beta: #check if remaining branches can be pruned
					if dumpValues: print dStr + '...MAX['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' returns Value: '+str(val)+' due to pruning'
					return val
				if alpha > val:#update alpha if necessary
					alpha = val
	if dumpValues: print dStr + '...MAX['+str(alpha)+', '+str(beta)+'] at depth ' + str(d) + ' returns Value: '+str(val)
	return val #return minamax value

def readFile(fileName): #Read game board from file.
	try:
		file = open(fileName,'r')
	except IOError:
		sys.exit("Error opening input file.\n\tCheck file name.")
	lines = file.readlines()
	state = [[int(char) for char in line[0:7]] for line in lines[0:-1]]
	player = int(lines[-1][0])
	file.close()
	return [state, player]

def writeFile(fileName, game): #write game board to file.
	try:
		file = open(fileName,'w')
	except IOError:
		sys.exit("Error opening output file.\n\tCheck file name.")
	for row in game.state:
		file.write(''.join(str(col) for col in row) + '\r\n')
	file.write('%s\r\n' % str(game.cPlayer))
	file.close()
	
def humanMove(game): #Get legal human move and play it (For interactive mode)
	try:
		mv = raw_input('Enter Column Number (1-7): ')
	except EOFError:
		sys.exit("Terminated at Keyboad.")
	act = int(mv,10) - 1
	if act < 0 or act > 6:
		print 'Invalid Move. Try again.'
		return humanMove(game)
	res = game.playPiece(act)
	if res is None:
		print 'No more moves can be made in that column. Try again.'
		return humanMove(game)
	return res
	
#globals
dumpValues = False
depthLimit = 45

def main():
	if len(sys.argv) != 5:
		sys.exit("Incorrect number of arguments:\n\tInteractive Mode: maxconnect4.py interactive [input_file] [computer-next/human-next] [depth]\n\tOne-Move mode: maxconnect4.py one-move [input_file] [output_file] [depth]")
	if sys.argv[1] == 'one-move':
		oneMove = True
	elif sys.argv[1] == 'interactive':
		oneMove = False
	else:
		sys.exit("Unknown Mode given.\n")
	[st, pl] = readFile(sys.argv[2])
	global depthLimit
	depthLimit = int(sys.argv[4])
	if oneMove:
		game = gameState(st,pl,pl)
		if dumpValues: print '\tOne Move Mode...\nBefore Move:'
		if dumpValues: print str(game)
		[act, payoff] = minMaxDecision(game)
		if act is not None:
			res = game.playPiece(act)
			if dumpValues: print 'After Move:'
			if dumpValues: print str(res)
			if dumpValues: print 'Payoff: '+str(payoff)
			writeFile(sys.argv[3],res)
		else:
			print 'Game cannot be played. Board is full.'
	else:
		if sys.argv[3] == 'human-next':
			compTurn = False
			hPl = pl
			if pl == 1:
				game = gameState(st,pl,2)
			else:
				game = gameState(st,pl,1)
		elif sys.argv[3] == 'computer-next':
			compTurn = True
			game = gameState(st,pl,pl)
			if pl == 1:
				hPl = 2
			else:
				hPl = 1
		else:
			sys.exit("Options for interactive mode are computer-next/human-next")
		print str(game)
		while game.pieceCount < 42:
			if compTurn:
				print 'Thinking...'
				[act, payoff] = minMaxDecision(game)
				if act is not None:
					game = game.playPiece(act)
					print '...Done'
					writeFile('computer.txt',game)
				else:
					print 'This part should be unreachable'
				compTurn = False
			else:
				print 'Your Turn (You Play '+str(hPl)+' )'
				game = humanMove(game)
				writeFile('human.txt',game)
				compTurn = True
			print str(game)
		print 'Game Over'

if __name__ == "__main__":
	main()