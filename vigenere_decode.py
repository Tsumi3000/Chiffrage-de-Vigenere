
def obtainIndex(letter=""):
    if letter.upper() == letter: return ord(letter) - 65, 65
    else: return ord(letter) - 97, 97

def newLetter(letter=0, index=0, add=0): return chr(25 - ((25 - letter + index)%26) + add)

def decode():
    text = input("Entrez votre message a decoder: ")
    check = True
    while True:
        for i in text:
            if((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)): check = False
        if(check): break
        print("La clé ne peut contenir que des lettres !")
        text = input("Entrez votre message a decoder: ")

    key = input("Entrez la clé utilisée pour chiffer ce message: ")
    check = True
    while check:
        for i in key:
            if((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)): check = False
        if(check): break
        print("La clé ne peut contenir que des lettres !")
        key = input("Entrez la clé utilisée pour chiffer ce message: ")

    newKey = ""
    for i in key: newKey = i + newKey
    key = newKey
    iter = 0

    start = len(text)%len(key)
    start = key[len(key) - start:]

    newText = ""
    lastText = ""
    for i in text:
        for m in i: newText = m + newText

    for i in range(len(newText)):

        if(start != ""): index, majIndex = obtainIndex(start[0])
        else: index, majIndex = obtainIndex(key[iter])
        letter, majLetter = obtainIndex(newText[i])

        newletter = newLetter(letter, index, majLetter)
        if newText[i] == "\n": newletter = "\n"
        lastText+=newletter

        if(start == ""): iter = (iter + 1)%len(key)
        else: start = start[1:]

    newText = ""
    for i in lastText: newText = i + newText

    print("Votre message:", text, "\nEst devenu:", newText)