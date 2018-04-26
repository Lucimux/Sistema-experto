import re
from pyknow import *
from SistemaExperto import DatosPaciente, Dieta
import csv

class DiagnosTicoEngine(KnowledgeEngine):
        
    def GenerarDatos(self):
        with open('Datos.csv') as archivoCsv:
            datos = csv.reader(archivoCsv)
            for dato in datos:
                sexo, peso, edad, estatura, cintura, cadera, perimetroAbd, circMun, porPesoT, pesoHabit, ICC, complexion, antecedentes, ejercicio = dato
                self.declare(DatosPaciente(sexo=sexo,peso= peso, edad=edad, estatura=estatura, cintura=cintura, cadera=cadera, perimetroAbd=perimetroAbd, circunfMun=circMun, porPesoTeorico=porPesoT, porPesoHabit=pesoHabit, icc=ICC, complexion=complexion, antecedentes=antecedentes, ejercicio=ejercicio))

    @Rule(DatosPaciente(sexo=MATCH.sexo & P(lambda sexo: re.match(r"\d+x\d+", sexo)),porPesoHabit=MATCH.porPesoHabit & P(lambda peso: re.match(r"\d+x\d+", porPesoHabit))))
    def wacharDieta(self,sexo,porPesoHabit):
        #print(sexo,porPesoHabit)
        print("Hechate otro pozolito marrano :v")
        self.declare(Dieta(carnes="Ni de pedo"))

watch('RULES','FACTS')
algo = DiagnosTicoEngine()
algo.reset()
algo.GenerarDatos()
algo.wacharDieta('masculino','Sin Denutricion')
algo.run()
print(algo.facts)
