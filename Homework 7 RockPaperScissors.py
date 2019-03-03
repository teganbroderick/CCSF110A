#Tegan Broderick
#CS110A Homework 7
#Rock-Paper-Scissors game. User plays rock paper scissors against a computer.

import random

def userSelection():
  '''User selects scissors, paper or rock, function turns the input into all lower case letters, and returns the selection'''

  selection1 = input("Please enter your move: paper, rock, " + "or" + " scissors:")
  selection1 = selection1.lower()

  if selection1 == "scissor":
    selection1 = "scissors"

  return selection1

def computerSelection():
  '''Function generates a random integer between 1 and 3, and returns scissors, paper or rock based on the number generated'''

  selectionInteger = random.randrange(1, 4)

  if selectionInteger == 1:
    selection2 = "scissors"
  elif selectionInteger == 2:
    selection2 = "paper"
  else:
    selection2 = "rock"

  print("Computer's move is " + selection2)
  return selection2

def comparison(selection1, selection2):
  '''Function runs the rock-paper-scissors game. It compares the parameters, which are the returns from the above two functions, and outputs a result based on the rules of the game.'''

  if selection1 == selection2:
    print("Tie with " + selection1 + "!")
  elif selection1 == "scissors" and selection2 == "paper":
    print("You win! Scissors cut paper!!")
  elif selection1 == "scissors" and selection2 == "rock":
    print("Computer wins! Rock breaks scissors!!")
  elif selection1 == "paper" and selection2 == "scissors":
    print("Computer wins! Scissors cut paper!!")
  elif selection1 == "paper" and selection2 == "rock":
    print("You win! Paper covers rock!!")
  elif selection1 == "rock" and selection2 == "scissors":
    print("You win! Rock breaks scissors!!")
  elif selection1 == "rock" and selection2 == "paper":
    print("Computer wins! Paper covers rock!!")
  else:
    print("Invalid move!!")


def main():
  '''Main function which calls the above functions'''
  x = userSelection()
  y = computerSelection()

  comparison(x, y)

if __name__ == "__main__":
  main()


'''
Example 1:
Please enter your move: paper, rock, or scissors: PAPER
Computer's move is scissors
Computer wins! Scissors cut paper!!

Example 2:
Please enter your move: paper, rock, or scissors: rock
Computer's move is rock
Tie with rock!

Example 3:
Please enter your move: paper, rock, or scissors: scissor
Computer's move is paper
You win! Scissors cut paper!!

Example 4:
Please enter your move: paper, rock, or scissors: scissors
Computer's move is paper
You win! Scissors cut paper!!
'''
