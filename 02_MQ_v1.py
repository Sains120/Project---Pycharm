"""Component two - Randomly Generate Question - v1
Randomly generate the questions and
say if wrong or right
"""

import random

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

question = random.choice([question_one, question_two, question_three,
                          question_four, question_five, question_six, question_seven,
                          question_eight, question_nine, question_ten])


answer_one = (input(question_one))
answer_two = (input(question_two))
answer_three = (input(question_three))
answer_four = (input(question_four))
answer_five = (input(question_five))
answer_six = (input(question_six))
answer_seven = (input(question_seven))
answer_eight = (input(question_eight))
answer_nine = (input(question_nine))
answer_ten = (input(question_ten))

if answer_one != "tahi":
    print("That's incorrect. Nice try. Answer was tahi. ")
else:
    print("That correct! Good job! ")

if answer_two != "rua":
    print("That's incorrect. Nice try. Answer was rua. ")
else:
    print("That correct! Good job! ")

if answer_three != "toru":
    print("That's incorrect. Nice try. Answer was toru. ")
else:
    print("That correct! Good job! ")

if answer_four != "whā":
    print("That's incorrect. Nice try. Answer was whā. ")
else:
    print("That correct! Good job! ")

if answer_five != "rima":
    print("That's incorrect. Nice try. Answer was rima. ")
else:
    print("That correct! Good job! ")

if answer_six != "ono":
    print("That's incorrect. Nice try. Answer was ono. ")
else:
    print("That correct! Good job! ")

if answer_seven != "whitu":
    print("That's incorrect. Nice try. Answer was whitu. ")
else:
    print("That correct! Good job! ")

if answer_eight != "waru":
    print("That's incorrect. Nice try. Answer was waru. ")
else:
    print("That correct! Good job! ")

if answer_nine != "iwa":
    print("That's incorrect. Nice try. Answer was iwa. ")
else:
    print("That correct! Good job! ")
    
if answer_ten != "tekau":
    print("That's incorrect. Nice try. Answer was tekau. ")
else:
    print("That correct! Good job! ")
