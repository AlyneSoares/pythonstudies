import pickle
import os
dict_cargo = {'1': 'Presidente', '2': 'Governador'}
dict_regiao = {'Norte': 'Norte', 'Sul': 'Sul', 'Leste': 'Leste', 'Oeste': 'Oeste'}
candidato = {}

def abrir_registro():
    registro = open('registro_elegiveis.dat','rb')
    elegiveis = pickle.load(registro)
    return elegiveis

def gravar_registro(elegiveis):
    registro = open('registro_elegiveis.dat','wb')
    pickle.dump(elegiveis, registro)
    registro.close()

def iniciar_processo():
    elegiveis = {}
    gravar_registro(elegiveis)
    rodar_programa()

def rodar_programa():
    continuar = 'Y'
    while continuar != 'X':
        legenda = inserir_cod_candidato()
        print('Dados salvos com sucesso\n')
        continuar = raw_input('Continue a cadastrar outro candidato ou digite X para concluir o cadastro: \n \n')

def cadastrar_novo_candidato(legenda):
    salvar_cod_candidato(legenda)
    inserir_nome_candidato(legenda)
    selecionar_cargo(legenda)
    inserir_votos_por_regiao(legenda)
    

def atualizar_candidato(legenda):
    inserir_nome_candidato(legenda)
    selecionar_cargo(legenda)
    inserir_votos_por_regiao(legenda)
    
    
def inserir_cod_candidato(): 
    elegiveis = abrir_registro()
    legenda = raw_input('Informe o código do candidato: ')
    if legenda in elegiveis:
            decisao = raw_input('Atualizar candidato, aperte "Enter". Digite X para novo candidato')
            if decisao != 'X':
                    atualizar_candidato(legenda)
    if legenda not in elegiveis:
        cadastrar_novo_candidato(legenda)       


def salvar_cod_candidato(legenda):
    elegiveis = abrir_registro()
    candidato['cod_candidato'] = legenda
    elegiveis[legenda] = candidato
    gravar_registro(elegiveis)
    return legenda


def inserir_nome_candidato(legenda):
    elegiveis = abrir_registro()
    elegiveis[legenda] = candidato
    candidato['nome'] = nome = raw_input('Informe o nome do candidato: ')
    gravar_registro(elegiveis)
    

def selecionar_cargo(legenda):
    elegiveis = abrir_registro()
    titulo = ''
    while titulo not in dict_cargo:
        titulo = raw_input('Digite 1 para presidente e 2 para governador: ')
        if titulo not in dict_cargo:
            print('Cargo não encontrado')
    cargo = dict_cargo.get(titulo)
    elegiveis[legenda] = candidato
    candidato['cargo'] = cargo
    gravar_registro(elegiveis)
    

def inserir_votos_por_regiao(legenda):
    elegiveis = abrir_registro()
    for key in dict_regiao:
        dict_regiao[key] = int(raw_input('Votos da Região ' + key + ' : '))
    dict_regiao_voto = dict_regiao
    elegiveis[legenda] = candidato    
    candidato['num_votos_regiao'] = dict_regiao_voto
    gravar_registro(elegiveis)
    print('Registro total: ' + str(len(elegiveis)) + ' candidatos')
    for subject, score in elegiveis.items():
               print(subject, score)

    


iniciar_processo()
