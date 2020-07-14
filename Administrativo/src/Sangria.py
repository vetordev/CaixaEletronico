class Sangria:

   def registrarSangria(self, data, valor, atm):
      sangria = 'ATM: ' + atm + ', Data: ' + data + ', Valor: ' + valor
      logSangria = open('./Administrativo/src/db/logSangria.txt', 'r').readlines()
      logSangria.append(sangria + '\n')

      arquivo = open('./Administrativo/src/db/logSangria.txt', 'w')
      arquivo.writelines(logSangria)
      arquivo.close()

      print('\nSangria registrada! Dados:')
      print(sangria)
      pass
   pass