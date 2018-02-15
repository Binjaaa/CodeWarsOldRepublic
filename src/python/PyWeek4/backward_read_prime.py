from src.python.codewars_test import test


def backwardsPrime(start, end):
    return [i for i in xrange(start, end + 1)
            if isPrime(i) and isPrime(int(''.join(reversed(str(i))))) and i != int(''.join(reversed(str(i))))]


def isPrime(x):
    return all([x % i != 0 for i in xrange(2, int(x ** 0.5) + 1)])



if __name__ == '__main__':

    a = [9923, 9931, 9941, 9967]
    test.assert_equals(backwardsPrime(9900, 10000), a)
    a = [7027, 7043, 7057]
    test.assert_equals(backwardsPrime(7026, 7058), a)
    a = [70001, 70009, 70061, 70079, 70121, 70141, 70163, 70241]
    test.assert_equals(backwardsPrime(70000, 70242), a)
    a = [109537, 109579, 109583, 109609, 109663]
    test.assert_equals(backwardsPrime(109536, 109664), a)
