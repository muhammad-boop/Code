# ! Guess the number game ..
import random
n = random.randint(1, 100)
a = -1
guess = 1
while(a!=n):
  a = int(input("Enter a Number: "))
  if(a>n):
    print("Enter a Lower Please")
    guess+=1
  elif(a<n):
    print("Enter a Higher Please")
    guess+=1
print(f"You guessed {n} it right in {guess} guesses")