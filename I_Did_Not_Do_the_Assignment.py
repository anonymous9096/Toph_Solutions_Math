n = int(input())
if 1 < n <= 1000:
    for k in range(2, n+1):
        if k == n:
            print("NO PUNISHMENT")

        elif (n % k) == 0:
            for n1 in range(n):
                print("I DID NOT DO THE ASSIGNMENT.")
            break

        else:
            k += 1
