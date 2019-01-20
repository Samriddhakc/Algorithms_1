def recur(n):
    if(n==0):
        return 1
    else:
        recur(n-1)
        print("exec")


def main():
    recur(3)
main()
