from tkinter import *


root = Tk()

#main window START




usr = Label(root, text="USERNAME")
usr.pack()


root.title('Course Selector')

root.geometry('{}x{}'.format(600, 400))


#main window END

#Dropdown Menu Widget START


menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="Select Class", menu=filemenu)
filemenu.add_command(label="Class1")
filemenu.add_command(label="Class2")
filemenu.add_command(label="Class3")
filemenu.add_command(label="Class4")

filemenu.add_separator()

homemenu = Menu(menu)
menu.add_cascade(label="Home", menu=homemenu)
homemenu.add_command(label="Return Home")
#Dropdown Menu Widget END

#top level START
top = Toplevel()
top.title("Grades")

course_name = "Course"
course_grade = "Grade"

crs = Message(top, text= course_name)
grd = Message(top, text = course_grade)

crs.pack()
grd.pack()

top.config(width = 250, height = 300)
top.pack_propagate(False)

#top level END

mainloop()