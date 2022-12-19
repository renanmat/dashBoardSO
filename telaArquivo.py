from tkinter import *
import os

class telaArquivo:
    def __init__(self, master=None):
        master.title("Sistemas de arquivos")
        master.geometry("610x500")
        self.master = master
        self.font = ("arial", 12)
        self.txt = Text(master, width=75, height=100, bg="grey")
        self.txt.place(x=0, y=0)
        self.listarArquivo()

    def listarArquivo(self):
        self.txt["state"] = "normal"
        self.txt.delete("1.0", "end")
        ls = os.popen("sudo fdisk -l")
        texto = ls.read() + "\n"
        self.txt.insert(INSERT, texto)

        ls = os.popen("df -h --total")
        texto = ls.read()
        self.txt.insert(INSERT, texto)

        self.txt["state"] = "disabled"