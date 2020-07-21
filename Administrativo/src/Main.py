import os
import time
import sys

from Administrativo.src.Sangria import Sangria

class Main:

  def init(self):
    self.sangria = Sangria()

    while True:
      time.sleep(2)
      os.system("cls")

      print("===Administração===")
      print("1 - Registrar sangria")
      print("2 - Registrar entrada de cédulas")
      print("3 - Emitir comprovante de transação")
      print("4 - Relatórios da ATM")
      print("5 - Ativação/desativação de recursos de uma ATM")
      print("6 - Ativação/desativação de recursos de uma agência")
      print("7 - Ativação/desativação de recursos de um cliente específico")
      print("8 - Sair do Sistema de Banco")

      opcaoSelecionada = int(input("Digite o opção desejada: "))

      if opcaoSelecionada == 1:
        self.registrarSangria()
        pass

      elif opcaoSelecionada == 2:
        print('Funcionalidade em manutenção. Volte mais tarde.')
        pass

      elif opcaoSelecionada == 3:
        print('Funcionalidade em manutenção. Volte mais tarde.')
        pass

      elif opcaoSelecionada == 4:
        print('Funcionalidade em manutenção. Volte mais tarde.')
        pass

      elif opcaoSelecionada == 5:
        print('Funcionalidade em manutenção. Volte mais tarde.')
        pass

      elif opcaoSelecionada == 6:
        print('Funcionalidade em manutenção. Volte mais tarde.')
        pass

      elif opcaoSelecionada == 7:
        print('Funcionalidade em manutenção. Volte mais tarde.')
        pass

      elif opcaoSelecionada == 8:
          print("Saindo do programa...")
          sys.exit()
      else:
          print("Opcão incorreta, por favor digite novamente...")
      pass
  pass

  def registrarSangria(self):
    sangria = {
      'atm' : input('Digite o código da ATM em que houve a sangria: '),
      'data' : input('Digite a data da sangria: '),
      'valor' : input('Digite o valor da sangria: '),
    }

    self.sangria.registrarSangria(sangria.get('data'), sangria.get('valor'), sangria.get('atm'))
    input()
    pass





