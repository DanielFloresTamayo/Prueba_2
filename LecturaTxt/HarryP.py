def leer():
    archi=open('Cuento.txt','r')
    linea=archi.readline()
    while linea!="":
        print(linea)
        linea=archi.readline()
    archi.close

leer()

def contar():
    archi=open('Cuento.txt','r')
    archir=open('ResultadoContar.txt','w')
    p=0
    for i in archi.readlines():
        palabras=i.split(" ")
        p=p+len(palabras)
    print("\nel total de palabras es: ",p)
    archir.write("el total de palabras es: "+str(p))
    archi.close()
    archir.close()

contar()