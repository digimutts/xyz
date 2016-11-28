from operator import itemgetter
import math
def countInversions(itemlist, n):
    if n == 1:
        return 0
    elif n == 2:
        if itemlist[0] > itemlist[1]:
            return 1

def eras(n):
    # enumerate all odd primes
    primes = [True] * (n +1)
    # print(primes)
    i = 2
    while i <= math.sqrt(n):
        if primes[i]:
            j = 2
            while i*j <= n:
                primes[i*j] = False
                j += 1
        i += 1

    # print('Done getting primes')
    # print(primes)
    # for i in range(len(primes)):
    #     if primes[i]:
    #         print(i)


    # Try the trivial case first, e.g. 4: 2, 2
    # if primes[n/2]:
    #     return [n/2, n/2]
    # if n == 4:
    #     return [2, 2]
    # only odd primes
    # move towards middle from both ends of list
    start = 2
    end = n
    while start <= n:
        if primes[start] and primes[end]:
            if (start + end) == n:
                return [start, end]
            elif (start + end) < n:
                start += 1
            else:
                end -= 1
        if not primes[start]:
            start += 1
        if not primes[end]:
            end -= 1
    print('Disproved Goldbachs! uh oh')


def main():
    pp = eras(4)
    print(pp)
main()