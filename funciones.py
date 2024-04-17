#Funciones calculadora
def suma (a, b):
  resultado = a + b
  return resultado

def resta (a, b):
  resultado = a - b
  return resultado

def multiplicacion (a, b):
  resultado = a * b
  return resultado

def division (a, b):
  resultado = a / b
  return resultado

#Funciones de orden
#mayor a menor
def menor_a_mayor(list1):
    
    stop=True
    list_ord=[]
    while stop:
        val_max=list1[0]

    for i in range(len(list1)):
        x = list1[i]
        if x > val_max:
            val_max=x

    list_ord.append(val_max)
    list1.remove(val_max)

    if len(list1) == 0:
        stop = False
    print(list_ord)

    return list_ord

#menor a mayor
def mayor_a_menor(list2):
   
   stop=True
   list_ord=[]
   while stop:
      val_min = list2[0]
      for i in range(len(list2)):
         x = list2[i]
         if x < val_min:
            val_min = x
      list_ord.append(val_min)
      list2.remove(val_min)
      if len(list2) == 0:
         stop = False
      print(list_ord)

      return list_ord

#alfabeticamente
def alfabeticamente(list3):
   list3.sort()
   print(list3)

   return list3
