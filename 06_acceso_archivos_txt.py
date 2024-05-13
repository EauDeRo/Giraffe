#la carpeta main es C:\Users\rocio.guichoux\Desktop\curso python\curso freecodecamp\Giraffe
# el .py en la carpeta C:\Users\rocio.guichoux\Desktop\curso python\curso freecodecamp\Giraffe\06_acceso_archivos_txt
#Crea un fichero en C:\Users\rocio.guichoux\Desktop\curso python\curso freecodecamp\Giraffe\ficheros
txt_hi =open("ficheros/hi.txt","w")
txt_hi.write("¡Hola!estoy creando un fichero nuevo o  borrando y escribiendo en un fichero hi.txt existente")
txt_hi.close()

txt_hi_append = open("ficheros/hi.txt","a")
txt_hi_append.write("\n Esta es la segunda linea del fichero que he añadido luego")
txt_hi_append.close()


txt_hi_read = open("ficheros/hi.txt","r")
print(txt_hi_read.readlines())
txt_hi_read.close()


txt_hi_read2 = open("ficheros/hi.txt","r")
for line in txt_hi_read2.readlines():
    print("\n leyendo for   " + line)
txt_hi_read2.close()
