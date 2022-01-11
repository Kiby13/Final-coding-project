def intro():
	global score
	print(" ")
	print("Press 1 to play the game")
	print("Press 2 to view high scores")
	print(" ")
	print("Please pick one of the options above")
	Answer = int(input("What would you like to do? \n"))
	if Answer == 1:
		print("Let's get playing!") #put everything here onto line with original code
		print("What was Jabari's first impression of the diving board?")
		print(" ")
		print("Press 1 if he thought it looked easy")
		print("Press 2 if he thought it looked scary")
		print("Press 3 if you're not sure")
		print(" ")
		print("Please pick one of the options above")
		print(" ")
		Answer1 = int(input("What is your answer? \n"))
		print(" ")
		if Answer1 == 1:
			print(" ")
			print("Congratulations, you're correct!")
			score = score + 10
			print ("You have", score, "Points!")
		elif Answer1 == 2:
			print(" ")
			print("Sorry, you're incorrect. But keep on going!")
			print("You lose 5 points.")
			score = score - 5
			print ("You have", score, "Points!")
		elif Answer1 == 3:
			print(" ")
			print("That's ok! You still have many questions to go.")
			print("You don't lose any points!")
			print("You still have", score, "Points!")
		else:
			print("That is not an option, please try again.")
			question1()
		print(" ")
		

		print("What was the first excuse does Jabari use to not go on the diving board?")
		print("Press 1 if he says that he's scared and he wants to wait a bit")
		print("Press 2 if he says that he's going to think of a special jump")	
		print("Press 3 if you're not sure")
		print(" ")
		print("Please pick one of the options")
		print(" ")
		Answer2 = int(input("What is your answer? \n"))
		if Answer2 == 2:
			print(" ")
			print("Congratulations you're correct!")
			print("You get 10 points!")
			score = score + 10
			print("You have", score, "Points!")
		elif Answer2 == 1:
			print(" ")
			print("Sorry, you're incorrect")
			print("You lose 5 points.")
			score = score - 5
			print("You have", score, "Points!")
		elif Answer2 == 3:
			print(" ")
			print("That's ok! You still have many questions to go.")
			print("You don't lose any points!")
			print("You still have", score, "Points!")
		else:
			print(" ")
			print("That is not an option, please try again.")
			question2()
		print(" ")


		print("What was the second excuse that Jabari used to not go on the board")
		print("Press 1 if he wanted to stretch before hand")
		print("Press 2 if he wanted to get his mom to take a picture first")
		print("Press 3 if you're unsure")
		print(" ")
		print("Please pick one of the options above")
		print(" ")
		Answer3 = int(input("What is your answer? \n"))
		if Answer3 == 1:
			print(" ")
			print("Congratulations you're correct!")
			print("You get 10 points!")
			score = score + 10
			print("You have", score, "Points!")
		elif Answer3 == 2:
			print(" ")
			print("Sorry, you're incorrect")
			print("You lose 5 points.")
			score = score - 5
			print("You have", score, "Points!")
		elif Answer3 == 3:
			print(" ")
			print("That's ok! You still have many questions to go.")
			print("You don't lose any points!")
			print("You still have", score, "Points!")
		else:
			print(" ")
			print("That is not an option, please try again")
			question3()
		print(" ")

		print("How does his dad feel about being scared")
		print("Press 1 if he thinks that Jabari's being a coward and he should just do it")
		print("press 2 if he thinks that it's ok that Jabari is scared")
		print("Press 3 if you're unsure")
		print(" ")
		print("Please pick one of the options")
		print(" ")
		Answer4 = int(input("What is your answer? \n"))
		if Answer4 == 2:
			print(" ")
			print("Congratulations you're correct!")
			print("You get 10 points!")
			score = score + 10
			print("You have", score, "Points!")
		if Answer4 == 1:
			print(" ")
			print("Sorry, you're incorrect")
			print("You lose 5 points.")
			score = score - 5
			print("You have", score, "Points!")
		if Answer4 == 3:
			print(" ")
			print("That's ok! You still have many questions to go.")
			print("You don't lose any points!")
			print("You still have", score, "Points!")
		else:
			print(" ")
			print("That is not an option, please try again")
			question4()
		print(" ")	

		print("This is the final question")
		print("It will be harder but you will get more points if you get it right")
		print("What does Jabari say after he jumps off the diving board")
		print(" ")
		print("Press 1 if he says that it was scary and he's never doing it again")
		print("Press 2 if he's going to do go on another time but with a double back flip")
		print("Press 3 if he said that it was fun but it's time to go home")
		print("")
		print("Please pick one of the options above")
		print(" ")
		Answer5 = int(input("What is your answer? \n"))
		if Answer5 == 2:
			print(" ")
			print("Congratulations you're correct!")
			print("You get 15 points!")
			score = score + 15
			print("You have", score, "Points!")
		elif Answer5 == 1:
			print(" ")
			print("Sorry, you're incorrect")
			print("You lose 5 points.")
			score = score - 5
			print("You have", score, "Points!")
		elif Answer5 == 3:
			print(" ")
			print("Sorry, you're incorrect")
			print("You lose 5 points.")
			score = score - 5
			print("You have", score, "Points!")
		else:
			print(" ")
			print("That is not an option, please try again")
			question5()
		print(" ")

				

		print(" ")
		print("That's the end!, you ended up with", score, "Points!")
		print(" ")
		print("Press 1 if you would like to play again")
		print("Press any other number if you are done playing")
		print(" ")
		ending = int(input("What would you like to do now? \n"))
		if ending == 1:
			print(" ")
			print("Great! Let's see if we can get a higher score!")
			print(art)
			intro()
		else:
			print(" ")
			print("Ok, thanks for playing! Hope you can come by again")
	


	elif Answer == 2:
		print("Current high scores are held by") #edit names when scores are submitted
		print(" ")
		print("1. Kyle Chung: 55")
		print(" ")
		print("2. Mr. Jugoon: 35")
		print(" ")
		print("3. Liam Woo: 30")
		print("What would you like to do?")
		print("Press 1 if you would like to exit the game")
		print("Press any other number if you would like to go back to the main menu")
		print(" ")
		highscoreanswer = int(input("Please pick one of the options above \n"))
		if highscoreanswer ==1:
			print("Ok, thank you for playing!")
		else:
			print(art)
			intro()
	else:
		print("That is not an option.")
		intro()
#Redeclare the questions after the question
	pass
def question1():
	Answer1 = int(input("What is your answer? \n"))
	print(" ")
	if Answer1 == 1:
		print(" ")
		print("Congratulations, you're correct!")
		score = score + 10
		print ("You have", score, "Points!")
	elif Answer1 == 2:
		print(" ")
		print("Sorry, you're incorrect. But keep on going!")
		print("You lose 5 points.")
		score = score - 5
		print ("You have", score, "Points!")
	elif Answer1 == 3:
			print(" ")
			print("That's ok! You still have many questions to go.")
			print("You don't lose any points!")
			print("You still have", score, "Points!")	
	else:
		print(" ")
		print("That is not an option, please try again.")
		print(" ")
	pass

def question2():
	Answer2 = int(input("What is your answer? \n"))
	if Answer2 == 2:
		print(" ")
		print("Congratulations you're correct!")
		score = score + 10
		print("You have", score, "Points!")
	elif Answer2 == 1:
		print(" ")
		print("Sorry, you're incorrect")
		score = score - 5
		print("You have", score, "Points!")
	elif Answer2 == 3:
		print(" ")
		print("That's ok! You still have many questions to go.")
		print("You still have ", score, "Points!")
	pass

def question3():
	Answer3 = int(input("What is your answer? \n"))
	if Answer3 == 1:
		print(" ")
		print("Congratulations you're correct!")
		print("You get 10 points!")
		score = score + 10
		print("You have", score, "Points!")
	elif Answer3 == 2:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	elif Answer3 == 3:
		print(" ")
		print("That is not an option, please try again.")
	pass
def question4():
	Answer4 = int(input("What is your answer? \n"))
	if Answer4 == 2:
		print(" ")
		print("Congratulations you're correct!")
		print("You get 10 points!")
		score = score + 10
		print("You have", score, "Points!")
	if Answer4 == 1:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	if Answer4 == 3:
		print(" ")
		print("That is not an option, please try again")
	pass	

def question5():
	Answer5 = int(input("What is your answer? \n"))
	if Answer5 == 2:
		print(" ")
		print("Congratulations you're correct!")
		print("You get 15 points!")
		score = score + 15
		print("You have", score, "Points!")
	elif Answer5 == 1:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	elif Answer5 == 3:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	else:
		print(" ")
		print("That is not an option, please try again")
	pass


# Declare variable for scorekeeping

score = 0

#Declare the art variables
art = """

 _  _  ____  __     ___  __   _  _  ____ 
/ )( \(  __)(  )   / __)/  \ ( \/ )(  __)
\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _) 
(_/\_)(____)\____/ \___)\__/ \_)(_/(____)
                ____  __  
               (_  _)/  \ 
                 )( (  O )
                (__) \__/  
   __   __   ____   __   ____  __  
 _(  ) / _\ (  _ \ / _\ (  _ \(  ) 
/ \) \/    \ ) _ (/    \ )   / )(  
\____/\_/\_/(____/\_/\_/(_/\_)(__) 
   __  _  _  _  _  ____  ____ 
 _(  )/ )( \( \/ )(  _ \/ ___)
/ \) \) \/ (/ \/ \ ) __/\___ \
							
\____/\____/\_)(_/(__)  (____/
	  __   _  _  __  ____  _   
	 /  \ / )( \(  )(__  )/ \  
	(  O )) \/ ( )(  / _/ \_/  
	 \__\)\____/(__)(____)(_)  	
"""
endart = """
  _____ _                 _    
 |_   _| |__   __ _ _ __ | | __
   | | | '_ \ / _` | '_ \| |/ /
   | | | | | | (_| | | | |   < 
   |_| |_| |_|\__,_|_| |_|_|\_\ 
 
 \ \ / /__  _   _ 
  \ V / _ \| | | |
   | | (_) | |_| |
   |_|\___/ \__,_|

  _____          
 |  ___|__  _ __ 
 | |_ / _ \| '__|
 |  _| (_) | |   
 |_|  \___/|_|   
  ____  _             _             _ 
 |  _ \| | __ _ _   _(_)_ __   __ _| |
 | |_) | |/ _` | | | | | '_ \ / _` | |
 |  __/| | (_| | |_| | | | | | (_| |_|
 |_|   |_|\__,_|\__, |_|_| |_|\__, (_)
                |___/         |___/   
"""                
print(art)
print("\n")
print(" ")
print("Press 1 to play the game")
print("Press 2 to view high scores")
print(" ")
print("Please pick one of the options above")
Answer = int(input("What would you like to do? \n"))
if Answer == 1:
	print("Let's get playing!") #put everything here onto line with original code
	print(" ")
	print("Throughout this game, if you think you don't know the question, just type 3 and you won't have any points removed or added")
	print("What was Jabari's first impression of the diving board?")
	print(" ")
	print("Press 1 if he thought it looked easy")
	print("Press 2 if he thought it looked scary")
	print("Press 3 if you're unsure")
	print(" ")
	print("Please pick one of the options above")
	print(" ")
	Answer1 = int(input("What is your answer? \n"))
	print(" ")
	if Answer1 == 1:
		print("Congratulations, you're correct!")
		score = score + 10
		print ("You have", score, "Points!")
	elif Answer1 == 2:
		print("Sorry, you're incorrect. But keep on going!")
		print("You lose 5 points.")
		score = score - 5
	elif Answer1 == 3:
			print(" ")
			print("That's ok! You still have many questions to go.")
			print("You don't lose any points!")
			print("You still have", score, "Points!")
	else:
		print("That is not an option, please try again.")
		question1()


	print(" ")
	print("What excuse does Jabari use to not go on the diving board?")
	print("Press 1 if he says that he's scared and he wants to wait a bit")
	print("Press 2 if he says that he's going to think of a special jump")
	print("Press 3 if you're not sure")
	print(" ")
	print("Please pick one of the options")
	print(" ")
	Answer2 = int(input("What is your answer? \n"))
	if Answer2 == 2:
		print("Congratulations you're correct!")
		score = score + 10
		print ("You have", score, "Points!")
	elif Answer2 == 1:
		print("Sorry, you're incorrect, but you still have many questions to go!")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	elif Answer2 == 3:
		print("That's ok! You still have many questions to go!")
		print("You have", score, "Points!")
	else:
		print("That is not an option, please try again.")
		print(" ")
		question2()
	print(" ")

	print("What was the second excuse that Jabari used to not go on the board")
	print("Press 1 if he wanted to stretch before hand")
	print("Press 2 if he wanted to get his mom to take a picture first")
	print("Press 3 if you're unsure")
	print(" ")
	print("Please pick one of the options above")
	print(" ")
	Answer3 = int(input("What is your answer? \n"))
	if Answer3 == 1:
		print(" ")
		print("Congratulations you're correct!")
		print("You get 10 points!")
		score = score + 10
		print("You have", score, "Points!")
	elif Answer3 == 2:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	elif Answer3 == 3:
		print(" ")
		print("That's ok! You still have many questions to go.")
		print("You don't lose any points!")
		print("You still have", score, "Points!")
	else:
		print(" ")
		print("That is not an option, please try again")
		question3()
	print(" ")
	print("How does his dad feel about being scared")
	print("Press 1 if he thinks that Jabari's being a coward and he should just do it")
	print("press 2 if he thinks that it's ok that Jabari is scared")
	print("Press 3 if you're unsure")
	print(" ")
	print("Please pick one of the options")
	print(" ")
	Answer4 = int(input("What is your answer? \n"))
	if Answer4 == 2:
		print(" ")
		print("Congratulations you're correct!")
		print("You get 10 points!")
		score = score + 10
		print("You have", score, "Points!")
	elif Answer4 == 1:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	elif Answer4 == 3:
		print(" ")
		print("That's ok! You still have many questions to go.")
		print("You don't lose any points!")
		print("You still have", score, "Points!")
	else:
		print(" ")
		print("That is not an option, please try again")
		question4()

	print(" ")	
	print("This is the final question")
	print("It will be harder but you will get more points if you get it right")
	print("What does Jabari say after he jumps off the diving board")
	print(" ")
	print("Press 1 if he says that it was scary and he's never doing it again")
	print("Press 2 if he's going to do go on another time but with a double back flip")
	print("Press 3 if he said that it was fun but it's time to go home")
	print("")
	print("Please pick one of the options above")
	print(" ")
	Answer5 = int(input("What is your answer? \n"))
	if Answer5 == 2:
		print(" ")
		print("Congratulations you're correct!")
		print("You get 15 points!")
		score = score + 15
		print("You have", score, "Points!")
	elif Answer5 == 1:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	elif Answer5 == 3:
		print(" ")
		print("Sorry, you're incorrect")
		print("You lose 5 points.")
		score = score - 5
		print("You have", score, "Points!")
	else:
		print(" ")
		print("That is not an option, please try again")
		question5()
	print(" ")
	print("That's the end!, you ended up with", score, "Points!")
	print(" ")
	print("Press 1 if you would like to play again")
	print("Press any other number if you are done playing")
	print(" ")
	ending = int(input("What would you like to do now? \n"))
	if ending == 1:
		print(" ")
		print("Great! Let's see if we can get a higher score!")
		print(art)
		intro()
	else:
		print(" ")
		print("Ok, thanks for playing! Hope you can come by again")
		print(endart)





elif Answer == 2:
	print("Current high scores are held by") #Add names for people who tested
	print(" ")
	print("1. Kyle Chung: 55")
	print(" ")
	print("2. Mr. Jugoon: 35")
	print(" ")
	print("3. Liam Woo: 30")
	print(" ")
	print("What would you like to do?")
	print("Press 1 if you would like to exit the game")
	print("Press any other number if you would like to go back to the main menu")
	print(" ")
	highscoreanswer = int(input("Please pick one of the options above \n"))
	if highscoreanswer == 1:
		print("Ok, thank you for playing!")
		print(endart)
	else:
		print(art)
		intro()
else:
	print(" ")
	print("That is not an option.")
	intro()