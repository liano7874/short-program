import random

secretnumber = random.randint(1, 20)
print("I'm thinking of a number between 1 and 20.")

for guessTaken in range(1, 6):
  print("Take a guess.")
  guess = int(input())
  less_num = guess - secretnumber

  if (less_num <= 2 and less_num > 0) or (less_num >= -2 and less_num < 0):
    print("Your guess almost right")
  elif guess < secretnumber:
    print("Your guess is too low.")
  elif guess > secretnumber:
    print("Your guess is too high")
  else:
    break

if guess == secretnumber:
  print("Good job! You guessed my number in " + str(guessTaken) + " guesses!")
else:
  print(f"Nope. The number I was thinking of was {str(secretnumber)}")
