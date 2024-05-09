peticion=input("Francesco ¿querías algo? no te he oido :  " )
educado=peticion.rfind("por favor")
print(educado)
num_intentos=3
intento=0
  
     
if educado == -1:
    while educado==-1 and  intento<=(num_intentos -1):
      if intento==0:
         peticion=input("\nsigo sin oirte:  " )
         educado=peticion.rfind("por favor")
      elif intento==1:
          peticion= input("\nasí no se dicen las cosas, pidemelo de nuevo: ")
          educado=peticion.rfind("por favor")
      else:
          peticion=input("\nse dice por favooorrr, venga última oportunidad: ")
          educado=peticion.rfind("por favor")
      intento+=1

if educado != -1 and intento >=1: 
    print("\n\nasí si, toma.")
elif educado == -1: 
    print( "\n\nAla pues ya no te lo doy,las cosas se piden por favor")
else :
    print("\n\nClaro toma.")


print("\nthe end")