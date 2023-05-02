"""Component two - Randomly Generate Question - v1
Randomly generate the questions and
say if wrong or right
"""

import random

# list of questions
questions = [
    1., "What is number one in Māori? ",
    2., "What is number two in Māori? ",
    3., "What is number three in Māori? ",
    4., "What is number four in Māori? ",
    5., "What is number five in Māori? ",
    6., "What is number six in Māori? ",
    7., "What is number seven in Māori? ",
    8., "What is number eight in Māori? ",
    9., "What is number nine in Māori? ",
    10., "What is number ten in Māori? "
    ]


question = random.choice(questions)

print(input(question))


if 1. in questions == "tahi":
    print("That's correct! Good job!")
elif 2. in questions == "rua":
    print("That's correct! Good job!")
elif 3. in questions == "toru":
    print("That's correct! Good job!")
elif 4. in questions == "whā":
    print("That's correct! Good job!")
elif 5. in questions == "rima":
    print("That's correct! Good job!")
elif 6. in questions == "ono":
    print("That's correct! Good job!")
elif 7. in questions == "whitu":
    print("That's correct! Good job!")
elif 8. in questions == "waru":
    print("That's correct! Good job!")
elif 9. in questions == "iwa":
    print("That's correct! Good job!")
elif 10. in questions == "tekau":
    print("That's correct! Good job!")
else:
    print("That's incorrect. Nice try.")
