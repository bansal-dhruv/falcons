from tkinter import *
from sp2txt import microphone

root = Tk()
root.title("Abler")
root.geometry("500x250+"+str(root.winfo_screenwidth()-500)+"+"+str(root.winfo_screenheight()-250))
name = Label(root, text="Event Viewer : ")
Text = StringVar()

def Button1(event):
	global Text
	Text.set('Event Viewer : ON/OFF button pressed!')
	microphone()

def Button2(event):
	global Text
	Text.set('Event Viewer : Capslocks pressed!')

def Button3(event):
	global Text
	Text.set('Event Viewer : Button3 pressed!')

#GUI Part
def GUI():

	Text.set("Event Viewer : ")
	test = Label(root, text="")
	name = Label(root, textvariable=Text)
	button1 = Button(root, text="ON/OFF", height=10, width=15)
	button2 = Button(root, text="CapsLocks", height=10, width=15)
	button3 = Button(root, text="Button3", height=10, width=15)
	name.grid(row=0, column=0, sticky=W,columnspan = 3)
	test.grid(row=1, column=0)
	button1.grid(row=2, column=0)
	button2.grid(row=2, column=1)
	button3.grid(row=2, column=2)
	button1.bind("<Button-1>", Button1)
	button2.bind("<Button-1>", Button2)
	button3.bind("<Button-1>", Button3)
	root.mainloop()
GUI()