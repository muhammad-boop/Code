# ! Snake water and Gun Game
import random
'''
sanke = 1
water = -1
gun = 0
'''
computer = random.choice([-1, 0 , 1])
youstr = input("Enter Your Choice: ")
yoDict = {"g":0,"s":1,"w":-1}
reversedDict = {0:"Gun",1:"Snake",-1:"Water"}
you = yoDict[youstr]
print(f"You have chosed {reversedDict[you]} and Computer has chosed {reversedDict[computer]} ")
if(computer == you):
  print("Its a Draw!")
else:
  if(computer == 0 and you == 1):
    print("Computer Won!")
  elif(computer ==0 and you ==-1):
    print("You Won!")
  elif(computer ==1 and you==-1):
    print("Computer Won!")
  elif(computer ==1 and you==0):
    print("You Won!")
  elif(computer ==-1 and you==0):
    print("Computer Won!")
  elif(computer ==-1 and you==1):
    print("You Won!")