
def indexInAlphabet(letter:str):

    # If letter is an upper
    if letter.upper() == letter:
        return ord(letter) - 65, True
    
    else:
        return ord(letter) - 97, False

choice = input("Do you want: Decode | Encode: ").upper()

while choice != "DECODE" and choice != "ENCODE":
    
    print("Veuillez rentrer une réponse valide !")
    choice = input("Do you want: Decode | Encode: ").upper()

if choice == "DECODE":

    def newLetter(letter:int, index:int, isUpper:bool):

        if isUpper:
            add = 65
        else:
            add = 97

        return chr((letter - index)%26 + add)

if choice == "ENCODE":

    def newLetter(letter:int, index:int, isUpper:bool):

        if isUpper:
            add = 65
        else:
            add = 97

        return chr((letter + index)%26 + add)
    
# Ask for messsage to encode
message = input(f"Type your message to {choice.lower()}: ")
check = True

while True:
    
    for i in message:

        isLetter = not (((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)))

        # If actual letter isn't a space or letter, restart the while loop
        if i != "\n" and i != " " and not isLetter:
            check = False

    if(check):
        break

    # Ask for messsage to encode
    print("The message can only contain letters !")
    message = input(f"Type your message to {choice.lower()}: ")


# Ask for key for decode
key = input(f"Type the key used to {choice.lower()} this message: ")
check = True

while True:

    for i in key:

        isLetter = not (((ord(i) < 65) or (90 < ord(i) < 97) or (ord(i) > 122)))

        # If actual letter isn't a space or letter, restart the while loop
        if i != "\n" and i != " " and not isLetter:
            check = False

    if(check):
        break

    # Ask for key for decode
    print("The key can only contain letters !")
    key = input(f"Type the key used to {choice.lower()} this message: ")

newMessage = ""
iter = 0

for i in range(len(message)):

    # Get informations about key and message
    index,_ = indexInAlphabet(key[iter])
    letter, isUpper = indexInAlphabet(message[i])

    isLetter = not (((ord(message[i]) < 65) or (90 < ord(message[i]) < 97) or (ord(message[i]) > 122)))

    # If current character is a letter, add the new version and increment iter
    if isLetter:
        newMessage += newLetter(letter,index,isUpper)
        iter = (iter+1)%len(key)
    
    else:
        newMessage += message[i]

print("Your message:", message, "\nIs become:", newMessage)
