import re
from pyknow import *
import csv

class DatosPaciente(Fact):
    pass

class Dieta(Fact):
    pass
    
class NuevoPaciente(Fact):
    pass

class DiagnosTicoEngine(KnowledgeEngine):
        
    def GenerarDatos(self):
        with open('Datos.csv') as archivoCsv:
            datos = csv.reader(archivoCsv)
            next(datos, None)
            for dato in datos:
                sexo, peso, edad, estatura, cintura, cadera, pesoTeoIdeal, circMun, porPesoT, ICC, pesoHabit, complexion, antecedentes, ejercicio = dato
                self.declare(DatosPaciente(sexo=sexo,peso=str(peso), edad=str(edad), estatura=str(estatura), cintura=str(cintura),cadera=str(cadera), 
                pesoTeoIdeal=str(pesoTeoIdeal), circunfMun=str(circMun), porPesoTeorico=str(porPesoT), 
                icc=str(ICC), porPesoHabit=str(pesoHabit), complexion=str(complexion), antecedentes=str(antecedentes), ejercicio=str(ejercicio)))
    @Rule(
        NuevoPaciente(
            nombre=MATCH.nombre,
            sexo=MATCH.sexo,
            edad=MATCH.edad,
            estatura=MATCH.estatura,
            cintura=MATCH.cintura,
            cadera=MATCH.cadera,
            pesoActual=MATCH.pesoActual,
            perimetroAbd=MATCH.PA,
            circfMun=MATCH.circunfMun,
            pesoHabit=MATCH.PH
        ),
        DatosPaciente(
            sexo = MATCH.sexo & L('masculino')
            #peso=MATCH.peso & P(lambda peso: re.match(/^masculino$/, peso)),
            #edad=MATCH.edad & P(lambda edad: re.match(r"\d+x\d+", edad)),
            #estatura=MATCH.estatura & P(lambda estatura: re.match(r"\d+x\d+", estatura)),
            #cintura=MATCH.cintura & P(lambda cintura: re.match(r"\d+x\d+", cintura)),
            #cadera=MATCH.cadera & P(lambda cadera: re.match(r"\d+x\d+", cadera)),
            #pesoTeoIdeal=MATCH.pesoTeoIdeal & P(lambda pesoTeoIdeal: re.match(r"\d+x\d+", pesoTeoIdeal)),
            #circunfMun=MATCH.circunfMun & P(lambda circunf: re.match(r"\d+x\d+", circunfMun)),
            #porPesoTeorico=MATCH.ppt & P(lambda ppt: re.match(r"\d+x\d+", ppt)),
            #icc=MATCH.icc & P(lambda icc: re.match(r"\d+x\d+", icc)),
            #porPesoHabit=MATCH.pph & P(lambda pph: re.match(r"\d+x\d+", pph)),            
            #complexion=MATCH.complexion & P(lambda complexion: re.match(r"\d+x\d+", complexion)),
            #antecedentes=MATCH.antecedentes & P(lambda antecedentes: re.match(r"\d+x\d+", antecedentes)),
            #ejercicio=MATCH.ejercicio & P(lambda sexo: re.match(r"\d+x\d+", ejercicio)),        
        ))
    #def DietaHombres(self,nombre,sexo,peso,edad,estatura,cintura,cadera,pesoTeoIdeal,circunfMun,ppt,icc,pph,complexion,antecedentes,ejercicio,pesoActual,PA,PH):
    def DietaHombres(self,nombre,sexo,edad,estatura,cintura,cadera,pesoActual,PA,circunfMun,PH):    
        self.declare(Dieta(nombre="Dieta para el marrano de:"+nombre))        
    
    @Rule(
        NuevoPaciente(
            nombre=MATCH.nombre,
            sexo=MATCH.sexo,
            edad=MATCH.edad,
            estatura=MATCH.estatura,
            cintura=MATCH.cintura,
            cadera=MATCH.cadera,
            pesoActual=MATCH.pesoActual,
            perimetroAbd=MATCH.PA,
            circfMun=MATCH.circunfMun,
            pesoHabit=MATCH.PH
        ),
        DatosPaciente(
            sexo = MATCH.sexo & L('masculino')
            #peso=MATCH.peso & P(lambda peso: re.match(/^masculino$/, peso)),
            #edad=MATCH.edad & P(lambda edad: re.match(r"\d+x\d+", edad)),
            #estatura=MATCH.estatura & P(lambda estatura: re.match(r"\d+x\d+", estatura)),
            #cintura=MATCH.cintura & P(lambda cintura: re.match(r"\d+x\d+", cintura)),
            #cadera=MATCH.cadera & P(lambda cadera: re.match(r"\d+x\d+", cadera)),
            #pesoTeoIdeal=MATCH.pesoTeoIdeal & P(lambda pesoTeoIdeal: re.match(r"\d+x\d+", pesoTeoIdeal)),
            #circunfMun=MATCH.circunfMun & P(lambda circunf: re.match(r"\d+x\d+", circunfMun)),
            #porPesoTeorico=MATCH.ppt & P(lambda ppt: re.match(r"\d+x\d+", ppt)),
            #icc=MATCH.icc & P(lambda icc: re.match(r"\d+x\d+", icc)),
            #porPesoHabit=MATCH.pph & P(lambda pph: re.match(r"\d+x\d+", pph)),            
            #complexion=MATCH.complexion & P(lambda complexion: re.match(r"\d+x\d+", complexion)),
            #antecedentes=MATCH.antecedentes & P(lambda antecedentes: re.match(r"\d+x\d+", antecedentes)),
            #ejercicio=MATCH.ejercicio & P(lambda sexo: re.match(r"\d+x\d+", ejercicio)),        
        ))
    
    def DietaMujeres(self,sexo):
        print("Hechate otros taquitos marrana :v")
        self.declare(Dieta(carnes="Pura lechuguita marrana"))
        