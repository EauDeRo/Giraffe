#Este programa funciona si se encuentra en la carpeta C:\Users\Rocío\Desktop\PYTHON\curso
#Crea un fichero en C:\Users\Rocío\Desktop\PYTHON\ROG
txt_hi =open("ROG/hi.txt","w")
txt_hi.write("¡Hola!etoy borrando y escribiendo en un fichero txt")
txt_hi.close()

txt_hi_append = open("ROG/hi.txt","a")
txt_hi_append.write("\n Esta es la segunda linea del fichero que he añadido luego")
txt_hi_append.close()


txt_hi_read = open("ROG/hi.txt","r")

for line in txt_hi_read.readlines():
    print("\n leyendo for   " + line)

print(txt_hi_read.read())

txt_hi_read.close()
