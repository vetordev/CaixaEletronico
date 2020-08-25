from datetime import datetime
import sys
# Só há uma tentativa de ativação

class AtivarCaixa: 

  def __init__(self): 
    print('a')
    logs = open('./logs/log.txt', 'r')
    
    # Recebe a ultima ativação bem-sucedida e a converte para o tipo datetime
    self.ultimaAtivacao = datetime.fromisoformat(self.buscarUltimaAtivacao(logs))

    # Recebe a data atual
    self.dataAtual = datetime.now()

    # Define o código de ativação do caixa eletrônico
    self.codigoAtivacao = '246IQ'    
    pass
  
  # Método principal da classe
  def ativarCaixa(self):

    '''
      Executa o método verificarAtivacao() que retona True caso tiver feito mais de 1 dia desde a última ativação bem-sucedida
    '''
    if(self.verificarAtivacao()):

      '''
        Executa o método exibirMenuDeAtivacao() que retorna True caso o código de ativação esteja correto
      '''
      if(self.exibirMenuDeAtivacao()):

        # Registra uma ativação bem-sucedida
        self.log('Ativação bem-sucedida')
        pass

      # Caso o código de ativação esteja errado
      else: 

        # Registra uma ativação mal-sucedida
        self.log('Ativação mal-sucedida')

        # Fecha a aplicação
        print('Código de ativação inválido.')
        sys.exit()
        pass
      
      pass
    
    # Caso não faça 1 dia desde a última ativação bem-sucedida
    else: 
      
      # Registra uma ativação desnecessária
      self.log('Ativação desnecessária')
      pass
    pass

  # Método para buscar a última ativação bem-sucedida do caixa eletrônico
  def buscarUltimaAtivacao(self, logs):
    ultimaAtivacao = ''
    
    # Lê o arquivo de logs e armazenar numa lista
    logs = logs.readlines()

    # Inverter os itens da lista de logs
    logs.reverse()

    for log in logs:

      '''
        Separa as informações de cada linha de log por ',' gerando uma lista com a estrutura abaixo:
        Tipo, data
      '''
      log = log.split(',')
      
      # Como a lista foi invertida, a primeira vez que aparecer uma 'Ativação bem-sucedida' terá sido a última realizada
      if log[0] == 'Ativação bem-sucedida':

        # Recebe a data da última ativação bem-sucedida
        ultimaAtivacao = log[1].strip() # -> remove o espaço do início
        break
      pass
    
    return ultimaAtivacao
    pass

  # Método para verificar se é necessário realizar a ativação do caixa eletrônico
  def verificarAtivacao(self):
    
    # Diferença de dias entre a ultima ativação e tentativa atual
    dias = (self.dataAtual - self.ultimaAtivacao).days

    # Verifica se faz mais de 1 dia desde a última ativação bem-sucedida
    if dias > 0:
      return True
      pass

    else: 
      return False
    pass
  
  # Método para exibir um menu de ativação que recebe o código de ativação e o valida
  def exibirMenuDeAtivacao(self): 

    # Recebe o código de ativação
    codigoAtivacao = input('Digite o código de ativação do caixa eletrônico: ')

    # Verifica se o código de ativação corresponde ao esperado
    if codigoAtivacao == self.codigoAtivacao:
      return True
      pass
    else:
      return False
      pass

    pass

  # Método para registrar uma tentativa de ativação
  def log(self, tipoAtivacao): 

    logs = open('./logs/log.txt', 'a')
    logs.write('\n{tipo}, {data}'.format(tipo=tipoAtivacao, data=self.dataAtual))
    pass
