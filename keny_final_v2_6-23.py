from tkinter import *
from tkinter import messagebox
import pygame.mixer

sounds = pygame.mixer
sounds.init()
correct_s = sounds.Sound("correct.wav")
wrong_s = sounds.Sound("wrong.wav")

def question_1():

	if depot.get()=="Kelly Slater" and country.get()=="USA":
		correct_s.play()
		messagebox.showinfo('Question 1', "You are Right")

	elif depot.get()=="Gabriel Medina" and country.get()=="Brazil":
		correct_s.play()
		messagebox.showinfo('Question 1', "You are Right")

	elif depot.get()=="Jordy Smith" and country.get()=="Africa":
		correct_s.play()
		messagebox.showinfo('Question 1', "You are Right")

	else:
		wrong_s.play()
		messagebox.showinfo('Question 1', "You are Wrong")


def question_2():

	if depot.get() == "Kelly Slater" and food.get() == "mahi":
		correct_s.play()
		messagebox.showinfo('Question 2', "You are Right")

	elif depot.get() == "Gabriel Medina" and food.get() == "feijoada":
		correct_s.play()
		messagebox.showinfo('Question 2', "You are Right")

	elif depot.get() == "Jordy Smith" and food.get() == "corn":
		correct_s.play()
		messagebox.showinfo('Question 2', "You are Right")

	else:
		wrong_s.play()
		messagebox.showinfo('Question 2', "You are Wrong")

def question_3():

	if depot.get() == "Kelly Slater" and trick.get() == "360":
		correct_s.play()
		messagebox.showinfo('Question 3', "You are Right")

	elif depot.get() == "Gabriel Medina" and trick.get() == "cutback":
		correct_s.play()
		messagebox.showinfo('Question 3', "You are Right")

	elif depot.get() == "Jordy Smith" and trick.get() == "floater":
		correct_s.play()
		messagebox.showinfo('Question 2', "You are Right")

	else:
		wrong_s.play()
		messagebox.showinfo('Question 3', "You are Wrong")

def question_4():

	if depot.get() == "Kelly Slater" and winning.get() == "2012":
		correct_s.play()
		messagebox.showinfo('Question 4', "You are Right")

	elif depot.get() == "Gabriel Medina" and winning.get() == "2021":
		correct_s.play()
		messagebox.showinfo('Question 4', "You are Right")

	elif depot.get() == "Jordy Smith" and winning.get() == "2019":
		correct_s.play()
		messagebox.showinfo('Question 4', "You are Right")

	else:
		wrong_s.play()
		messagebox.showinfo('Question 4', "You are Wrong")

def read_depots(file):
	depots = []
	depots_f = open(file)
	for line in depots_f:
		depots.append(line.rstrip())
	return depots

app = Tk()
app.title('Let`s surf')
Label(app, text="WSL 2021:").pack()
depot = StringVar()
depot.set(None)
options = read_depots("surfers1.txt")
OptionMenu(app, depot, *options).pack()

country = StringVar()
country.set(None)

#question 1
Label(app, text="What is the surfer country?").pack()
Radiobutton(app,variable = country, text = "USA" , value = "USA").pack()
Radiobutton(app,variable = country, text = "Brazil" , value = "Brazil").pack()
Radiobutton(app,variable = country, text = "Africa " , value = "Africa").pack()
Button(app, text = "Play Question 1", command = question_1).pack()

food = StringVar()
food.set(None)

Label(app, text="What is the favorite food?").pack()
Radiobutton(app,variable = food, text = "Feijoada" , value = "feijoada").pack()
Radiobutton(app,variable = food, text = "Mahi Mahi" , value = "mahi").pack()
Radiobutton(app,variable = food, text = "Corn Dog" , value = "corn").pack()
Button(app, text = "Play Question 2", command = question_2).pack()

trick = StringVar()
trick.set(None)

Label(app, text="What is best trick?").pack()
Radiobutton(app,variable = trick, text = "360 air" , value = "360").pack()
Radiobutton(app,variable = trick, text = "cutback" , value = "cutback").pack()
Radiobutton(app,variable = trick, text = "floater" , value = "floater").pack()
Button(app, text = "Play Question 3", command = question_3).pack()

winning = StringVar()
winning.set(None)

Label(app, text="Last time winning a competition?").pack()
Radiobutton(app,variable = winning, text = "2012" , value = "2012").pack()
Radiobutton(app,variable = winning, text = "2021" , value = "2021").pack()
Radiobutton(app,variable = winning, text = "2019" , value = "2019").pack()
Button(app, text = "Play Question 4", command = question_4).pack()

app.mainloop()