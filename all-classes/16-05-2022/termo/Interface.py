from tkinter import *
tela = Tk()
tela.title("Termo")
tela.geometry("600x700")
tela.configure(background="#E9C2A6")

texto=Label(tela,text="TERMO", background="#FFFF00", foreground="#000000")
texto.place(x=150,y=30,width=300,height=30)

letra1 = Entry(tela)
letra1.place(x=150,y =70,width=40,height=70,a)

tela.mainloop()