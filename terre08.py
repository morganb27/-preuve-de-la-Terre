import sys

def puissance_nombre():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    p = 1
    for i in range(b):
        p = p * a
    print(p)

puissance_nombre()


