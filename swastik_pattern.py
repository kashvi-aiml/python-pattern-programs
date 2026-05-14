n = int(input("Enter an odd number: "))

def swastik(n):
    mid = n // 2

    for i in range(n):
        for j in range(n):

            if (
                i == mid or
                j == mid or
                (i == 0 and j >= mid) or
                (j == 0 and i <= mid) or
                (i == n - 1 and j <= mid) or
                (j == n - 1 and i >= mid)
            ):
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()

swastik(n)