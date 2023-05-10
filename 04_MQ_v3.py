"""Component four - Statement formatter - v3
Program works with uppercase, lowercase, and y/n
"""


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
