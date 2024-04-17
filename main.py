#Codigo de calculadora
import funciones as fn

while True:

  a = int(input("Ingrese el primer numero: "))

  b = int(input("Ingrese el segundo numero: "))

  print("Estas son las opciones:")
  print("La letra S para la suma")
  print("La letra R para la resta")
  print("La letra M para la multiplicacion")
  print("La letrta D para la division")
  print("Salir")
  letra=input("Seleccione una opcion: ")


  if letra == "S":
    print(fn.suma(a, b))
  elif letra == "R":
    print(fn.resta(a, b))
  elif letra == "M":
    print(fn.multiplicacion(a, b))
  elif letra == "D":
    print(fn.division(a, b))
  elif letra == "Salir":
    break

#Codigo de oden
#Mayor a menor
lista_menor_mayor = [1,5,9,8,2,65,45,78,95,32,111,55,8,-5]
lista_ordenada = fn.menor_a_mayor(lista_menor_mayor)

#Menor a mayor
mayor_a_menor = [51,18,89,65,4,2,3,5,96,85,74,14,25,36,32,65,98,87,45,12]
lista_ordenada2 = fn.mayor_a_menor

#Alfabeticamente
alfabeticamente = ["Bruno","Joaquin","Martin","Gonzalo","Franco","Matias","Quimy","Marti"]
lista_ordenada3 = fn.alfabeticamente