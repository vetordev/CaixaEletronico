import os
import time

from Cliente.src.agencia import Agencia



class Main:

  def init(self):
    self.agencia = Agencia()

    while True:
      time.sleep(2)
      os.system("cls")

      print("===Cliente===")
      print("1 - Adicionar Banco/fintech")
      print("2 - Alterar Banco/fintech")
      print("3 - Excluir Banco/fintech")
      print("4 - Buscar Banco/fintech por cnpj")
      print("5 - Buscar Cliente Pelo Identificador")
      print("6 - Listar Todos os Clientes")
      print("7 - Sair do Sistema de Banco")

      opcaoSelecionada = int(input("Digite o opção desejada: "))

      if opcaoSelecionada == 1:
        self.adicionarCliente()



      elif opcaoSelecionada == 2:
        print("ainda não definido")

      elif opcaoSelecionada == 3:
        print("ainda não definido")

      elif opcaoSelecionada == 4:
        print("ainda não definido")

      elif opcaoSelecionada == 5:
       print("ainda não definido")

      elif opcaoSelecionada == 6:
        print("ainda não definido")

      elif opcaoSelecionada == 7:
          print("Saindo do programa...")
          print("Inté...")
      else:
          print("Opcão incorreta, por favor digite novamente...")
      pass

  pass

  def adicionarCliente(self):
    nome = input("insira o nome da sua agência: ")
    cnpj = input("insira o CNPJ da sua agência: ")
    ie = input("inseira a incrição estadual da sua agência")
    self.agencia.adicionar_txt(nome,cnpj,ie)
    pass





