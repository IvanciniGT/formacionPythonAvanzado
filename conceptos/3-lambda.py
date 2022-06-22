

lista_de_funciones = []

def creadorDeFuncionDeImprimir(numero):
    
    def imprimir():
        print(numero)
        
    return imprimir

for numero in range(10):
    lista_de_funciones.append( creadorDeFuncionDeImprimir(numero) )    
    # RUINA !!!! lista_de_funciones.append( lambda: print(numero) )    

for funcion in lista_de_funciones:
    print(funcion)
    funcion()
    