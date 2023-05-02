import customtkinter as ctk
import random

def enter_clicked():
    print("")
    strList = ["You chose", user]
    comList = ["The computer chose", x, ", so you won"]
    numList = ["the computer chose", x, ", so you tied"]
    idkList = ["The computer chose", x, ", so you lost"]
    OM.configure(text='\n'.join(strList))
    hey.configure(text='\n'.join(comList))
    tag.configure(text='\n'.join(numList))
    Really.configure(text='\n'.join(idkList))

app = ctk.CTk()
app.title("RockPaperScissorsShoot")
app.geometry("800x700")
computer = random.choice(['r', ' p', 's'])
x = ""
if computer == 'r':
    x = 'rock'
elif computer == 's':
    x = 'scissors'

else:
    x = 'paper'

user = input("Enter rock, paper, or scissors ")

OM = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
OM.grid(row=1, column=0)

btn = ctk.CTkButton(app, text="Click", command= enter_clicked)
btn.grid(row=0, column=0, padx=5, pady=5)

hey = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
hey.grid(row=3, column=0)

tag = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
tag.grid(row=3, column=0)

Really = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
Really.grid(row=3, column=0)

if user == 'rock' and computer == 's':
    hey = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
    hey.grid(row=3, column=0)
elif user == 'paper' and computer == 'r':
    hey = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
    hey.grid(row=3, column=0)
elif user == 'scissors' and computer == 'p':
    hey = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
    hey.grid(row=3, column=0)
elif user == 'rock' and computer =='r':
    tag = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
    tag.grid(row=3, column=0)
elif user == 'paper' and computer == 'p':
    tag = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
    tag.grid(row=3, column=0)
elif user == 'scissors' and computer == 's':
    tag = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
    tag.grid(row=3, column=0)
else:
    Really = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
    Really.grid(row=3, column=0)

app.mainloop()