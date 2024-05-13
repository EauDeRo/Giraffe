from gestion_clientes import *

lista_clientes=[]
cliente0 = Cliente("cocacola","ftp.patata.com","cocacola_es","123456")
lista_clientes.append(cliente0)
cliente1 = Cliente("pepsi","ftp.frita.com","pepsi_es","abcdef")
lista_clientes.append(cliente1)
cliente2 = Cliente("hacendado","ftp.ketchup.com","hacendado_es","a1b2c3")
lista_clientes.append(cliente2)
añadido=[]
for cliente in lista_clientes:
    añade=añadir_cliente_txt(cliente)
    añadido.append(añade)
    

print(añadido)

encontrado=busca_cliente_txt(cliente2)

print(encontrado)