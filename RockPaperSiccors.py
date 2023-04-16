import random
user = input("Enter'r'for rock, 'p' for paper, or 's' for scissors ")

computer = random.choice(['r', ' p', 's'])
x = ""
if computer == 'r':
    x = 'rock'
elif computer == 's':
    x = 'scissors'

else:
    x = 'paper'


if user == 'r' and computer == 's':
    print("The computer used scissors, so you won!")
elif user == 'p' and computer == 'r':
    print("The computer used rock, so you won!")
elif user == 's' and computer == 'p':
    print("The computer used paper, so you won")
elif user == 'r' and computer =='r':
    print("You both chose the smae thing so you tied")
elif user == 'p' and computer == 'p':
    print("You both chose the same thing so you tied")
elif user == 's' and computer == 's':
    print("The computer chose the same ting so yo both tied")
else:
    print(f"Computer selected {x} and you lost!")