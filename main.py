import random

rock = "rock"
paper = "paper"
scissors = "scissors"

humanchoice = input("Pick rock paper or scissors: ")
humanchoice = humanchoice.lower()
aichoice = random.randint(1, 3)

if aichoice == 1:
    if humanchoice == rock:
        print(f"You tied, AI picked rock, you picked {humanchoice}")
    elif humanchoice == paper:
        print(f"You won, AI picked rock, you picked {humanchoice}")
    elif humanchoice == scissors:
        print(f"You lost, AI picked rock, you picked {humanchoice}")

elif aichoice == 2:
    if humanchoice == rock:
        print(f"You lost, AI picked paper, you picked {humanchoice}")
    elif humanchoice == paper:
        print(f"You tied, AI picked paper, you picked {humanchoice}")
    elif humanchoice == scissors:
      
        print(f"You won, AI picked paper, you picked {humanchoice}")

elif aichoice == 3:
    if humanchoice == rock:
        print(f"You won, AI picked scissors, you picked {humanchoice}")
    elif humanchoice == paper:
        print(f"You lost, AI picked scissors, you picked {humanchoice}")
    elif humanchoice == scissors:
        print(f"You tied, AI picked scissors, you picked {humanchoice}")