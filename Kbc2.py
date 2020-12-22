question_list = [
	# question first
    "Q-1. How many continents are there?",
	#second question 
	"Q-2. What is the capital of India?",
	#third question
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
while(index <len(question_list)):
	print(index+1,question_list[index])
	j= 0
	while(j<=len(question_list)):
		print(j+1,options_list[index][j])
		j=j+1
	a=int(input("enter the number:"))
	if (a == solution_list[index]):
		print("congret")
	else:
		print("wrong answere")
		break
	index=index+1
