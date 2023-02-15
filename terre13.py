print("Veuillez entrer trois nombres séparés par des espaces :", end = " ")
ch = input()
ch = ch.split()

try:
    a, b, c = map(int, ch)
    if (b<a<c):
        print(a)
    elif (a<b<c):
        print(b)
    elif (a<c<b):
        print(c)
    else:
        print("erreur.")



except:
    print("erreur.")
