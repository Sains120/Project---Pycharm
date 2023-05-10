"""Component four - Statement formatter - v2
Program gives end summary and asks if player
would like to play again
"""

print("Good job. You got - out of 10. \n")
play_again = input("Would you like to play again? ")

if play_again == "yes":
    print("Questions again")
elif play_again == "no":
    print("*****Thanks for playing the Maori Number Quiz!*****")
else:
    print("Please enter yes or no. ")
    print(input("Would you like to play again? "))
