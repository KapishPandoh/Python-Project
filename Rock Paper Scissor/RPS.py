import random

moves = ["Rock","Paper","Scissors"]

keep_playing="true"

while(keep_playing == "true"):
    cmove = random.choice(moves)
    pmove=input("What us your move\nRock,Paper,Scissors ? = ")

    print("The computer chose = ",cmove)

    if(cmove==pmove):                                         #1
        print("Tie")
    elif(pmove=="Rock" and cmove=="Scissors"):                #2
        print("Player wins")
    elif(pmove=="Paper" and cmove=="Rock"):                   #3
        print("Player wins")
    elif (pmove == "Rock" and cmove == "Paper"):              #4
        print("Computer wins")
    elif (pmove == "Paper" and cmove == "Scissors"):           #5
        print("Computer wins")
    elif (pmove == "Scissors" and cmove == "Paper"):          #6
        print("Player wins")
    elif (pmove == "Scissors" and cmove == "Rock"):           #7
        print("Computer wins")

    print(" ")
    print("Enter 1 to continue or 0 to exit")
    x=int(input())
    if x==0:
        keep_playing="false"








