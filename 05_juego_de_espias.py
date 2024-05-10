def codificar (frase,original,reemplazo):
    lista_compare=["Lo","QUE","SEA"]
    if len(original) != len(reemplazo) or (type(original) != type(lista_compare) ) or (type(reemplazo) !=  type(lista_compare) ) :
        print("format error")
        frase_cod=frase
    else: 
        repeticion=0
        for rem in reemplazo:
             for ori in original:
                if(rem==ori): repeticion=1
        
        if repeticion==1:
           print("no pueden coincidir ninguna letra de orininal y reemplazo")
           frase_cod=frase
        else:
            for letter in original:
                pos=original.index(letter)
                frase=frase.replace(str(letter),str(reemplazo[pos]))
            frase_cod=frase
            
    return(frase_cod)

frase=input"dime la frase :  "
original=["a","e","i","o","u"]
reemplazo=[1,2,3,4,5]
print(type(original))
print(type(reemplazo))

frase_cod=codificar(frase,original,reemplazo)

print(frase_cod)
# frase=input("dime que frase quieres codificar :  ")
#orininal =("¿Qué letras quieres cambiar? :  )
####