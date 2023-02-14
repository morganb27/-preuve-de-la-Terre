print("Veuillez entrer une heure au format 24h (xx:xx) : ", end = "")
ch=input()

try:
    if (len(ch) != 5):
        print("Ce que vous avez entré ne correspond pas au format demandé.")
    elif (len(ch) == 5) & (ch[2] == ":"):
        a = int(ch[0])
        b = int(ch[1])
        c = int(ch[3])
        d = int(ch[4])
        if (a==0) & (b==0) & (0<=c<=5):
            print("12:", c,d, "(AM)", sep = "")
        elif (a==1) & (b==2) & (0<=c<=5):
            print("12:", c, d, "(PM)", sep = "")
        elif (a==0) & (1<b<9) & (0<=c<=5):
            print(b,":", c,d, sep = "")
        elif (a==1) & (0<=b<=1) & (0<=c<=5):
            print(a, b, ":", c, d, sep="")
        elif (a==1) & (3<=b<=9) & (0<=c<=5):
            a = str(a)
            b = str(b)
            e = int(a+b)
            e = (e - 12)
            print(e, ":", c, d, sep="")
        elif (a == 2) & (0 <= b <= 3) & (0<=c<=5):
            a = str(a)
            b = str(b)
            e = int(a + b)
            e = (e - 12)
            print(e, ":", c, d, sep="")
        else:
            print("Ce que vous avez entré ne correspond pas au format demandé.")


    else:
        print("Ce que vous avez entré ne correspond pas au format demandé.")


except:
    print(print("Ce que vous avez entré ne correspond pas au format demandé."))
