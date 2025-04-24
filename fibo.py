def recursive_nth_fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    n = int(input("Pocet clenu Fibonacciho posloupnosti: "))
    sek = []
    for num in range(n):
        sek.append(recursive_nth_fibo(num))

    print(sek)


if __name__ == "__main__":
    main()
