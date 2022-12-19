from tkinter import *
import os

class telaSistema:
    def __init__(self, master=None):
        master.title("Sistema")
        master.geometry("750x500")
        self.master = master
        self.font = ("arial", 12)
        self.txt = Text(master, width=100, height=100, bg="grey")
        self.txt.place(x=0, y=0)
        self.listarSitema()

    def listarSitema(self):
        ls = os.popen("inxi -SMNACGB")
        texto = ls.read()
        texto = texto.replace('\x0312', '')
        texto = texto.replace('\x03', '')
        self.txt["state"] = "normal"
        self.txt.delete("1.0", "end")
        self.txt.insert(INSERT, texto)
        self.txt["state"] = "disabled"

