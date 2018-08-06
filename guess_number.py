
import random
# get guess
def get_guess():
  return input("What is your guess: ")

# generate computer code
def generate_code():
  digits=[str(num) for num in range(10)]
  #shuffle the digits
  random.shuffle(digits)
  #grab the first three
  return digits[:3]

# generate the clues
def generate_clues(random_num, user_guess):
  if user_guess==random_num:
    return 'Number Cracked'
  clues=[]
  for ind,num in enumerate(user_guess):
    if num == random_num[ind]:
      clues.append("Match")
    elif num in random_num:
      clues.append("Close")
  if clues == []: 
    return "Nope"
  else:
    return clues

# run game logic
print("Welcome Guess Game")
random_num= generate_code()
clue_report=[]
while clue_report != "Number Cracked":
  guess=get_guess()
  clue_report=generate_clues(guess,random_num)
  print("Here is the result of your guess: ")
  for clue in clue_report:
    print(clue)



#hit1
# x=get_guess()
# print(x)

#hint2
# l1 = ["eat","sleep","repeat"]
# l2= ["sleep","repeat","eat"]
# for count,ele in enumerate(l1):
#   print(count,ele)
#   print (ele in l2)