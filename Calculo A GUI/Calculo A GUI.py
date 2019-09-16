from __future__ import division
from tkinter import *
from sympy import symbols, cos, sin, diff, init_printing
from sympy.plotting import plot

init_printing()
x,y = symbols('x y')

class App:
	def __init__(self, Parent):
		
		self.Window_1 = Frame(Parent)
		self.Window_1.place(x = 0,y = 0,width = 600, height = 20)
		self.Window_2 = Frame(Parent)
		self.Window_2.place(x = 0, y = 20,width = 600, height = 200)

		# Window_1
		self.lab_1 = Label(self.Window_1, text="Função: ")
		self.lab_1.place(x = 260,y = 0)
		self.ent_1 = Entry(self.Window_1, bd = 5)
		self.ent_1.place(x = 310,y = 0,width=200)

		# Window_2
		self.btn_1 = Button(self.Window_2, text="Derivada", command = self.derivada,cursor="circle")
		self.btn_1.place(x = 0, y = 15)
		self.btn_2 = Button(self.Window_2, text="Integral Indefinida", command = self.integral_indefinida,cursor="circle")
		self.btn_2.place(x = 0, y = 60)
		self.btn_3 = Button(self.Window_2, text="Integral Definida", command = self.integral_definida,cursor="circle")
		self.btn_3.place(x = 0, y = 105)
		self.btn_4 = Button(self.Window_2, text="Reta Tangente", command = self.reta_tangente,cursor="circle")
		self.btn_4.place(x = 0, y = 150)




	def derivada(self):
		f_ = self.ent_1.get()
		print("Derivada de ordem",1,":",diff(f_,x,1))

		self.lab_2 = Label(self.Window_2, text=("Derivada de ordem",1,":",diff(f_,x,1)))
		self.lab_2.place(x = 150, y = 15)

		plot(f_, diff(f_,x,1), title="Função e sua derivada")

	def integral_indefinida(self):
		f_ = self.ent_1.get()
		print("Integral indefinida da funcao:",integrate(f_,x),"+ C")

		self.Window_int_indef = Toplevel()

		self.lab_3 = Label(self.Window_int_indef, text=("Integral indefinida da funcao:",integrate(f_,x),"+ C"))
		self.lab_3.pack()

	def integral_definida(self):
		pass

	def reta_tangente(self):
		pass

root = Tk()

root.title("Calculo A")
root.geometry("750x600+200+50")

app = App(root)
root.mainloop()