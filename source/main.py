import os
import time
import sys
from source.ativar_caixa import AtivarCaixa

class Main:

  def init(self):
    ativarCaixa = AtivarCaixa()
    ativarCaixa.ativarCaixa()

    self.menu()
    pass
  def menu(self):
    while True:
      time.sleep(2)
      os.system("cls")

      print("===Banco Digital===")
      print("1 - Administrativo")
      print("2 - Cliente")
      print("3 - Movimentação")
      print("4 - Sair do Sistema de Banco")

      opcaoSelecionada = int(input("Digite o opção desejada: "))

      if opcaoSelecionada == 1:
        print('Administrativo...')

      elif opcaoSelecionada == 2:
        print('Cliente...')

      elif opcaoSelecionada == 3:
        print('Movimenação...')

      elif opcaoSelecionada == 4:
          print("Saindo do sistema...")
          sys.exit()
      else:
          print("Opcão incorreta, por favor digite novamente...")
      pass

  pass