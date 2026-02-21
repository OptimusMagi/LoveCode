import tkinter as tk
from random import randint

def move_no(event):
    no_button.place(x=randint(0, 300), y=randint(0, 200))

root = tk.Tk()
root.title("A Second Chance?")
root.geometry("400x300")
root.configure(bg='pink')

label = tk.Label(root, text="Hey [Her Name], will you give us another shot? ❤️\nRemember our [personal memory]?", bg='pink', font=('Arial', 14))
label.pack(pady=20)

yes_button = tk.Button(root, text="Yes", command=lambda: tk.Label(root, text="YAY! Let's talk. 😊", font=('Arial', 16), bg='pink').pack())
yes_button.pack(side='left', padx=50)

no_button = tk.Button(root, text="No")
no_button.bind("<Enter>", move_no)
no_button.pack(side='right', padx=50)

root.mainloop()