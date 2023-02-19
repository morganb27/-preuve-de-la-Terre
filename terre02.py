import sys

def affiche_arguments():
    for i in range(1, len(sys.argv)):
        print(sys.argv[i])

affiche_arguments()

