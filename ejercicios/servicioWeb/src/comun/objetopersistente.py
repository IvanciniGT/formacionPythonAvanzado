from servicios.inicializador import base_datos

class ObjetoPersistente:
    
    def guardar(self):
        # SQL Alchemy: 
        # Guardame el objeto en esta base de datos
        # En función del TIPO DE OBJETO (Clase)
        # En función de las columnas que haya definido
        # Contruye la query... YO ME OLVIDO
        base_datos.session.add(self) # INSERT
        base_datos.session.commit()

    def borrar(self):
        base_datos.session.delete(self)
        base_datos.session.commit()
        
    @classmethod
    def recuperar(cls,id):
        # Dame de la tabla correcpondiente (cls)
        # El elemento con el id suministrado
        return cls.query.get(id)
    
    @classmethod
    def recuperarTodos(cls):
        # Dame de la tabla correcpondiente (cls)
        # todo
        return cls.query.all()
    