import customtkinter as ctk

def enter_clicked():
    print("")
    userName = entry.get()
    addString = adress.get()
    hey = textbox.get()
    strList = [hey, addString, userName]
    OM.configure(text='\n'.join(strList))



app = ctk.CTk()
app.title("MYFIRSTAPP")
app.geometry("800x700")

label = ctk.CTkLabel(app, text="Name: ", font=ctk.CTkFont(size=20))
label.grid(row=0, column=0, padx=5, pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Enter ur name",
                     font=ctk.CTkFont(size=20),
                     width=240, height=20)
entry.grid(row=0, column=1)

labelAdress = ctk.CTkLabel(app, text="Adress: ", font=ctk.CTkFont(size=20))
labelAdress.grid(row=1, column=0, padx=5, pady=5)

adress = ctk.CTkEntry(app, placeholder_text="Enter Your Adress",
                      font=ctk.CTkFont(size=20),
                      width=240, height=20)
adress.grid(row=1, column=1, padx=5, pady=5)
age = ctk.CTkLabel(app, text="Age:", font=ctk.CTkFont(size=20))
age.grid(row=2, column=0, padx=5, pady=5)

textbox = ctk.CTkEntry(app, placeholder_text="Enter your current age", font=ctk.CTkFont(size=20),
                       width=240, height=20)
textbox.grid(row=2, column=1)

btn = ctk.CTkButton(app, text="Enter", command= enter_clicked)
btn.grid(row=3, column=1, padx=5, pady=5)

OM = ctk.CTkLabel(app, text="strList", font=ctk.CTkFont(size=20))
OM.grid(row=3, column=2)





app.mainloop()