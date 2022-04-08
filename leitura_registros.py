import pickle 
import os
import collections
dict_cargo = {'1': 'Presidente', '2': 'Governador'}


def abrir_registro():
    registro = open('registro_elegiveis.dat','rb')
    votos_candidatos = pickle.load(registro)
    return votos_candidatos

def escolher_candidato():
     legenda = raw_input('Digite o código do candidato:')
     return legenda

def buscar_nome(legenda):
     votos_candidatos = abrir_registro()
     candidato = votos_candidatos.get(legenda)
     nome_candidato = candidato.get('nome')
     return nome_candidato

def buscar_voto_regiao(legenda):
     votos_candidatos = abrir_registro()
     candidato = votos_candidatos.get(legenda)
     num_votos_regiao = candidato.get('num_votos_regiao')
     return num_votos_regiao

def buscar_cargo(legenda):     
     votos_candidatos = abrir_registro()
     candidato = votos_candidatos.get(legenda)
     cargo = candidato.get('cargo')
     return cargo   

def total_votos_candidatos():
     votos_candidatos = abrir_registro()
     candidatos = {}
     for key, value in votos_candidatos.items():
          nome = buscar_nome(key)
          num_votos_regiao = buscar_voto_regiao(key)
          total_votos = str(sum(num_votos_regiao.values()) )          
          candidatos[nome] = total_votos
     print(candidatos)

def ler_registro():
     votos_candidatos = abrir_registro()
     for key, value in votos_candidatos.items():
          print('Código ' +key +':')
          for subject, score in value.items():
               print(subject, score)


def presidente_eleito():
     votos_candidatos = abrir_registro()
     candidatos = {}
     for key, value in votos_candidatos.items():
          cargo = buscar_cargo(key)
          if cargo == 'Presidente':
                    nome = buscar_nome(key)
                    num_votos_regiao = buscar_voto_regiao(key)
                    total_votos = (sum(num_votos_regiao.values()))          
                    candidatos[nome] = total_votos
     presidente = max(candidatos, key=candidatos.get)
     print('Novo Presidente: candidato ' + presidente + ' venceu com ' + str(candidatos[presidente]) + ' votos')


def governador_eleito():
     votos_candidatos = abrir_registro()
     candidatos = {}
     for key, value in votos_candidatos.items():
          cargo = buscar_cargo(key)
          if cargo == 'Governador':
                    nome = buscar_nome(key)
                    num_votos_regiao = buscar_voto_regiao(key)
                    total_votos = sum(num_votos_regiao.values())          
                    candidatos[nome] = total_votos
     presidente = max(candidatos, key=candidatos.get)
     print('Novo Governador: candidato ' + presidente + ' venceu com ' + str(candidatos[presidente]) + ' votos')

                    
def votos_por_regiao():
     votos_candidatos = abrir_registro()
     votos_regiao = []
     for key, value in votos_candidatos.items():
          num_votos_regiao = buscar_voto_regiao(key)
          votos_regiao.append(num_votos_regiao)          
     contador = collections.Counter()
     for i in votos_regiao:
          contador.update(i)
     resultado = dict(contador)
     print('Total por região: ')
     print(contador)



def rodar_programa():
    continuar = 'Y'
    while continuar != 'X':
        legenda = menu()
        continuar = raw_input('Aperte "enter" para nova consulta ou digite X para concluir o cadastro: \n \n')


def menu():
     opcao = ''
     while opcao !='X':
          opcao = raw_input('\n O que vc quer? \n' + '\n' + '1- Total de votos para cada região: '
                         + '\n' + '2- Governador eleito: '+ '\n' +
                         '3- Presidente Eleito: '
                         + '\n' + '4- Total de Votos dos candidatos: ' +
                         '\n' + '5- Ler dados do registro de candidatos: '
                         + '\n' + 'X - Sair do programa\n \n')
          if opcao == 'X':
               print('Tem certeza?')
               break
          elif opcao == '1':
               votos_por_regiao()
          elif opcao == '2':
               governador_eleito()
          elif opcao == '3':
               presidente_eleito()
          elif opcao == '4':
               total_votos_candidatos()
          elif opcao == '5':
               ler_registro()
          else:
               print('\n Não é uma opção valida')
          


rodar_programa()            
#votos_por_regiao()
#governador_eleito()               
#presidente_eleito()
#total_votos_candidatos()
#ler_registro()
