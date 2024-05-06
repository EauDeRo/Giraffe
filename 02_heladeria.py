mensaje_bienvenida= "Bienvenidos a la heladeria saludable"
print(mensaje_bienvenida)
name=input("¡Buenos días! ¿Dómo te llamas?  : ")
print("¡saludos "+ name +"! Que la fuerza te acompañe.")
contenedor=input("¿Qué vas a tomar tarrina o cucurucho?  : ")
num_bolas=input("¿Cuantas bolas de helado quieres?  : ")
if int(num_bolas) > 3: 
    print("Que listo calisto...venga te pongo 3 pero porque eres tú")
    num_bolas=3
elif int(num_bolas) < 0:
    print("no se admiten devoluciones")
    num_bolas=0

else:
    print("¡Buena ellección!")



