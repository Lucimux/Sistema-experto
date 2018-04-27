import sys, re
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton
from PyQt5 import uic
from Paciente import Paciente
from Diagnostico import DiagnosTicoEngine, DatosPaciente, NuevoPaciente
class SistemaExpertoGUI(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('GUI.ui',self)
        self.Calcular.clicked.connect(self.getDieta)
        self.nombre.textChanged.connect(self.validar_nombre)

    def closeEvent(self, event):
        result = QMessageBox.question(self, "Salir .... ? ","Seguro que quieres salir de la aplicacion", QMessageBox.Yes,QMessageBox.No)
        if result == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def validar_nombre(self): 
        nombre = self.nombre.text()
        validar = re.match('^[a-zA-Z\s]+$',nombre,re.I)
        if nombre == "":
            self.nombre.setStyleSheet("border: 1px solid red;")
            return False
        elif not validar:
            self.nombre.setStyleSheet("border: 1px solid red;")
            return False
        else: 
            self.nombre.setStyleSheet("border: 1px solid black;")            
            return True
            
    def generoValue(self):
        if self.masculino.isChecked():
            return "masculino"
        elif self.femenino.isChecked():
            return "femenino"
    
    def getDieta(self):
        nombre = self.nombre.text()
        edad = int(self.edad.text())
        estatura = float(self.estatura.text())
        cintura = float(self.cintura.text())
        cadera = float(self.cadera.text())        
        peso_actual = float(self.peso_actual.text())
        peso_habitual = float(self.peso_habitual.text())
        perimetro_abdominal = float(self.perimetro_abdominal.text())
        circunferencia_mun = float(self.circunferencia_mun.text())
        sexo = self.generoValue()
        paciente = Paciente(nombre,sexo,edad,estatura,cintura,cadera,peso_actual,peso_habitual,perimetro_abdominal,circunferencia_mun)
        algo = DiagnosTicoEngine()
        algo.reset()
        algo.GenerarDatos()
        algo.declare(
            NuevoPaciente(
                sexo=paciente.sexo,
                nombre=paciente.nombre,
                edad=paciente.edad,
                estatura=paciente.estatura,
                cintura=paciente.cintura,
                cadera=paciente.cadera,
                pesoActual=paciente.pesoActual,
                perimetroAbd=paciente.perimetroAbdominal,
                circfMun=paciente.circunfMun,
                pesoHabit=paciente.pesoHabitual
            )
        )
        algo.run()
        print(algo.facts)



app = QApplication(sys.argv)
#crear objeto de la clase)
ventana = SistemaExpertoGUI()
#mostrar la ventana
ventana.show()
#ejecutar la aplicacion
app.exec_()