from helpers import Helper
from Cargo import Cargo
from Empleado import Empleado
from Departamento import Departamento
from Validar import Validar
import os
import re

def buscargo(cod):
  car = "Sin cargo"    
  for pos in range(0,len(Cargo.cargos)):
    cargo = Cargo.cargos[pos]
    if cargo["codigo"] == cod:
       car = cargo["cargo"]
       break
  return car    


def buscardepartamento(cod):
  dep = "Sin departamento"     
  for pos in range(0,len(Departamento.departamentos)):
    departamento = Departamento.departamentos[pos]
    if departamento["codigo"] == cod:
       dep = departamento["departamento"]
       break
  return dep    
     

helper = Helper()
lista = ["1) Cargo","2) Departamento","3) Empleados","4) Salir"]
opcion=""
while opcion != "4":
  os.system("cls")
  opcion = helper.menu(lista,"*"*20+" MENÚ FICHA PERSONAL "+"*"*20)
  if opcion == "1":
    opc1= ""
    while opc1 != "3":
      os.system("cls")
      opc1 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"*"*18+" MANTENIMIENTO DE CARGOS "+"*"*17)
      os.system("cls")
      if opc1 == "1":
        print("*"*10+"INGRESO DE CARGOS"+"*"*10)
        nombre = input("Cargo: ")
        car = Validar.valCargo(nombre)
        print(" ")
        input("Presiones una tecla para continuar...")   

      elif opc1 == "2":
        print("*"*10," LISTADO DE CARGOS ","*"*10)  
        print("Codigo"," "*5,"Cargo")
        for carg in Cargo.cargos:
          cod = carg["codigo"]
          car = carg["cargo"]
          carb = buscargo(car)
          print(" "*1,cod," "*6,car)
        print("*"*41)
        print(" ")
        input("Presione una tecla para continuar...")
            
  elif opcion == "2":
    opc2 = ""
    while opc2 != "3":
      os.system("cls")
      opc2 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"*"*14+" MANTENIMIENTO DE DEPARTAMENTOS "+"*"*14)
      os.system("cls")
      if opc2 == "1":
        print("*"*10,"INGRESO DE DEPARTAMENTOS")
        nombre = input("Departamento: ")
        dep = Validar.valDepartamento(nombre)
        print(" ")
        input("Presiones una tecla para continuar...")
          
      elif opc2 == "2":
        print("*"*10," LISTADO DE DEPARTAMENTOS ","*"*10) 
        print("Codigo"," "*5,"Departamento") 
        for depg in Departamento.departamentos:
          cod = depg["codigo"]
          dep = depg["departamento"]
          depb = buscardepartamento(dep)
          print(" "*1,cod," "*6,dep)
        print("*"*48)
        print(" ")
        input("Presione una tecla para continuar...")
               
  elif opcion == "3":
    opc3 = ""
    while opc3 != "3":
      os.system("cls")
      opc3 = helper.menu(["1) Ingreso","2) Consulta","3) Salir"],"*"*16+" MANTENIMIENTO DE EMPLEADOS "+"*"*16)
      os.system("cls")
      if opc3 == "1":
          print("*"*20,"INGRESO DE EMPLEADOS ","*"*20)
          nombre= input("Nombre del Empleado: ")
          cedula= input("Cedula del Empleado: ")
          cargo= int(input("Codigo del cargo: "))
          departamento= int(input("Departamento: "))
          sueldo = float(input("Sueldo del Empleado: "))
          emp = Empleado(nombre,cedula,cargo,departamento,sueldo)
          empleado = emp.registro()
          Empleado.empleados.append(empleado)
          print(" ")
          input("Datos ingresados satisfactoriamente, presiones una tecla para continuar...")
      
      elif opc3 == "2":
          print("*"*32,"LISTADO DE EMPLEADOS ","*"*32)
          print("Codigo"," "*5,"Nombre"," "*5,"Cedula"," "*8,"Cargo"," "*8,"Departamento"," "*10,"Sueldo")
          for emp in Empleado.empleados:
            cod = emp["codigo"]
            nom = emp["nombre"]
            ced = emp["cedula"]
            car = emp["cargo"]
            carb = buscargo(car)
            dep = emp["departamento"]
            depb = buscardepartamento(dep)
            sul = emp["sueldo"]
            print(" "*2,cod," "*8,nom," "*(10-len(nom)),ced," "*(6-len(ced))," "*2,carb," "*6,depb," "*6,sul)
          print("*"*87)
          print(" ")
          input("Presione una tecla para continuar...")

  elif opcion == "4":
      print("Salir") 
print("Gracias por visitarnos")  




