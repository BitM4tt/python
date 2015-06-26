import time

#######################################
# TextAdventure coded by Daniel Lewis #
#######################################

#Define functions
def get_input(prompt, accepted):
	response = input(prompt + " ")
	response = response.lower
	while True:
		if response in accepted:
			return response
		else:
			print("Please type one of the accepted answers: " + accepted)
			time.sleep(2)

#Define variables
hp = 30

#Start game
answer1 = get_input("Are you ready?", ["yes", "no"])
if answer1 == "yes":
	go = 1
else:
	if answer1 == "no":
		print("OK, maybe start being an adventurer tomorrow...")
