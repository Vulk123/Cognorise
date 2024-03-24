import random
game_list = [ 'Rock','Paper','Scissor']
computer = c = 0
command = p = 0
print("Score: Computer" + str(c) + "Player" + str(p))
#the loop
run = True
while run :
    computer_choice = random.choice(game_list)
    command = input("Rock, Paper, Scissor or Quit :")
    if command == computer_choice:
        print("Tie")
    elif command == 'Rock':
        if computer_choice == 'Scissor':
             print("Player won!")
             p += 1
        else:
             print("computer won!")
             c += 1    
elif command == 'Paper':
    if command == 'Rock':
        print("Player won!")
        p +
