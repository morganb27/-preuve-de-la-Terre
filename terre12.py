print("Veuillez entrer une heure au format 12h (xx:xxAM ou x:xxAM) : ", end = "")
ch=input()


try:
    if (len(ch) == 7) & (ch[2] == ":"):
        a = int(ch[0])
        b = int(ch[1])
        c = int(ch[3])
        d = int(ch[4])
        f = ch[5]
        if (a==1) & (0<=b<=1) & (0<=c<=5) & (f == "A"):
            print(a, b, ":", c, d, sep = "")
        elif (a==1) & (0<=b<=1) & (0<=c<=5) & (f == "P"):
            a = a + 1
            b = b + 2
            print(a, b, ":", c, d, sep = "")
        elif (a==1) & (b==2) & (0<=c<=5) & (f == "A"):
            a = 0
            b = 0
            print(a, b, ":", c, d, sep="")
        elif (a==1) & (b==2) & (0<=c<=5) & (f == "P"):
            print(a, b, ":", c, d, sep="")
        else:
            print("Ce que vous avez entré ne correspond pas au format demandé.")

    elif (len(ch) == 6) & (ch[1] == ":"):
        a = int(ch[0])
        b = int(ch[2])
        c = int(ch[3])
        f = ch[4]
        if (1<=a<=9) & (0<=b<=5) & (f == "A"):
            print("0", a, ":", b, c, sep = "")
        if (1<=a<=9) & (0<=b<=5) & (f == "P"):
            a = a + 12
            print(a, ":", b, c, sep = "")
    else:
        print("Ce que vous avez entré ne correspond pas au format demandé.")


except:
    print("Ce que vous avez entré ne correspond pas au format demandé.")