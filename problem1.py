from random import randrange

number=randrange(1,1000)
secret=int(raw_input("We are going to play higher and lower, guess a number from 1 to 1000.\n>"))
while(secret!=number):
	if(secret<number):
		print("Guess Higher")
		secret=int(raw_input("Enter another number.\n>"))
	elif(secret>number):
		print("Guess Lower")
		secret=int(raw_input("Enter another number.\n>"))
print("Congrats you got it, the right number was {}!".format(number))
