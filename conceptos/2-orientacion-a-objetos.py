#class FiguraGeometrica:
#
#    def getArea()
#    
#    def getPerimetro()
    
#---    

class Rectangulo:
    
    # Constructor: Funcion que se llamará cuando queramos contruir un nuevo Rectangulo
    def __init__(self, la_base, la_altura):
        self.__base   = None
        self.base = la_base
        self.__altura = None
        self.altura = la_altura
        self.__inicializado=True

    @property
        # Si no fuera un property, yo esto lo invocaría:     dato = myrectangulo.base()
        # Al ser un property, puedo usar esta otra sintaxis: dato = myrectangulo.base
        # Esto nos permite mantenimiento y evolutivos con bajo impacto en el codigo
        
    def base(self):
        return self.__base
        
    @base.setter
        # Si no fuera un setter, yo esto lo invocaría:     myrectangulo.base(17)
        # Al ser un setter, puedo usar esta otra sintaxis: myrectangulo.base=17
    def base(self, nuevaBase):
        if nuevaBase < 0 :
            raise ValueError("La base no puede ser negativa")
        self.__base=nuevaBase
    
    @property
        # Si no fuera un property, yo esto lo invocaría:     dato = myrectangulo.base()
        # Al ser un property, puedo usar esta otra sintaxis: dato = myrectangulo.base
        # Esto nos permite mantenimiento y evolutivos con bajo impacto en el codigo
        
    def altura(self):
        return self.__altura
        
    @altura.setter
        # Si no fuera un setter, yo esto lo invocaría:     myrectangulo.base(17)
        # Al ser un setter, puedo usar esta otra sintaxis: myrectangulo.base=17
    def altura(self, nuevaAltura):
        if nuevaAltura < 0 :
            raise ValueError("La base no puede ser negativa")
        self.__altura=nuevaAltura

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

rectangulo1.base=-5
print( rectangulo1.getArea() )

cuadrado1.base=8 # cagada 
# En este caso, que deberia pasar? la altura tambien es 8
print( cuadrado1.getArea() )
