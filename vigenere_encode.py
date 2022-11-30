
def obtainIndex(letter=""):
    if letter.upper() == letter: return ord(letter) - 65, 65
    else: return ord(letter) - 97, 97

def newLetter(letter=0, index=0, add=0): return chr((letter + index)%26 + add)

def encode():
    text = input("Entrez votre message a encoder: ")
    check = True
    while True:
        for i in text:
            if((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)): check = False
        if(check): break
        print("La clé ne peut contenir que des lettres !")
        text = input("Entrez votre message a encoder: ")

    key = input("Entrez la clé utilisée pour chiffer ce message: ")
    check = True
    while check:
        for i in key:
            if((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)): check = False
        if(check): break
        print("La clé ne peut contenir que des lettres !")
        key = input("Entrez la clé utilisée pour chiffer ce message: ")

    iter = 0
    newText = ""

    for ligne in text:

        for i in range(len(ligne)):

            index, majIndex = obtainIndex(key[iter])
            letter, majLetter = obtainIndex(ligne[i])

            newletter = newLetter(letter, index, majLetter)
            if ligne[i] == "\n": newletter = "\n"
            newText+=newletter

            iter = (iter + 1)%len(key)

    print("Votre message:", text, "\nEst devenu:", newText)