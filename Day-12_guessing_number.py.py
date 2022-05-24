import random
import os
from art import logo
print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 to 100")
guess_correct = random.randint(1,100)
level  = input("Choose a difficulty. Type 'easy' or 'hard': ")
os.system('cls')
if level == 'easy':
  guess_count = 10
else:
  guess_count = 5
print(f"you have {guess_count} attempts remaining to guess the number")
while guess_count>0:
  guess = int(input("Make a guess: "))
  if guess == guess_correct:
    print(f"you got it! The answer is {guess_correct}.")
    break
    #print and break
  elif guess < guess_correct:
    guess_count = guess_count-1
    print("Too Low")
  else:
    guess_count = guess_count-1
    print("Too high")
  if guess_count>0:
    print(f"you have {guess_count} chances remaining to guess")
  else:
    print("You've run out of guesses, you lose.")

  