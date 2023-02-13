a = "abcdefghijklmnopqrstuvwxyz"
a = list(a)


print("Veuillez entrez une lettre de l'alphabet en minuscule :", end = " ")
ch = input()
i = -1

while ch != a[i]:
    i = i +1
    if ch == a[i]:
        a = (a[i:27])
        s = ''.join(a)
        print(s)
        print("\n")
        break






