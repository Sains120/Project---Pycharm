"""Component one - Instructions - v1
player will be asked if they have played before,
if not instructions will show
"""

print("***Maori Number Quiz***")
answer = (input("\nHave you played before? "))

if answer == "yes":
    print("Game begins...")
elif answer == "no":
    print("instructions")
else:
    print(input("Please enter yes or no: "))
