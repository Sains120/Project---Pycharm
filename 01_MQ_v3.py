"""Component one - Instructions - v3
player can put uppercase, lowercase, or y/n
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
