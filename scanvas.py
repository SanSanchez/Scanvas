import tkinter as tk
import datetime
import calendar

class Base(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		raise NotImplementedError

class HomePage(Base):

	def create_widgets(self):
		self.configure(background = "black")

		self.button1 = tk.Button(self, command=self.controller.Calendar_Box, text="Semester", fg="yellow", bg="black")
		self.button1.grid(row=0, column=0, padx=20, pady=50, sticky=tk.W+tk.E)

		self.button2 = tk.Button(self, command=lambda: self.controller.show_frame(GradePage), padx=5, pady=5, text="Grades", fg="yellow", bg="black")
		self.button2.grid(row=1, column=0, padx=20, pady=50, sticky=tk.W+tk.E)

		self.button3 = tk.Button(self, text="Login/Logout", fg="yellow", bg="black", command=self.controller.Login_Box)
		self.button3.grid(row=2, column=0, padx=20, pady=50, sticky=tk.W+tk.E)



class GradePage(Base):

	def create_widgets(self):
		self.configure(background="black")

		self.usr = tk.Label(self, text="USERNAME", fg="yellow", bg="black")
		self.usr.grid(row=0, column=0)

		OPTIONS = ["one", "two", "three"]
		self.variable = tk.StringVar(self)
		self.variable.set(OPTIONS[0])

		self.w = tk.OptionMenu(self, self.variable, *OPTIONS)
		self.w.grid(row=1, column=0)

		self.button1 = tk.Button(self, anchor=tk.W, command=lambda: self.controller.show_frame(HomePage), padx=5, pady=5, text="Home")
		self.button1.grid(row=0, column=4, columnspan=4, padx=5, pady=5, sticky=tk.W+tk.E)

		self.button2 = tk.Button(self, text="Show Grades", command=self.controller.Grade_Box)
		self.button2.grid(row=2, column=0)
class Grades:

	def __init__(self, parent):
		self.parent = parent
		gFrame = tk.Frame(parent, bg="black")
		gFrame.grid()

		crs = tk.Label(gFrame, text="Course", bg="black", fg="yellow")
		grd = tk.Label(gFrame, text="Grade", bg="black", fg="yellow")

		crs.grid(row=0, column=0)
		grd.grid(row=0, column=2)


class Login:

	def __init__(self, parent):
		self.parent = parent
		logFrame = tk.Frame(parent, bg="black")
		logFrame.grid()

		fsuid = tk.Label(logFrame, text="FSUID", fg="yellow", bg="black")
		fsuid.grid(row=0)

		password = tk.Label(logFrame, text="Password", fg="yellow", bg="black")
		password.grid(row=1)

		e1 = tk.Entry(logFrame)
		e2 = tk.Entry(logFrame)

		e1.grid(row=0, column=1)
		e2.grid(row=1, column=1)

		self.button1 = tk.Button(logFrame, text="Login", command=self.close_box)
		self.button1.grid(row=4, column=2, sticky=tk.E)

		self.button2 = tk.Button(logFrame, text="Cancel", command=self.close_box)
		self.button2.grid(row=4, column=3, sticky=tk.W)

	def close_box(self):
		self.parent.destroy()

# Calendar class modified from metulburr's Calendar widget code
# https://python-forum.io/Thread-Tkinter-tkinter-calendar-widget
class Calendar:
	def __init__(self, parent, values):
		self.values = values
		self.parent = parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY)
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		self.wid = []
		self.day_selected = 1
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = ''

		self.setup(self.year, self.month)

	def clear(self):
		for w in self.wid[:]:
			w.grid_forget()
			self.wid.remove(w)

	def go_prev(self):
		if self.month > 1:
			self.month -= 1
		else:
			self.month = 12
			self.year -= 1
		self.clear()
		self.setup(self.year, self.month)

	def go_next(self):
		if self.month < 12:
			self.month += 1
		else:
			self.month = 1
			self.year += 1

		self.clear()
		self.setup(self.year, self.month)

	def selection(self, day, name):
		self.day_selected = day
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = name

		#data
		self.values['day_selected'] = day
		self.values['month_selected'] = self.month
		self.values['year_selected'] = self.year
		self.values['day_name'] = name
		self.values['month_name'] = calendar.month_name[self.month_selected]

		self.clear()
		self.setup(self.year, self.month)

	def setup(self, y, m):
		left = tk.Button(self.parent, text='<', bg='black', fg='yellow', command=self.go_prev)
		self.wid.append(left)
		left.grid(row=0, column=1)

		header = tk.Label(self.parent, bg='black', fg='yellow',height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
		self.wid.append(header)
		header.grid(row=0, column=2, columnspan=3)

		right = tk.Button(self.parent, text='>', fg='yellow', bg='black', command=self.go_next)
		self.wid.append(right)
		right.grid(row=0, column=5)

		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		for num, name in enumerate(days):
			t = tk.Label(self.parent, text=name[:3], bg='black', fg='yellow')
			self.wid.append(t)
			t.grid(row=1, column=num)

		for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
			for d, day in enumerate(week):
				if day:
					b = tk.Button(self.parent, width=1, text=day, fg='yellow', bg='black', command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
					self.wid.append(b)
					b.grid(row=w, column=d)

		sel = tk.Label(self.parent, fg='yellow', bg='black', height=2, text='{} {} {} {}'.format(self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
		self.wid.append(sel)
		sel.grid(row=8, column=0, columnspan=7)

		ok = tk.Button(self.parent, fg='yellow', bg='black', width=5, text='OK', command=self.kill_and_save)
		self.wid.append(ok)
		ok.grid(row=9, column=2, columnspan=3, pady=10)

	def kill_and_save(self):
		self.parent.destroy()


class Control(tk.Tk):

	def __init__(self):
		tk.Tk.__init__(self)
		self.title("sCanvas")
		self.configure(background='black')
		self.geometry("600x500")
		self.create_widgets()
		self.resizable(0, 0)
		self.data = {}

	def create_widgets(self):
		self.container = tk.Frame(self, background="black")
		self.container.grid(row=0, column=0)

		self.frames = {}
		for F in (HomePage, GradePage):
			frame = F(self.container, self)
			frame.grid(row=2, column=2, sticky=tk.NW+tk.SE)
			self.frames[F] = frame
		self.show_frame(HomePage)

	def show_frame(self, cls):
		self.frames[cls].tkraise()

	def Login_Box(self):
		box = tk.Toplevel()
		box.configure(background='black')
		log = Login(box)

	def Calendar_Box(self):
		top = tk.Toplevel()
		top.configure(background='black')
		cal = Calendar(top, self.data)

	def Grade_Box(self):
		grade = tk.Toplevel()
		grade.configure(background='black')
		gr = Grades(grade)

if __name__ == "__main__":
	app = Control()
	app.mainloop()
	exit()
