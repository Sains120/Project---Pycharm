""" MQ base - v1
"""

# ask the player if they have played before
print("***Māori Number Quiz***")
answer = (input("\nHave you played before? "))

if answer == "yes" or answer == "Yes" \
        or answer == "y" or answer == "Y":
    print("Game begins...")
elif answer == "no" or answer == "No" \
        or answer == "n" or answer == "N":
    print("instructions")
else:
    print(input("Please enter yes or no: "))


points = 0

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
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was tahi. \n")


answer_two = (input(question_two))
if answer_two == "rua" or answer_two == "Rua":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was rua. \n")

answer_three = (input(question_three))
if answer_three == "toru" or answer_three == "Toru":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was toru. \n")

answer_four = (input(question_four))
if answer_four == "whā" or answer_four == "Whā" or \
        answer_four == "wha" or answer_four == "Wha":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was whā. \n")

answer_five = (input(question_five))
if answer_five == "rima" or answer_five == "Rima":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was rima. \n")

answer_six = (input(question_six))
if answer_six == "ono" or answer_six == "Ono":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was ono. \n")

answer_seven = (input(question_seven))
if answer_seven == "whitu" or answer_seven == "Whitu":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was whitu. \n")

answer_eight = (input(question_eight))
if answer_eight == "waru" or answer_eight == "Waru":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was waru. \n")

answer_nine = (input(question_nine))
if answer_nine == "iwa" or answer_nine == "Iwa":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was iwa. \n")

answer_ten = (input(question_ten))
if answer_ten == "tekau" or answer_ten == "Tekau":
    points += 1
    print("That's correct! Good job! \n")
else:
    points += 0
    print("That's incorrect. Nice try. Answer was tekau. \n")

print(f"You got {points} right out of 10. Good job. ")

print("Good job. You got - out of 10. \n")
play_again = input("Would you like to play again? ")

if play_again == "yes" or play_again == "Yes" \
        or play_again == "y" or play_again == "Y":
    print("Questions again")
elif play_again == "no" or play_again == "No"\
        or play_again == "n" or play_again == "N":
    print("*****Thanks for playing the Maori Number Quiz!*****")
else:
    print("Please enter yes or no. ")
    print(input("Would you like to play again? "))
