import pickle
import os
dict_cod_candidato = {}
dict_regiao = {'N': 'norte', 'NE': 'nordeste', 'S': 'sul', 'SE': 'sudeste', 'O': 'centroeste'}
#dict_cod_candidato = {cod_candidato:{cod_candidato, nome_candidato, cargo},}
#dict_regioes = {cod_candidato:{regiao1, num_votos},}
#dict_resultado = {cod_candidato:{cod_candidato, nome_candidato, cargo},{regiao1, num_votos},{regiao2, num_votos},}


def cargo():
    dict_cargo = {'1': 'Presidente', '2': 'Governador'}
    titulo = ''
    while titulo not in dict_cargo:
        titulo = raw_input('Digite 1 para presidente e 2 para governador: ')
        if titulo not in dict_cargo:
            print('Cargo não encontrado')
    cargo = dict_cargo.get(titulo)
    print('Cargo: ' + cargo)
    return cargo

def registra_codigo():
    registro = open('registro_elegiveis.dat','rb')
    elegiveis = pickle.load(registro)
    legenda = ''
    if elegiveis != {}:
        legenda = raw_input('Informe o código do candidato: ')
        if legenda in elegiveis:
                print('Legenda já registrada')
                legenda = raw_input('Informe o código do candidato: ')
        elif legenda not in elegiveis:
            cod_candidato = elegiveis.get(legenda)
    else:
        legenda = raw_input('Informe o código do candidato: ')
        cod_candidato = elegiveis.get(legenda)
    print('Código: ' + legenda)
    return legenda

def dados_candidato():
    registro = open('registro_elegiveis.dat','rb')
    elegiveis = pickle.load(registro)
    print('Insira os dados dos candidatos')
    candidato = {}

    candidato['cod_candidato'] = legenda = registra_codigo()
    candidato['nome'] = raw_input('Informe o nome do candidato: ')
    candidato['cargo'] = cargo()
    candidato['regiao'] = regiao()
    candidato['num_votos'] = int(raw_input('Quantidade de votos: '))
    elegiveis[legenda] = candidato
    registro.close()
    registro = open('registro_elegiveis.dat','wb')
    pickle.dump(elegiveis, registro)
    print(elegiveis)
    print('Registro total: ' + str(len(elegiveis)) + ' candidatos')

def regiao():    
    sigla = ''
    while sigla not in dict_regiao:
        sigla = raw_input('Insira a sigla para a região: \n N = Norte; NE = Nordeste; S = Sul; SE = Sudeste; O = Centroeste: ')
        if sigla not in dict_regiao:
            print('Região não encontrada')
    regiao = dict_regiao.get(sigla)
    print('Região: ' + regiao)
    return regiao  

def inserir_dados_eleicao():
    continuar = 'Y'
    while continuar != 'X':
        dados_candidato()
        print('Dados salvos com sucesso')
        continuar = raw_input('Continue a cadastrar outro candidato ou digite X para iniciar a contagem de votos: \n \n')
 

def iniciar_processo():
    elegiveis = {}
    registro = open('registro_elegiveis.dat','wb')
    pickle.dump(elegiveis, registro)
    registro.close()
    inserir_dados_eleicao()

iniciar_processo()
