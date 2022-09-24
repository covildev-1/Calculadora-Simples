import colorama
import os
from colorama import Fore, Style
from Historico import historico
from Calcular import calcular


def valores():
    values = input()
    
    
    if values.lower() == 'h':
        historico()
    else:
        return (calcular(values))
            

colorama.init()
rodando = True


while rodando:
    resul = valores()
    
    
    if type(resul) != int and type(resul) != float:
        resul = valores()
        
        
    print(Fore.BLUE +
          Style.BRIGHT +
          'Digite "H" se quiser ver o histórico da calculadora.' +
          Style.RESET_ALL
          )
    print(resul)
