print("Veuillez entrer un nombre entier (positif ou négatif) :", end = " ")
ch = input()
try:
    ch=int(ch)
except:
    print("Tu ne me la mettras pas à l'envers.")

else:
    if ch % 2 == 0:
        print("Il s'agit d'un nombre pair.")
    else:
        print("Il s'agit d'un nombre impair.")

