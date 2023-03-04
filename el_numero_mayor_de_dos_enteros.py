# Cual de los dos enteros es mayor

print("-------------------------------")
print("---------Mayor o menor---------")
print("-------------------------------")


# input 
a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))

# procesing and output
if a == b:
 print("los numeros son iguales")
else:
 if (a > b):
   mayor = a
   print("EL mayor es: "+str(a))
 else:
  mayor = b
  print("El mayor es: "+str(b))


 

