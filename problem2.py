from random import randrange
numlow=1
numhigh=1001
highorlow=" "
print("We are going to play high or lower again but this time the computer is guessing!\nThink of a secret number from 1 to 1000")
numberguess=randrange(1,1000)
while(highorlow!="right"):
	highorlow=raw_input("The computer guessed {}, is that too high or too low, or just right?\n>".format(numberguess))
	if(highorlow=="high"):
		numhigh=numberguess-1
		numberguess=randrange(numlow,numhigh)
	elif(highorlow=="low"):
		numlow=numberguess+1
		numberguess=randrange(numlow,numhigh)
print("Congrats the computer got it!\nComputer - The number is (Machine clinking) {}.".format(numberguess))
