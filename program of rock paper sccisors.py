import random
player=''
name=input("enter the name:")
while name.isdigit()==True and len(name)<4:
    name=input("please consider your name:")
print("User name:",name)
age=input("enter the age:")
while age.isalpha()==True and len(age)>18:
    age=input("please consider your name:")
print("User age:",age)
password=input("enter the password:")
if password=='admin':
    password=("enter the password:")
def menu():
    print("MENU,\n 1-PLAY GAME\n 2-HIGH SCORE\n 3-QUIT")
    choice=input("enter the choice:")
    if choice==1:
        print("Let's play")
    if choice==2:
        print("high score")
    if choice==3:

        print("quit")


while player != 'q':

    sum=0
    print('enter the choice:')
    print('R or r for rock\n P or p for paper\n S for scissors\n Q or q  to quit')
    player=input('')
    player.lower()
    select = 'rps'
    if player == 'q':
        break
    if player not in select:
        print('invalid choice')
        continue
    player=select.find(player)
    comp=random.randrange(1,4)
    select = ['rock', 'paper', 'scissors']
    print('Computer picked:', [comp])
    if player == 'r':
        player=1
    elif player == 'p':
        player=2
    elif player == 's':
        player=3
    if comp==1:
        choice='rock'
    elif comp==2:
        choice='paper'
    elif comp==3:
        choice='scissors'
    if player==1 and comp==3:
        sum = sum+1
        print("You win against comp\n"+"score is ",sum)
    elif player==3 and comp==1:

        print("You lose against comp\n")
    #elif player < comp:

        print("You lost against comp\n")
    #elif player > comp:
        sum = sum+1
        print("You win against comp\n")
    elif player==comp:
        print("You tie the against comp\n")
    else:
        print("Try again")
        print("Your Score:",sum)











