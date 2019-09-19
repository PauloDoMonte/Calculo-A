from __future__ import division
from tkinter import *
from sympy import symbols, cos, sin, diff, init_printing, integrate, sympify, Lambda
from sympy.plotting import plot

init_printing()
x,y = symbols('x y')

class App():

	def __init__(self, Parent):
		
		self.Window_Reta_Tangente = Frame(Parent)
		self.Window_Reta_Tangente.place(x = 0,y = 0,width = 200, height = 300)

		self.Window_Derivada = Frame(Parent)
		self.Window_Derivada.place(x=0, y=130,width=200, height=300)

					# Reta Tangente
		self.lab_1 = Label(self.Window_Reta_Tangente, text="Reta Tangente")
		self.lab_2 = Label(self.Window_Reta_Tangente, text="Função: ")
		self.lab_3 = Label(self.Window_Reta_Tangente, text="Ponto X0: ")
		self.ent_1 = Entry(self.Window_Reta_Tangente, bd=5)
		self.ent_2 = Entry(self.Window_Reta_Tangente, bd=5)
		self.btn_1 = Button(self.Window_Reta_Tangente, text="Calcular", command=self.reta_tangente)

		self.lab_1.place(x=20,y=0)
		self.lab_2.place(x=0,y=25)
		self.lab_3.place(x=0,y=50)
		self.ent_1.place(x=60,y=25)
		self.ent_2.place(x=60,y=50)
		self.btn_1.place(x=0,y=90)

					# Derivada
		self.lab_4 = Label(self.Window_Derivada, text="Derivada")
		self.lab_5 = Label(self.Window_Derivada, text="Função: ")
		self.lab_6 = Label(self.Window_Derivada, text="Ordem: ")
		self.ent_3 = Entry(self.Window_Derivada, bd=5)
		self.ent_4 = Entry(self.Window_Derivada, bd=5)
		self.btn_2 = Button(self.Window_Derivada, text="Calcular", command=self.derivada)

		self.lab_4.place(x=20,y=0)
		self.lab_5.place(x=0,y=26)
		self.lab_6.place(x=0,y=55)
		self.ent_3.place(x=60,y=20)
		self.ent_4.place(x=60,y=50)
		self.btn_2.place(x=0,y=90)

					# Integral Indefinida

					# Integral Definida

	def reta_tangente(self):
		funcao = sympify(self.ent_1.get())
		f = Lambda(x, funcao)
		x0 = int(self.ent_2.get())
		equacao_da_reta = (diff(f(x),x).subs(x,x0))*(x-x0) + f(x0)
		print (equacao_da_reta)
		self.lab_8 = Label(self.Window_Reta_Tangente, text=equacao_da_reta)
		self.lab_8.place(x=55,y=92)


	def derivada(self):		
		funcao = self.ent_3.get()
		ordem = self.ent_4.get()
		print(diff(funcao,x,ordem))
		self.lab_7 = Label(self.Window_Derivada, text = (diff(funcao,x,ordem)))
		self.lab_7.place(x=60,y=90)

root = Tk()

root.title("Calculo A")
root.geometry("750x600+200+50")

app = App(root)
root.mainloop()