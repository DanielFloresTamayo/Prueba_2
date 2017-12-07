

def leertxt():
    archi=open('cuento.txt','r')
    linea=archi.readline()
    datos=linea
    while linea!="":
      print(linea)  # se puede comentar esta linea para que no aparesca todo el texto
      linea=archi.readline()

    archi.close()
    nuevo = datos.split(" ")
    print("Existen: "+str(len(nuevo))+" palabras")

    # for p in texto:
    #     print(p, len(p))

leertxt()

print("Nombre: Jefferson Omar Diaz")