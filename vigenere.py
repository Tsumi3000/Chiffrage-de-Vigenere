
from vigenere_decode import decode
from vigenere_encode import encode

choice = input("Do you want: Decode | Encode: ").upper()
while choice != "DECODE" and choice != "ENCODE":
    print("Veuillez rentrer une réponse valide !")
    choice = input("Do you want: Decode | Encode: ").upper()

if choice == "DECODE": decode()
if choice == "ENCODE": encode()
