#class FiguraGeometrica:
#
#    def getArea()
#    
#    def getPerimetro()
    
#---    

class Rectangulo:
    
    # Constructor: Funcion que se llamará cuando queramos contruir un nuevo Rectangulo
    def __init__(self, la_base, la_altura):
        self.base   = la_base
        self.altura = la_altura
        self.__inicializado=True

    def getArea(self):
        print(self.__inicializado)
        return self.base * self.altura
    
    def getPerimetro(self):
        return ( self.base + self.altura ) * 2

    # self es el alma del nuevo dato que creo

rectangulo1=Rectangulo(10,5) # Python, internamente, lo que hace al ver esta siuntaxis es:
                             # Crear un self, un alma, y llamar a la funcion __init__
rectangulo2=Rectangulo(5,2)

print( rectangulo1.getArea() )

# mitexto=str("hola")
# print(mitexto.upper())



class Cuadrado( Rectangulo ):   # Herencia
    
    # Constructor: Funcion que se llamará cuando queramos contruir un nuevo Rectangulo
    def __init__(self, el_lado):
        super().__init__(el_lado, el_lado) # super hace alusión al RECTANGULO


cuadrado1=Cuadrado(5)

print( cuadrado1.base )
print( cuadrado1.altura )
print( cuadrado1.getArea() )
print( cuadrado1.getPerimetro() )
