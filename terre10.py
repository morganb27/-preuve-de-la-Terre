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
                print("Tu ne me la mettras pas à l'envers ! ;).")
                break
            else:
                if (a > 1) & (a % 1 == 0) & (a % a == 0):
                    b = True
                    for i in range(2,a):
                        if a % i ==0:
                            b = False

                    if b == True:
                        print("Oui,", a, "est un nombre premier.")

                    else:
                        print("Non,", a, "n'est pas un nombre premier.")

                else:
                    print("Non,", a, "n'est pas un nombre premier.")

    except:
        print("Tu ne me la mettras pas à l'envers ! ;)")
        break
