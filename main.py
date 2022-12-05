import random

#random number, no seed
random.seed() 

comp_player = [] 
x = 0 

#adding elements to comp_player list
while x <= 2: 
  new_element = int(random.randint(0,100)) 
  comp_player.append(new_element) 
  x += 1 


#initialize scores
comp_player_score = 0
player_score = 0 
i = 0

#while iteration for player input and point add/subtract 
while i <= 2: 
  number_guess = int(input("Guess a number between 1 to 100:"))
  
  if number_guess >= comp_player[i]: 
    player_score += 1 
    i += 1 
  else: 
    comp_player_score += 1 
    i += 1 


player_name = "Daniel"

#print results
if player_score > comp_player_score: 
  print(player_name + " has won!")
else: 
  print(player_name + " has lost") 

print("Player Score: " + str(player_score)) 
print("Computer Score: " + str(comp_player_score) + "\n")

#not on assignment but wanted to add to show game works 
print("Computer's numbers: " + str(comp_player))
