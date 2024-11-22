import tkinter
import random

root = tkinter.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("400x500")

random_number = random.randint(1, 3)
if random_number == 1:
    computer_choice = "R"
elif random_number == 2:
    computer_choice = "P"
elif random_number == 3:
    computer_choice = "S"

rock_image = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper_image = """

     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)"""

scissors_image = """
    _______
---'   ____)____
          ______)   
       __________)   
      (____)
---.__(___)"""


def rock():
    label_user_choice['text'] = rock_image
    
    if computer_choice == "R":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "S":
        label_result['text'] = "You Won!"
        label_computer_choice['text'] = scissors_image
    
def paper():
    label_user_choice['text'] = paper_image
    
    if computer_choice == "P":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = paper_image
    elif computer_choice == "S":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = scissors_image
    elif computer_choice == "R":
        label_result['text'] = "You Won!"
        label_computer_choice['text'] = rock_image
    
def scissors():
    label_user_choice['text'] = scissors_image
    
    if computer_choice == "S":
        label_result['text'] = "TIE"
        label_computer_choice['text'] = scissors_image
    elif computer_choice == "R":
        label_result['text'] = "Computer wins!"
        label_computer_choice['text'] = rock_image
    elif computer_choice == "P":
        label_result['text'] = "You Won!"
        label_computer_choice['text'] = paper_image
    
def reset():
    global computer_choice
    random_number = random.randint(1, 3)
    if random_number == 1:
        computer_choice = "R"
    elif random_number == 2:
        computer_choice = "P"
    elif random_number == 3:
        computer_choice = "S"
        
    label_computer_choice['text'] = ""
    label_user_choice['text'] = ""
    label_result['text'] = "Enter Player's Choice!!"


button_rock = tkinter.Button(root, text="Rock", command = rock,bg="Gray")
button_rock.pack()

button_paper = tkinter.Button(root, text="Paper", command = paper,bg="Yellow")
button_paper.pack()

button_scissors = tkinter.Button(root, text="Scissors", command = scissors,bg="red")
button_scissors.pack()

label_computer_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
label_computer_choice.pack()

label_user_choice = tkinter.Label(root, justify=tkinter.LEFT, font="Courier", text="")
label_user_choice.pack()

label_result = tkinter.Label(root, text="Enter Player's Choice!!")
label_result.pack()

button_reset = tkinter.Button(root, text="Reset", command = reset,bg="green")
button_reset.pack()

root.mainloop()