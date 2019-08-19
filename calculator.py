"""
Your module documentation here
"""

class CalculatorClass(object):
   lista = []
   num = 0
   def llenarlista(self):
       x= int (input("Ingrese Tamaño De La Lista:"))
       for i in range(x):
           #add numbers
           self.lista.append(int(input("Ingrese Numero:")))
       #print list
       for i in self.lista:
           print (i)
 
   def sumar(self):
       for i in self.lista:
           self.num+= i
       print ("La Suma De Los Datos Es:",self.num)
 
obj = CalculatorClass()
obj.llenarlista()
obj.sumar()
