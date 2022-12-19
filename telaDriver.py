from tkinter import *
import os

class telaDriver:
    def __init__(self, master=None):
        master.title("Drivers")
        master.geometry("610x500")
        self.master = master
        self.font = ("arial", 12)
        self.txt = Text(master, width=75, height=100, bg="grey")
        self.txt.place(x=0, y=0)
        self.listarDriver()

    def listarDriver(self):
        self.txt["state"] = "normal"
        self.txt.delete("1.0", "end")
        ls = os.popen("lsmod| grep [^0]$")
        texto = ls.read()
        self.txt.insert(INSERT, texto)
        self.txt["state"] = "disabled"