from __future__ import print_function
from src.python.codewars_test import test
import datetime

def backwardsPrime(start, end):

    def primes_sieve(p_start, p_end):
        p_endn = p_end + 1
        not_prime = set()
        primes = []

        for i in range(p_start, p_endn):
            if i in not_prime:
                continue
            for f in range(i * 2, p_endn, i):
                not_prime.add(f)
            primes.append(i)
        return primes

    start_len = len(str(start))
    p_start = 2
    p_end = int("9"+"9"*(start_len-1))
    print('+ p_end: {}'.format(p_end))

    is_prime_list = primes_sieve(p_start, 975902)

    result = []
    result_reverse = []
    for i in xrange(start, end):
        reversed_num = int(''.join(reversed(str(i))))
        if i in is_prime_list:
            if i != reversed_num:
                if reversed_num in is_prime_list:
                    if end > i > start:
                        result.append(i)
                        result_reverse.append(int(''.join(reversed(str(i)))))
    print('+ result: {}'.format(result))
    return result


if __name__ == '__main__':
    time_start = datetime.datetime.now()

    a = [9923, 9931, 9941, 9967]
    test.assert_equals(backwardsPrime(9900, 10000), a)
    a = [7027, 7043, 7057]
    test.assert_equals(backwardsPrime(7026, 7058), a)
    a = [70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]
    test.assert_equals(backwardsPrime(70000, 70242), a)
    a = [109537, 109579, 109583, 109609, 109663]
    test.assert_equals(backwardsPrime(109536, 109664), a)
    time_end = datetime.datetime.now()
