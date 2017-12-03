from tkinter import *

root = Tk()

#main window START




usr = Label(root, text="USERNAME")
usr.pack()

separator = Frame(height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)



h_button = Button(root, text="Home")
h_button.pack()


root.title('Course Selector')

root.geometry('{}x{}'.format(700, 400))


#main window END

#Scrolldown Menu Widget START
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(root, yscrollcommand=scrollbar.set)

for i in range(6): #should be: for each class out of all the classes the user is taken.
    listbox.insert(END, str(i)) #all of the selections in the scrolldown widget

listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)
#Scrolldown Menu Widget END

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