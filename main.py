# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

def play():
    playerSelection = input("'r' for rock, 'p' for paper, 's' for scissors: ")
    compSelection = random.choice(['r','p','s'])

    if compSelection == playerSelection:
        print(f"It's a tie, both players hit {compSelection}. Please reroll")
        play()
    else:
        if compSelection == 'r' and playerSelection == 'p':
            print(f"Comp hit {compSelection}, player hit {playerSelection}. Player wins")
        elif compSelection == 'r' and playerSelection == 's':
            print(f"Comp hit {compSelection}, player hit {playerSelection}. Comp wins")
        elif compSelection == 'p' and playerSelection == 's':
            print(f"Comp hit {compSelection}, player hit {playerSelection}. Player wins")
        elif compSelection == 'p' and playerSelection == 'r':
            print(f"Comp hit {compSelection}, player hit {playerSelection}. Comp wins")
        elif compSelection == 's' and playerSelection == 'r':
            print(f"Comp hit {compSelection}, player hit {playerSelection}. Player wins")
        elif compSelection == 's' and playerSelection == 'p':
            print(f"Comp hit {compSelection}, player hit {playerSelection}. Comp wins")


if __name__ == '__main__':
    play()

