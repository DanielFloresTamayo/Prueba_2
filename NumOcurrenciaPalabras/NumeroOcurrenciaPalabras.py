

#---------------------
def creartxt():
    texto = open('ConcurrenciaPalabras.txt', 'w')
    texto.close()

def grabartxt(textoUsuario):
    texto = open('ConcurrenciaPalabras.txt', 'a')
    texto.write(textoUsuario)
    texto.close()

def leertxt():
    texto=open('ConcurrenciaPalabras.txt','r')
    vertxt=texto.readline()
    while vertxt!="":
        print(vertxt)
        vertxt=texto.readline()
    texto.close()

def contadorPalabras(cadena):
    contador = 0
    # ------------////// con el lower se cambia de mayusculas a minusculas porque se necesita que el programa
    # /----------///////// relacione palabras tanto mayusculas como minusculas porque pueden ser iguales
    cadena = mensaje.lower().split(" ")
    for i in range(0, len(cadena)):
        # print(i)
        for j in range(0, len(cadena)):
            if cadena[j] == cadena[i]:
                contador = contador + 1

        print("La palabra '" + str(cadena[i] + "' se repite " + str(contador) + " veces\n"))
        # //////////----------El contador debe resetearce por cada interaccion
        contador = 0

#-----------------llamado a funciones

print("Nombre: Jefferson Omar Díaz Cando")

print("El texto del documento tiene el siguiente mensaje:\n")
mensaje="Las abejas obtienen polen de las flores, la miel es mas saludable que la azucar"

creartxt()
grabartxt(mensaje)
leertxt()
print()
# ////////////---------El texto cuenta con lo siguiente
contadorPalabras(mensaje)
