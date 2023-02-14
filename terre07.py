while True:
    print("Veuillez entrer une chaîne de caractères :", end = " ")
    ch = input()
    a = len(ch)

    try:
        int(ch)
        print("Erreur.")
        break

    except:
        if ch.isspace():
            print("Erreur.")
            break

        if ch.count('"') or ("'") == 4:
            print("Erreur.")
            break


        if isinstance(ch,str):
            print(a)
            break

