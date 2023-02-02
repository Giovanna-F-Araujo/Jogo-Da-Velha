# Vetor com 9 campos referentes as posições do jogo da velha 
tabela = ["_","_","_","_","_","_","_","_","_",]

#Função para realizar a quebra de linha do jogo
def desenha_tabela (vetor_velha_da_velha):
  jogoDaVelha = ''
  for i in range(len(vetor_da_velha)):
    if(i==2 or i==5 or i==8):
      jogoDaVelha += " " + vetor_velha_da_velha[i] + " \n"
    else:
      jogoDaVelha += " " + vetor_velha_da_velha[i] + " |"
  return jogoDaVelha

#Função para verificar a posição 
def verifica_tabela(vetor_da_velha, posicao):
  resultado = False
  if(verifica_tabela[posicao] == '_'):
    resultado = True
  return resultado

#Função para verificar se o jogador venceu
def verifica_vitoria(vetor_da_velha,simbolo):
  resultado = False
  #linha
  if(vetor_da_velha [0] == simbolo and vetor_da_velha[1] == simbolo and vetor_da_velha[2] == simbolo):
    resultado = True
  elif(vetor_da_velha[3] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[5] == simbolo):
    resultado = True
  elif(vetor_da_velha[6] == simbolo and vetor_da_velha[7] == simbolo and vetor_da_velha[7] == simbolo):
    resultado = True
  #coluna
  elif(vetor_da_velha[0] == simbolo and vetor_da_velha[3] == simbolo and vetor_da_velha[6] == simbolo):
    resultado = True
  elif(vetor_da_velha[1] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[7] == simbolo):
    resultado = True
  elif(vetor_da_velha[2] == simbolo and vetor_da_velha[5] == simbolo and vetor_da_velha[8] == simbolo):
     resultado = True
  #vertical
  elif(vetor_da_velha[0] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[8] == simbolo):
    resultado = True
  elif(vetor_da_velha[6] == simbolo and vetor_da_velha[4] == simbolo and vetor_da_velha[2] == simbolo):
    resultado = True

#Função para verificar o empate
def verificar_empate(vetor_da_velha):
  resultado = True
  for i in vetor_da_velha:
    if(i == "_"):
      resultado = False
  return resultado

#Variáveis do jogo
jogador = 1
jogador_numero_1 = 0
jogador_numero_2 = 0

while(True):
#Verifica se é a vez do jogador 1
  if(jogador == 1):
    jogador_numero_1 = input('Jogador 1 - Digite uma posição 1 a 9: ')
    if(verifica_tabela(tabela,int(jogador_numero_1)-1)):
      tabela[int(jogador_numero_1)-1] = 'X'
      jogador = 2
      print(desenha_tabela(tabela))
    else:
      print(desenha_tabela(tabela))
      print('Posição já ocupada')
  if(verifica_vitoria(tabela,'X')):
    print('Jogador número 1 ganhou!!!')
    break
  if(verificar_empate(tabela)):
    print('Empate!!!')
    break
#Verifica se é a vez do jogador 2
  if(jogador == 2):
    jogador_numero_2 = input('Jogador 2 - Digite uma posição 1 a 9: ')
    if(verifica_tabela(tabela,int(jogador_numero_2)-1)):
      tabela[int(jogador_numero_2)-1] = 'O'
      jogador = 1
      print(desenha_tabela(tabela))
    else:
      print(desenha_tabela(tabela))
      print('Posição já ocupada')
  if(verifica_vitoria(tabela,'O')):
    print('Jogador número 2 ganhou!!!')
    break
  if(verificar_empate(tabela)):
    print('Empate!!!')
    break