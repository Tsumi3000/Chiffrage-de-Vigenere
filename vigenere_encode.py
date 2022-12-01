
def obtainIndex(letter=""):
    if letter.upper() == letter: return ord(letter) - 65, 65
    else: return ord(letter) - 97, 97

def newLetter(letter=0, index=0, add=0): return chr((letter + index)%26 + add)

def encode():
    text = input("Type your message to decode: ")
    check = True
    while True:
        for i in text:
            if((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)): check = False
        if(check): break
        print("The message can only contain letters !")
        text = input("Type your message to decode: ")

    key = input("Type the key used to encrypt this message: ")
    check = True
    while check:
        for i in key:
            if((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)): check = False
        if(check): break
        print("The key can only contain letters !")
        key = input("Type the key used to encrypt this message: ")

    iter = 0
    newText = ""

    for ligne in text:

        for i in range(len(ligne)):

            index, majIndex = obtainIndex(key[iter])
            letter, majLetter = obtainIndex(ligne[i])

            newletter = newLetter(letter, index, majLetter)
            if (ord(newText[i]) > 65 or 90 < ord(newText[i]) < 97): newletter = newText[i]
            newText+=newletter

            iter = (iter + 1)%len(key)

    print("Your message:", text, "\nIs become:", newText)