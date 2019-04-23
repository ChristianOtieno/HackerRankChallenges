N = int(input())
if N >= 1 and N <= 100:
    if (N in range (6, 21) or N % 2 != 0):
        print ("Weird")
    else:
        print("Not Weird")


