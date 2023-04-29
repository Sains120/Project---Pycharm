"""Component one - Instructions - v2
player can enter lowercase or uppercase
"""


print("***Maori Number Quiz***")
answer = (input("\nHave you played before? "))

if answer == "yes" or "Yes":
    print("Game begins...")
elif answer == "no" or "No":
    print("instructions")
else:
    print(input("Please enter yes or no: "))
