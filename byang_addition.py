# Coded by SpiderX

x, y = map(int, input().split())


def Byans_Carrier_logic(x, y):
    # listing First
    x_list = list(str(x))
    y_list = list(str(y))
    # print(x_list)

    if len(x_list) > len(y_list):
        i = len(y_list)

    else:
        i = len(x_list)

    # swaping x_list
    x_list = x_list[::-1]
    y_list = y_list[::-1]

    for j in range(0, i):
        if int(x_list[j]) + int(y_list[j]) >= 10:
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    Byans_Carrier_logic(x, y)
