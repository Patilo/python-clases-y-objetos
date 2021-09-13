class Persona:
    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self): #se agrega el str para que no salga la info de la memoria
        return f' {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}'

class Empleado(Persona):
    def __init__(self,nombre,apellido,edad,sueldo):
        super().__init__(nombre,apellido,edad)  # super() para que llame al constructor de Persona
        self.sueldo = sueldo
    def __str__(self):
        return f'Empleado: {super().__str__()} y con sueldo de: {self.sueldo}'