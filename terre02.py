print("Veuillez entrer vos arguments :", end = " ")
ch = input()
#type(ch) = 'str'

ch = ch.split(" ") #split ch into a list of words

for argument in ch:
    print(argument)