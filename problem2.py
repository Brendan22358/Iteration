from random import randrange

secret=int(raw_input("We are going to play high or lower again but this time the computer is guessing!\nInput a secret number from 1 to 1000\n>"))
numberguess=randrange(1,1000)
if(secret<1 or secret>1000):
	secret=int(raw_input("Error 403: Enter a number between 1 and 1000!!!"))
while(secret!=numberguess):
	if(numberguess>secret):
		print("The computer guessed {} but that is too high.".format(numberguess))
		numberguess=randrange(1,numberguess)
	elif(numberguess<secret):
		print("The computer guessed {} but that is too low.".format(numberguess))
		numberguess=randrange(numberguess,1000)
print("Congrats the computer got it!\nComputer - The number is (Machine clinking) {}.".format(secret))
