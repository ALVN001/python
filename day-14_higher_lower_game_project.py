import art
import os
import game_data as g
import random
isUser_true = True
score = 0
os.system('cls')
print(art.logo)
i = int(random.randint(0,len(g.data)-1))
j = int(random.randint(0,len(g.data)-1))
if g.data[i]['follower_count']>g.data[j]['follower_count']:
  low = j
else:
  low = i
print(f"Compare A : {g.data[i]['name']}, {g.data[i]['description']},from {g.data[i]['country']}")
print(art.vs)
print(f"Against B : {g.data[j]['name']}, {g.data[j]['description']},from {g.data[j]['country']}")
user_ans = input("Who has more followers? Type 'A' or 'B': ")
if g.data[i]['follower_count'] < g.data[j]['follower_count']:
    actual_ans = 'B'
else:
    actual_ans = 'A'

if user_ans ==actual_ans:
  score +=1
  while(isUser_true):
    os.system('cls')
    print(art.logo)
    print(f"You're right! Current score: {score}.")
    #i = int(random.randint(0,len(g.data)-1))
    j = int(random.randint(0,len(g.data)-1))
    print(f"Compare A : {g.data[low]['name']}, {g.data[low]['description']},from {g.data[low]['country']}")
    if g.data[low]['follower_count'] < g.data[j]['follower_count']:
      actual_ans = 'B'
    else:
      actual_ans = 'A'
    print(art.vs)
    print(f"Against B : {g.data[j]['name']}, {g.data[j]['description']},from {g.data[j]['country']}")
    user_ans = input("Who has more followers? Type 'A' or 'B': ")
    if user_ans != actual_ans:
      os.system('cls')
      print(art.logo)
      print(f"Sorry, that's wrong. Final score: {score}")
      isUser_true = False
    else:
      if g.data[low]['follower_count']>g.data[j]['follower_count']:
        low = j
      score+=1

else:
  os.system('cls')
  print(art.logo)
  print(f"Sorry, that's wrong. Final score: {score}")

