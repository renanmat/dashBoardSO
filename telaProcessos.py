from tkinter import *
import os
class telaProcessos:
    def __init__(self, master=None):
        master.title("Processos")
        master.geometry("960x500")
        self.master = master
        self.font = ("arial", 12)
        self.txt = Text(master, width=120, height=20, bg="black", fg="green")
        self.txt.place(x=0, y=0)
        self.listarProcessos()
        self.legenda ="User: Usuario" + ' '*4 + "PID: Id do processo" + ' '*4 + "%CPU:Uso do processador" + ' '*4 + "%MEM:Uso da memoria RAM"
        self.msg = Label(master, text=self.legenda, font=self.font)
        self.msg.place(x=0, y=360)



    def listarProcessos(self):
        ls = os.popen("ps aux  --sort=-pcpu,+pmem| cut -c 1-120 | head -n 20")
        texto = ls.read()
        self.txt["state"] = "normal"
        self.txt.delete("1.0", "end")
        self.txt.insert(INSERT, texto)
        self.txt["state"] = "disabled"
        self.master.after(2000, self.listarProcessos)
