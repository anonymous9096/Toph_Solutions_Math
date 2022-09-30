#better password

user_input = input("").lower()
z1 = user_input.replace("s", "$")
z2 = z1
z2 = z1.replace("i", "!")
z3 = z2
z3 = z2.replace("o", "()")

z4 = z3
z4 = z3[0].upper()
z5 = z4 + z3[1:]
print(z5, end="")
print(".")
