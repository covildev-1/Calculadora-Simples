from Historico import l_historico

def calcular(entrada):
    resultado = eval(entrada)
    l_historico.append(entrada + '=' + str(resultado))

    
    return (resultado)