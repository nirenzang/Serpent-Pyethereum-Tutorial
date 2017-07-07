import serpent
from ethereum.tools import tester
from ethereum import utils
import sys
import struct
import binascii
import pytest

serpent_code = '''
data player[2](address, commit, choice, has_revealed)
data num_players
data reward
data timer_start
data check_winner[3][3]

def init():
	#If 2, tie
	#If 0, player 0 wins
	#If 1, player 1 wins

	#0 = rock
	#1 = paper
	#2 = scissors

	self.check_winner[0][0] = 2
	self.check_winner[1][1] = 2
	self.check_winner[2][2] = 2

	#Rock beats scissors
	self.check_winner[0][2] = 0
	self.check_winner[2][0] = 1

	#Scissors beats paper
	self.check_winner[2][1] = 0
	self.check_winner[1][2] = 1

	#Paper beats rock
	self.check_winner[1][0] = 0
	self.check_winner[0][1] = 1

	self.num_players = 0

#accepts a hash from the player in form sha3(address, choice, nonce)
def add_player(player_commitment):
	#prevents a max callstack exception
	if self.test_callstack() != 1: return(-1)

	if self.num_players < 2 and msg.value >= 1000:
		self.reward = self.reward + msg.value
		self.player[self.num_players].address = msg.sender
		self.player[self.num_players].commit = player_commitment
		self.num_players = self.num_players + 1
		if msg.value - 1000 > 0:
			send(0, msg.sender, msg.value-1000)
		return(0)

	else:	
		if msg.value > 0 :
			# prevent unnecessary leakage of money
			send(0, msg.sender, msg.value)
		return(-1)
		
#verifies the choice in their committed answer matches
def open(choice, nonce):
    #prevents a max callstack exception
    YOURCODEHERE

	#Ensure two players are in the contract, if not return -1
	YOURCODEHERE

	#Determine which player submitted the open request
	YOURCODEHERE

	#Check the commitment and ensure they have not tried to commit already
	if YOURCODEHERE(commitment is correct) and not YOURCODEHERE(first time commit):
		#If commitment verified, we should store choice in plain text
		YOURCODEHERE
        #Remember that the choice is revealed
        YOURCODEHERE
		#Store current block number to give other player 10 blocks to open their commit
		YOURCODEHERE
        return(0)
	else:
		return(-1)

def check():
	if self.test_callstack() != 1: return(-1)

	#Check to make sure at least 10 blocks have been given for both players to reveal their play.
	if block.number - self.timer_start < 10: return(-2)

	#check to see if both players have revealed answer
	if self.player[0].has_revealed and self.player[1].has_revealed:
		p0_choice = self.player[0].choice
		p1_choice = self.player[1].choice

		#If player 0 wins
		if self.check_winner[p0_choice][p1_choice] == 0:
			send(0,self.player[0].address, self.reward)
			return(0)
		#If player 1 wins
		elif self.check_winner[p0_choice][p1_choice] == 1:
			send(0,self.player[1].address, self.reward)
			return(1)
		#If no one wins
		else:
			send(0,self.player[0].address, self.reward/2)
			send(0,self.player[1].address, self.reward/2)
			return(2)

	#if p1 revealed but p2 did not, send money to p1
	elif self.player[0].has_revealed and not self.player[1].has_revealed:
		send(0,self.player[0].address, self.reward)
		return(0)

	#if p2 revealed but p1 did not, send money to p2
	elif not self.player[0].has_revealed and self.player[1].has_revealed:
		send(0,self.player[1].address, self.reward)
		return(1)

	#if neither p1 nor p2 revealed, keep both of their bets
	else:
		return(-1)

#returns the balance to ensure funds were lost and won properly
def balance_check():
	log(self.storage["player1"].balance)
	log(self.storage["player2"].balance)

def test_callstack():
	return(1)
'''

s = tester.Chain()
c = s.contract(serpent_code, language='serpent')

print("Output of 1 designated success for player 1.")
print("Output of 2 designated success for player 2.")
print("Output of 0 designated a tie.")
print("Output of -1 designated an error.\n")

##################################### SETUP COMMITMENTS ########################################
choice = ["rock", "paper", "scissors"]

choice1 = 2
nonce1 = 1
YOURCODEHERE(compute the sha3 commitment of player 0)
print("Player zero chooses {} which is: {}".format(choice1, choice[choice1]))

choice2 = 0
nonce2 = 1
YOURCODEHERE(compute the sha3 commitment of player 1)
print("Player one chooses {} which is: {}\n".format(choice2, choice[choice2]))

# send the players' choices
o = YOURCODEHERE
print("Player 0 Added: {}".format(o))
o = YOURCODEHERE
print("Player 1 Added: {}\n".format(o))

# open the commitment, use s.tx() instead of c.open()!
YOURCODEHERE
print("Open for player 0: {}".format(o))

YOURCODEHERE
print("Open for player 1: {}\n".format(o))

# mine 11 blocks
YOURCODEHERE # needed to move the blockchain at least 10 blocks so check can run

o = c.check(sender=tester.k1)
print("Check says player {} wins\n".format(o))

c.balance_check(sender=tester.k0)

# output how many gas are used for all these transactions
YOURCODEHERE
# output the balance of contract c
YOURCODEHERE
