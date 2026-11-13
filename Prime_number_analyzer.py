import math

def isprime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def finnoofprime(n):
    cnt = 0

    for i in range(n):
        if isprime(i):
            cnt += 1

    return cnt


def findthemaximumprime(n):
    arr = []

    for i in range(n):
        if isprime(i):
            arr.append(i)

    if len(arr) == 0:
        return None

    return max(arr)


def allprimes(n) -> list:
    arr = []

    for i in range(n):
        if isprime(i):
            arr.append(i)

    return sorted(arr)


# Main program
print("Give your input number:")
n = int(input())

if n < 0:
    print("Give a valid input")
else:
    print("Number of primes:", finnoofprime(n))
    print("Maximum prime:", findthemaximumprime(n))
    print("All primes:", allprimes(n))
