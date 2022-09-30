#add multiple error in one line
#raise keyword

"""

try:
    n1 = int(input("Enter 1st number : "))
    n2 = int(input("Enter 2nd number : "))
    z = n1 / n2
    print(z)

except (ValueError, ZeroDivisionError, IndexError):
    print("You sure what you just typed ?")

finally:
    print("")

"""


def voter(age):
    if age < 18:
        raise ValueError("")
    else:
        print("You are allowed to vote")


try:
    n = int(input("Enter your age : "))
    z = voter(n)
    print(z)
except ValueError:
    print("Wait a little")
