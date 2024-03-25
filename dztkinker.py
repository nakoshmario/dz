# from tkinter import *

# root = Tk()
# # root.title('Hello world')
# root.geometry('400x300')
# root.resizable(0,1)



# count = 0

   


# def yellow():
#     global count 
#     count += 1
#     print(count)
#     if count > 10:
#         lab['text'] = 'red'
#         btn2.config(bg='red')




# lab = Label(root)
# lab.pack(fill='x')
# entry = Entry(root)
# entry.pack(fill='x')


# btn2 = Button(root, command=yellow,bg='yellow')
# btn2.pack(fill='x')

# mainloop()


# -------------------------------------


import tkinter as tk
import random



root = tk.Tk()
root.title("камень, ножници, бумага")



label = tk.Label(root, text="ваш выбор:")
label.pack()

rock_button = tk.Button(root, text="камень", command=lambda: game("камень"))
rock_button.pack()

paper_button = tk.Button(root, text="бумага", command=lambda: game("бумага"))
paper_button.pack()

scissors_button = tk.Button(root, text="ножницы", command=lambda: game("ножницы"))
scissors_button.pack()


def game(user_choice):
    computer_choice = random.choice(["камень", "бумага", "ножницы"])
    result = opciton_winner(user_choice, computer_choice)
    message = f"вы выбрали {user_choice.capitalize()}.\n компуктер выбрал {computer_choice.capitalize()}.\n{result}"
    result_label = tk.Label(root, text=message)
    result_label.pack()


def opciton_winner(user, computer):
    if user == computer:
        return "ничья!"
    elif (user == "камень" and computer == "ножницы") or \
         (user == "ножницы" and computer == "бумага") or \
         (user == "бумага" and computer == "камень"):
        return "победа!"
    else:
        return "компуктер выйграл!"

root.mainloop()