"""Component two - Generate Question - v2
Generate the questions and say if wrong or right
Uppercase and lowercase work
"""


# list of questions
question_one = "What is number one in Māori? "
question_two = "What is number two in Māori? "
question_three = "What is number three in Māori? "
question_four = "What is number four in Māori? "
question_five = "What is number five in Māori? "
question_six = "What is number six in Māori? "
question_seven = "What is number seven in Māori? "
question_eight = "What is number eight in Māori? "
question_nine = "What is number nine in Māori? "
question_ten = "What is number ten in Māori? "

# questions answers
answer_one = (input(question_one))
if answer_one == "tahi" or answer_one == "Tahi":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was tahi. \n")


answer_two = (input(question_two))
if answer_two == "rua" or answer_two == "Rua":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was rua. \n")

answer_three = (input(question_three))
if answer_three == "toru" or answer_three == "Toru":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was toru. \n")

answer_four = (input(question_four))
if answer_four == "whā" or answer_four == "Whā" or \
        answer_four == "wha" or answer_four == "Wha":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was whā. \n")

answer_five = (input(question_five))
if answer_five == "rima" or answer_five == "Rima":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was rima. \n")

answer_six = (input(question_six))
if answer_six == "ono" or answer_six == "Ono":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was ono. \n")

answer_seven = (input(question_seven))
if answer_seven == "whitu" or answer_seven == "Whitu":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was whitu. \n")

answer_eight = (input(question_eight))
if answer_eight == "waru" or answer_eight == "Waru":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was waru. \n")

answer_nine = (input(question_nine))
if answer_nine == "iwa" or answer_nine == "Iwa":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was iwa. \n")

answer_ten = (input(question_ten))
if answer_ten == "tekau" or answer_ten == "Tekau":
    print("That's correct! Good job! \n")
else:
    print("That's incorrect. Nice try. Answer was tekau. \n")
