
#runtime error # code error #user input error

#try # except #finally

try:
    n = [0, 20, 30, 40, 50]
    z = n[4] // n[2]
    print(z)
    print("Done")

except ZeroDivisionError:
    print("Dividing by zero is not possible")

# except IndexError:
#     print("Index Error")

# print("Error Bypassed")

finally:
    print("Maybe you made a mistake")
