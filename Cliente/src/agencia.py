class Agencia:
    def adicionar_txt(self, nome, cnpj, ie ):
        arquivo = open('Cliente/src/bd.txt', 'r') # Abra o arquivo (Leitura)
        conteudo = arquivo.readlines()
        id1 = str(len(arquivo.readlines()) + 1)
        texto =   id1 + ","+nome+","+ cnpj+","+ ie +"\n"
        conteudo.append(texto) #insira seu conteúdo
        arquivo = open('Cliente/src/bd.txt', 'w') # Abre novamente o arquivo (escrita)
        arquivo.writelines(conteudo)
        arquivo.close()
        pass
   
    pass