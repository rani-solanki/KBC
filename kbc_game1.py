question_list = [
    "Q-1. How many continents are there?",  #first question
	"Q-2. What is the capital of India?",   #second question
	"Q-3. NG mei kaun se course padhaya jaata hai?"  #third question
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
options_list2 =[["3.Seven", "4.Eight"],
                ["3.Chennai", "4.Delhi"],
                ["2.Counseling", "3.Software Engineering"]
]
# index for print question list
index = 0
while(index <len(question_list)):
	print(index+1,question_list[index])
	# take loop for option list
	j= 0
	while(j<=len(question_list)):
		print(j+1,options_list[index][j])
		j=j+1
	index=index+1