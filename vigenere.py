
from vigenere_decode import decode
from vigenere_encode import encode

choice = input("Voulez vous: Decoder | Encoder: ")
while choice != "Decoder" and choice != "Encoder":
    print("Veuillez rentrer une réponse valide !")
    choice = input("Voulez vous: Decoder | Encoder: ")

if choice == "Decoder": decode()
if choice == "Encoder": encode()