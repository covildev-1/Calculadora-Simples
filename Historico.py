import os
import colorama
from colorama import Fore, Style

def historico():
    i = 0
    
    
    print(Fore.BLUE +
          Style.BRIGHT +
          'Digite "V" para voltar à calcular.' +
          Style.RESET_ALL
          )
    
    
    while i < len(l_historico):
        print(Fore.GREEN + Style.BRIGHT+ str(l_historico[i]) + Style.RESET_ALL)
        i += 1
    

    resp = input()


    while resp.lower() != 'v':
        print(Fore.BLUE +
              Style.BRIGHT +
              'Digite "V" para voltar à calcular.' +
              Style.RESET_ALL
              )
        resp = input()
        
        
    if resp.lower() == 'v':
        os.system('cls')
    else:
        print(Fore.BLUE +
              Style.BRIGHT +
              'Digite "V" para voltar à calcular.' +
              Style.RESET_ALL
              )


colorama.init()
l_historico = []