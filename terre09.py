from math import sqrt

while True:
    print("Veuillez entrer un nombre entier positif :", end = " ")
    ch=input()

    ch = ch.split(" ")

    try:
        if len(ch) >= 2:
            print("Tu ne me la mettras pas à l'envers ! ;)")
            break
        else:
            a = ch[0]

            a = int(a)


            if a <= 0:
                print("Erreur.")
                break
            else:
                b = sqrt(a)
                print(b)
                break

    except:
        print("Tu ne me la mettras pas à l'envers ! ;)")
        break


