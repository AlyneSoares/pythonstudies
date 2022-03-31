import pickle 
import os 
     
def ler_registro():
     try:
          registro = open('registro_elegiveis.dat','rb') 
          votos_candidatos = pickle.load(registro) 
          if len(votos_candidatos) > 0: 
               for i in votos_candidatos: 
                    print( 'Legenda do Candiato: ' + votos_candidatos[i]['cod_candidato'] )
                    print ('Nome candidato: ' + votos_candidatos[i]['nome'] )
                    print ('Cargo: ' + votos_candidatos[i]['cargo'] )
                    print ('Região: ' + votos_candidatos[i]['regiao']) 
                    print ('Total de votos: ' + str(votos_candidatos[i]['num_votos']) )
          registro.close()
     except:
          print("Este registro não existe \n" )

ler_registro()
