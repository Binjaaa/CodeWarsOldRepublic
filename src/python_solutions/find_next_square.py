import math

def find_next_square(sq):
    if sq > 0 and sq % (math.sqrt(sq)) == 0:
        return (math.sqrt(sq)+1)**2
    else:
        return -1

print(find_next_square(-1))
print(find_next_square(0))
print(find_next_square(1))
print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))

# Examples:
#
# findNextSquare(121) --> returns 144
# findNextSquare(625) --> returns 676
# findNextSquare(114) --> returns -1 since 114 is not a perfect
# https://www.codewars.com/kata/find-the-next-perfect-square