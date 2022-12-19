from tkinter import *
import os
from telaProcessos import *
from telaSistema import *
from telaArquivo import *
from telaDriver import *
import psutil

class telaInicial:
    def __init__(self, master=None):
        self.master = master
        self.font = ("Arial", 14)

        ##Objetos Tela##
        #Sistema
        self.btSistema = Button(master, text="Sistema", font=self.font)
        self.btSistema["command"] = self.abrirSistema
        self.btSistema.place(x=100, y=50)

        # Processos
        self.btProcessos = Button(master, text="Processos", font=self.font)
        self.btProcessos["command"] = self.abrirProcessos
        self.btProcessos.place(x=200, y=50)

        #Driver
        self.btDriver = Button(master, text="Drivers", font=self.font)
        self.btDriver["command"] = self.abrirDriver
        self.btDriver.place(x=320, y=50)

        #Arquivos
        self.btArquivos = Button(master, text="Sistemas de arquivos", font=self.font)
        self.btArquivos["command"] = self.abrirArquivo
        self.btArquivos.place(x=100, y=100)

        #Terminal
        self.btTerminal = Button(master, text="Terminal", font=self.font)
        self.btTerminal["command"] = self.abrirTerminal
        #self.btTerminal.place(x=300, y=100)

        # CPU %
        self.Cpu = Label(master, text="")
        self.Cpu.place(x=0, y=0)
        self.lbCpu = Label(master, text="")
        self.lbCpu.place(x=470, y=0)
        self.usoCpu()

        # MEMORIA%
        self.Memoria = Label(master, text="")
        self.Memoria.place(x=0, y=20)
        self.lbMemoria = Label(master, text="")
        self.lbMemoria.place(x=470, y=20)
        self.usoMemoria()

    def abrirProcessos(self):
        tlProcessos = Toplevel(self.master)
        telaProcessos(tlProcessos)

    def abrirSistema(self):
        tlSistema = Toplevel(self.master)
        telaSistema(tlSistema)

    def abrirArquivo(self):
        tlArquivo = Toplevel(self.master)
        telaArquivo(tlArquivo)

    def usoCpu(self):
        usadaCpu = psutil.cpu_percent(1)
        self.Cpu["text"] = "CPU%  [" + "|" * int(usadaCpu) + " " * int(100 - usadaCpu) + " ]"
        self.lbCpu["text"] = usadaCpu
        self.master.after(2000, self.usoCpu)

    def usoMemoria(self):
        usadaMemoria = psutil.virtual_memory()[2]
        self.Memoria["text"] = "MEM% [" + "|" * int(usadaMemoria) + " " * int(100 - usadaMemoria) + " ]"
        self.lbMemoria["text"] = usadaMemoria
        self.master.after(2000, self.usoMemoria)

    def abrirDriver(self):
        tlDriver = Toplevel(self.master)
        telaDriver(tlDriver)

    def abrirTerminal(self):
        os.system('sh')


tela = Tk()
tela.title("SO")
tela.geometry("500x200")
tl = telaInicial(tela)
tela.mainloop()

