# Cual entero es mayor

print("---------------------------------")
print("------Mayor entre enteros--------")
print("---------------------------------")


# input
a = int(input("Digite el primer numero: "))
b = int(input("Digite el segundo numero: "))
c = int(input("Digite el tercer numero: "))

# procesing and output
if a > b and a > c:
    print("El numero " +str(a)+" es mayor que "+str(b)+" y mayor que "+str(c))
elif b > a and b > c:
     print("El numero " +str(b)+" es mayor que "+str(a)+" y mayor que "+str(c))
else :
      print("El numero " +str(c)+" es mayor que "+str(b)+" y mayor que "+str(a))

print("-----------FIN--------------")
