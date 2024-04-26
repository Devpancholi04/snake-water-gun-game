import random
score = 0
def user():
    global score
    user_input = int(input('''enter your choice : 
                       press 1 for SNAKE__(1) : 
                       press 2 for WATER__(2) : 
                       press 3 for GUN__(3) : 
                       : '''))

    if(user_input == 1):
        if(user_input == 1 and computer == 'SNAKE'):
            print(f"MATCH DRAW because computer has choseen {computer}")
            score = score + 0
        elif(user_input == 1 and computer == 'WATER'):
            print(f"USER WON because computer has choseen {computer}")
            score = score + 1
        elif(user_input == 1 and computer == 'GUN'):
            print(f"COMPUTER WON because computer has choseen {computer}")
            score = score - 1

    elif(user_input == 2):
        if(user_input == 2 and computer == 'SNAKE'):
            print(f"COMPUTER WON because computer has choseen {computer}")
            score = score - 1
        elif(user_input == 2 and computer == 'WATER'):
            print(f"MATCH DRAW because computer has choseen {computer}")
            score = score + 0
        elif(user_input == 2 and computer == 'GUN'):
            print(f"USER WON because computer has choseen {computer}")
            score = score + 1

    elif(user_input == 3):
        if(user_input == 3 and computer == 'SNAKE'):
            print(f"USER WON because computer has choseen {computer}")
            score = score + 1
        elif(user_input == 3 and computer == 'WATER'):
            print(f"COMPUTER WON because computer has choseen {computer}")
            score = score - 1
        elif(user_input == 3 and computer == 'GUN'):
            print(f"MATCH DRAW because computer has choseen {computer}")
            score = score + 0
    else:
        print("invalid input")


print("RULES OF GAME : ")
print(''' if match draw then you will get 0 point
        if match will be won by user then you will get +1 point 
        if match will be won by computer then you will get -1 point
      \n''')
while True:
    possible_outcome = ['SNAKE','WATER', 'GUN']
    computer = random.choice(possible_outcome)
    user()
    print(f"your score is : {score}")