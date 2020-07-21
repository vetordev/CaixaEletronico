import os
import time
import sys

from Administrativo.src.Main import Main as AdminMain
from Cliente.src.Main import Main as ClienteMain
from Movimentação.src.Main import Main as MoviMain


class Menu:

  def init(self):

    while True:
      time.sleep(2)
      os.system("cls")

      print("===Banco Digital===")
      print("1 - Módulo administrativo")
      print("2 - Módulo cliente")
      print("3 - Módulo movimentação")
      print("4 - Sair do Sistema de Banco")

      opcaoSelecionada = int(input("Digite o opção desejada: "))

      if opcaoSelecionada == 1:
        self.administrativo()
        pass

      elif opcaoSelecionada == 2:
        self.cliente()
        pass

      elif opcaoSelecionada == 3:
        self.movimentacao()
        pass

      elif opcaoSelecionada == 4:
          print("Saindo do programa...")
          sys.exit()
      else:
          print("Opcão incorreta, por favor digite novamente...")
      pass
  pass

  def administrativo(self):
    adminMain = AdminMain()
    adminMain.init()
    pass
  def cliente(self):
    clienteMain = ClienteMain()
    clienteMain.init()
    pass
  def movimentacao(self):
    moviMain = MoviMain()
    moviMain.init()
    pass