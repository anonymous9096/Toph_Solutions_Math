# Coded by SpiderX

usr = int(float(input()))
# print(usr)
if 0 <= usr <= 100:
    print("[", "+" * (usr // 10), "." * (10 - (usr // 10)), "]", sep="", end=" ")
    print(round(usr), "%", sep="")
