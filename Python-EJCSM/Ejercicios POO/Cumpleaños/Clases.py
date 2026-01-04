
class Persona:

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.__dni = dni
    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    @property
    def dni(self):
        return self.__dni

class Fecha:
    
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'
    

