from datetime import datetime
# Só há uma tentativa de ativação

class AtivarCaixa: 

  # TODO método gerar logs de ativações

  def __init__(self): 
    logs = open('./logs/log.txt', 'r')
    
    self.ultimaAtivacao = datetime.fromisoformat(self.buscarUltimaAtivacao(logs))

    self.dataAtual = datetime.now()

    self.codigoAtivacao = '246IQ'    
    print(self.ultimaAtivacao)
    print(self.dataAtual)
    pass
  
  def ativarCaixa(self):

    # Caso faça mais de 1 dia desde a última ativação
    if(self.verificarAtivacao()):

      # Caso o código de ativação esteja correto
      if(self.exibirMenuDeAtivacao()):
        print('true')
        # Registra uma ativação bem-sucedida
        self.log('Ativação bem-sucedida')
        pass
      else: 
        print('false')
        # Registra uma ativação mal-sucedida
        self.log('Ativação mal-sucedida')
        pass
      
      pass

    else: 
      
      # Registra uma ativação não necessária
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

  # Verifica se é necessário realizar a ativação do caixa eletrônico
  def verificarAtivacao(self):
    
    # Diferença de dias entre a ultima ativação e tentativa atual
    dias = (self.dataAtual - self.ultimaAtivacao).days
    print(dias)

    if dias > 0:
      return True
      pass

    else: 
      return False
    pass
  
  # Exibe um menu de ativação que recebe o código de ativação e o valida
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

  def log(self, tipoAtivacao): 
    logs = open('./logs/log.txt', 'a')
    logs.write('\n{tipo}, {data}'.format(tipo=tipoAtivacao, data=self.dataAtual))
    pass
