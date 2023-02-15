print("Veuillez entrer des nombres entiers séparés par des espaces :", end = " ")
ch = input()
ch = ch.split()
i = 0
nombres = []

try:
    for num in ch:
        nombres.append(int(num))


    triée = all(nombres[i] < nombres[i+1] for i in range(len(nombres)-1))

    if triée == True:
        print("Triée !")

    else:
        print("Pas triée !")


except:
    print("Erreur.")
