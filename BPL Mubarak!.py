# Coded by SpiderX

def POWDER(n, z):
    z = int(z)

    for powD in range(1):
        if z > 6:
            over = z // 6
            rem = z - (over * 6)
            if over == 1:
                print(over, "OVER", end=" ")
                if rem == 1:
                    print(rem, "BALL")

                else:
                    print(rem, "BALLS")

            else:
                over = z // 6
                rem = z - (over * 6)
                print(over, "OVERS", end=" ")
                if rem == 0:
                    pass

                elif rem == 1:
                    print(rem, "BALL")

                else:
                    print(rem, "BALLS")

        elif z == 6:
            print(1, "OVER")

        else:
            if z == 0:
                pass

            elif z == 1:
                print(z, "BALL")

            else:
                print(z, "BALLS")


n = int(input())

emp = []
ballm = []

for no in range(n):
    ballm.append('0')

for i in range(n):
    usr = input("")
    emp.append(usr)

for j in range(len(emp)):
    emp[j] = list(emp[j])
    z = 0
    for k in range((len(emp[j]))+1):
            try:
                if k == (len(emp[j])):
                    POWDER(n, z)

                elif emp[j][k] == "W":
                    k += 1

                elif emp[j][k] == "N":
                    k += 1

                elif emp[j][k] == "D":
                    k += 1

                elif emp[j][k] == "O":
                    z += 1
                    ballm[j] = z
                    k += 1

                else:
                    z += 1
                    ballm[j] = z

            except Exception as e:
                print(e)
