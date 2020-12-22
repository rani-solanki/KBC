question_list = [
	# first qouestion
    "Q-1. How many continents are there?",
	# second question
	"Q-2. What is the capital of India?",
	# third question
	"Q-3. NG mei kaun se course padhaya jaata hai?"  
]
options_list = [
    # options of first questions
	["1.Four", "2.Nine", "3.Seven", "4.Eight"],
	# options of second questions
	["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
	# options of third questions
	["1.Tourism", "2.Counseling", "3.Software Engineering", "4.Agriculture"]
	]
solution_list = [3, 4, 3]
options_list2 =[["3.Seven", "4.Eight"],["3.Chennai", "4.Delhi"],["2.Counseling", "3.Software Engineering"]]

index = 0
incre = 0
counter = 0
while index < len(question_list):
	print(question_list[index])
	iterate = 0
	# another loop for options_list
	while iterate < len(options_list[index]):
		print(options_list[index][iterate])
		# increment of options_list
		iterate = iterate + 1
	user_input = int(input("which option is right: "))
	if user_input == solution_list[index]:
		print("congrats your answer is right")
	elif user_input == 5050:
		if counter < 1:
			counter = counter + 1
			while incre < len (options_list2[index]):
				print(options_list2[index][incre])
				incre = incre + 1
			user_input2 = int(input("write your option: "))
			if user_input2 == solution_list[index]:
				print("congrats your answer is right")
			else:
				print("sadly,better luck next time")
				break
		else:
			increment = 0
			print("you allready took lifeline")
			while increment < len (options_list[index]):
				print(options_list[index][increment])
				increment = increment + 1
			user_input3 = int(input("select your option: "))
			if user_input3 == solution_list[index]:
				print("congrats your answer is right")
			else:
				print("sadly,better luck next time")
	else:
		print("sadly,better luck next time")
		break	
	index = index + 1