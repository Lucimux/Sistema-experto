class Paciente():
    def __init__(self, nombre, sexo, edad, estatura, cintura, cadera, pesoActual, pesoHabit, perAbdominal, circunfMun):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad
        self.estatura = estatura
        self.cintura = cintura
        self.cadera = cadera
        self.pesoActual = pesoActual
        self.pesoHabitual = pesoHabit
        self.circunfMun = circunfMun
        self.perimetroAbdominal = perAbdominal

    def pesoTeoricoIdeal(self):
        return 21.5 * (self.estatura * self.estatura)

    def pocentajePesoTeorico(self):
        return (self.pesoActual / self.pesoTeoricoIdeal()) * 100

    def porcentajePesoHabitual(self):
        return (self.pesoActual / self.pesoHabitual) * 100

    def icc(self):
        return self.cintura / self.cadera
    
    def perimetroAbd(self):
        
        if self.pocentajePesoTeorico() <= 89.9: 
            return "Bajo peso"
        elif self.pocentajePesoTeorico() >= 90 and self.pocentajePesoTeorico() <= 120: 
            return "Peso aceptable"
        elif self.pocentajePesoTeorico() >= 120.1: 
            return "Sobrepeso"
        
        

