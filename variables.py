a = 5
b = 8
c = a + b
print(c)

numero = 10
numero += 5
print(numero)

#Concatenar con + y snake_case es recomendable por python
nombre_completo = "Cristian Alcantara"
bienvenida = "Hola " + nombre_completo + " ¿Como estas?"
print (bienvenida)

#Concatenar con f string
#f String --- convierte todo a texto
nombre_completo = "Antonella"
bienvenida = f"Hola {nombre_completo} ¿Como estas?"
print (bienvenida)

# del borra dato
del nombre_completo 

#print(nombre_completo)

#buscar un texto dentro de cuna cadena

#operadores de pertenencia in o not in
print("Hola" in bienvenida) #operador de pertenencia true
print("Hola" not in bienvenida) #operador de pertenencia false
