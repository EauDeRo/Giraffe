#este programa permite acceder a dos funciones : 
#   una que añade clientes a ficheros/lista_de_clientes.txt 
#   otra que permite buscar un cliente en la lista ficheros/lista_de_clientes.txt
from clientes import Cliente

def añadir_cliente_txt (cliente_añadir):
    if isinstance (cliente_añadir,Cliente) :
        txt_append =open("ficheros/lista_de_clientes.txt","a")
        txt_append.write( "\n"+cliente_añadir.name+";"+cliente_añadir.ftp+";"+cliente_añadir.user+";"+cliente_añadir.pasword)
        txt_append.close()
        return("DONE")
    else :return("ERROR")

def busca_cliente_txt (cliente_buscar):
    presente=0
    if isinstance (cliente_buscar,Cliente) :
        cli= cliente_buscar.name +";"+cliente_buscar.ftp+";"+cliente_buscar.user+";"+cliente_buscar.pasword
        txt_read =open("ficheros/lista_de_clientes.txt","r")

        for line in txt_read.readlines():
            if cli == line: presente=1

        txt_read.close()
    return (presente)

#inicializando fichero

#cliente_cero =Cliente("name","ftp","user","pasword")
#añadido=añadir_cliente_txt(cliente_cero)
#encontrado=busca_cliente_txt(cliente_cero)

#print("Añadido = " + añadido +"\nEncontrado = " + str(encontrado))
