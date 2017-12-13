frase=input("Frase: ")
fra=frase.split(".")
for i in fra:
    pal = len(i.split(" "))
    print("Frase: ", i, ":", pal)

for p in palabras:
    print(p,len(p))