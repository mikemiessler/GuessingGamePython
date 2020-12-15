import random

random_num = random.randint(1,10)  # random numbers between 1-10
guess_num = None
# hold gueses

# handle logic

while guess_num != random_num:

	guess_num = input("what is the number: ")
	guess_num = int(guess_num)

	if guess_num == random_num:
		print("CorrecT! You guessed the right number!")
	elif guess_num < random_num:
		print("You guessed too low")
	elif guess_num > random_num:
		print("You guessed too high")  
	else:
		print("your won!")