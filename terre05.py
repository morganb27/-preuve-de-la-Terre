print("Veuillez saisir deux nombres positifs :", end = " ")
ch = input()
ch = ch.split(" ")

try:
    a = int(ch[0])
    b = int(ch[1])

except:
    b=0
    a=0
    print("Erreur. Vous deuvez saisir deux nombres positifs.")



if (a>=b) & (b != 0):
    print("résultat :", (a//b))
    print("reste :", (a%b))
elif (b==0) & (a != 0):
    print("erreur.")
elif (a==0) & (b==0):
    print("")
else:
    print("erreur.")

