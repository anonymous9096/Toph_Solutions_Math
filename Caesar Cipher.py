import string

z = int(input(""))
text = input("")
shift = -z

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = text.translate(table)
print(encrypted)
