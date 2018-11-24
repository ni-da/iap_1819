a = 347


def is_prime(a):
    if a == 2:
        return True
    if a < 2:
        return False
    else:
        for i in range(2, a):
            if a % i == 0:
                return False
    return True


def all_primes_upto(n):
    for i in range(n):
        if is_prime(i):
            print(i)


def factorize(x):
    res = x
    while res != 1:
        counter = 0
        while True:
            if is_prime(counter):
                if res % counter == 0:
                    res = res / counter
                    print(counter)
                    break
            counter += 1


# print(is_prime(a))
# all_primes_upto(25)

factorize(3003)
