multiplicator = {"DECODE": -1, "ENCODE": 1}

def index_in_alphabet(letter):
    return (ord(letter.lower()) - 97, letter.isupper())

def new_letter(letter, index, is_upper):
    base = 65 if is_upper else 97
    return chr((letter * multiplicator[choice] + index) % 26 + base)

def valid_input(prompt):
    while True:
        text = input(prompt)
        if text.isalpha():
            return text
        print("Le texte ne doit contenir que des lettres !")

# Choix entre Encode et Decode
choice = input("Do you want: Decode | Encode: ").upper()
while choice not in multiplicator:
    choice = input("Veuillez rentrer une réponse valide (Decode | Encode): ").upper()

# Demande du message et de la clé
message = valid_input(f"Type your message to {choice.lower()}: ")
key = valid_input(f"Type the key used to {choice.lower()} this message: ")

# Traitement du message
new_message = ""
for i, char in enumerate(message):
    if char.isalpha():
        letter, is_upper = index_in_alphabet(char)
        index = index_in_alphabet(key[i % len(key)])[0]
        new_message += new_letter(letter, index, is_upper)
    else:
        new_message += char

print(f"Your message: {message}\nHas become: {new_message}")
