while True:
    print("Veuillez entrer un nombre et sa puissance :", end = " ")
    ch=input()

    ch = ch.split(" ")

    try:
        if len(ch) >= 3:
            print("Tu ne me la mettras pas à l'envers ! ;)")
            break
        else:
            a = ch[0]
            b = ch[1]

            a = int(a)
            b = int(b)

            if b < 0:
                print("Erreur.")
                break
            else:
                print(a ** b)
                break

    except:
        print("Tu ne me la mettras pas à l'envers ! ;)")
        break


