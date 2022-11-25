import random
import os


options = ("rock", "paper", "scissors")
computer = random.choice(options)
playing= True
p=0
c=0
res=f'''
----------------[Score card]------------------
\t\tYou\t\t\tComputer
\t\t{p}\t\t\t{c}
----------------------------------------------
'''

os.system('cls')
while playing:
    player=''
    res=f'''
    ----------------[Score card]------------------
    \t\tYou\t\t\tComputer
    \t\t{p}\t\t\t{c}
    ----------------------------------------------
    '''
    print(res)
    while player not in options:
        player = input("Enter a choice (rock , paper ,scissors): ")
    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player==computer:
        print("It's a Tie")
    elif player =="rock" and computer=="scissors":
        print("You win!")
        p+=1
    elif player =="paper" and computer=="rock":
        print("You Win!")
        p+=1
    elif player =="scissors" and computer=="paper":
        print("You win!")
        p+=1
    else:
        print("You lose!")
        c+=1
    
    if input("Want to play again? (y/n)")!="y":
        playing=False
    os.system('cls')
print(res+'\n'+"\t\tThanks for playing\n"+'-'*60)
