def creartxt():
    archi=open('lectura.txt','w')
    archi.close()

def grabartxt():
    archi=open('lectura.txt','a')
    archi.write(input("Frase"))
    archi.close()

def leertxt():
    archi=open('lectura.txt','r')
    linea=archi.readline()
    datos=linea
    while linea!="":
     # print(linea)  # se puede comentar esta linea para que no aparesca todo el texto
      linea=archi.readline()

    archi.close()
    nuevo = datos.split(" ")
    print("Existen: "+str(len(nuevo))+" palabras")

def leertxt2():
    archi=open('cuento.txt','r')
    linea=archi.readline()
    datos=linea
    while linea!="":
      print(linea)  # se puede comentar esta linea para que no aparesca todo el texto
      linea=archi.readline()

    archi.close()
    nuevo = datos.split(" ")
    print("Existen: "+str(len(nuevo))+" palabras")

creartxt()
grabartxt()
leertxt()
leertxt2()

print("Nombre: Jefferson Omar Diaz")
print("Nombre: Daniel Flores")
print("Nombre: Jefferson Llumiquinga")