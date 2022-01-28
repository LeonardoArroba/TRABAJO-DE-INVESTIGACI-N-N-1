from helpers import Helper
from Cargo import Cargo
from Empleado import Empleado
from Departamento import Departamento
import re

class Validar:
    def valCargo(cadena):
        if 1 <= len(cadena) <=20:
            if re.search('[a-z]', cadena) or re.search('[A-Z]', cadena) or re.search('[ ]', cadena):
                car1 = Cargo(cadena)
                cate = car1.registro()
                Cargo.cargos.append(cate)
                print(" ")
                print("*"*37)
                print("Datos ingresados satisfactoriamente")
        else:
            print(" ")
            print("*"*37)
            print("Ingrese entre 1 a 20 caracteres")
    
    def valDepartamento (cadena):
        if 5 <= len(cadena) <=20:
            if re.search('[a-z]', cadena) or re.search('[A-Z]', cadena) or re.search('[ ]', cadena):
                dep1 = Departamento(cadena)
                depe = dep1.registro()
                Departamento.departamentos.append(depe)
                print(" ")
                print("*"*37)
                print("Datos ingresados satisfactoriamente")
        else:
            print(" ")
            print("*"*37)
            print("Ingrese entre 5 a 20 caracteres")
           
