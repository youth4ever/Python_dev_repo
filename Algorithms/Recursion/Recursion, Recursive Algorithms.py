# RECURSION ALGORITHMS

# TOWERS OF HANOI, Solved Recursively
print('--------------  TOWERS OF HANOI, Solved Recursively -------------------')
def move_Disk(from_pole, to_pole ):
    print('moving disk from ', from_pole, " to ", to_pole  )


def move_Tower(height, fromPole, toPole, withPole ):
    if height >= 1 :
        move_Tower( height-1, fromPole, withPole, toPole   )
        move_Disk(fromPole,  toPole )
        move_Tower( height-1, withPole, toPole, fromPole  )

move_Tower(3, "A", "B", "C" )




# RECURSION  FUNCTION ALGORITHM MULTIPLICATION
print('\n---------------- Recursive Function Implementation of the multiplication of two numbers : ------------------')

def mult_recursive(a=3, b=9):
    if b == 1:
        return a
    else :                                                              #  The Recursive Step
        return (a + mult_recursive(a, b-1))             #

print(mult_recursive(22,89))

### Compute the value x n for integer n.


print('\n---------------- gcd - The Greatest Commont Factor : ------------------')


def gcd_rec(a, b) :                             #     Made by Bogdan Trif @ 2018-05-21, 1!:00

    if b == 0 :return a

    else :
        return gcd_rec(b, a%b )


print('gcd_rec : \t   ',gcd_rec( 4*3*7*5**2, 3*7*2*5**2) )

### Compute the value x n for integer n.




# RECURSION FUNCTION FACTORIAL :
print('\n---------------- Recursive Function Implementation for Factorial : ---------------')
def factorial(n=10):
    if n == 1:
        return 1
    else:
        return (n*factorial(n-1))

print(factorial(12))

# RECURSION FUNCTION for base**POWER :
print('\n----------------  RECURSION FUNCTION for base**power  :       --------------------')


def recursionPower(base=3, exp=6):
    '''         **©** Made by Bogdan Trif in 2017-02-20
                :base: int or float.    exp: int >= 0
        :returns: int or float, base^exp     '''
    if exp == 1 : return base
    else :
        return (base * recursionPower(base, exp-1))

print(recursionPower(3,5))

print('\n----------------  RECURSION FUNCTION for base**power, MORE Efficient Algorithm  :       --------------------')
# Goodrich, Tamassia, Goldwasser - Book,  Data Structures and Algorithms in Python 2013

def power(x, n):
    if n == 0:
        return 1

    else:
        partial = power(x, n // 2)     # rely on truncated division
        result = partial * partial

        if n % 2 == 1:         # if n odd, include extra factor of x
            result *= x

        return result

power(3,5)


# RECURSION Function for Greatest Common Factor - CMMDC, c.m.m.d.c. - Cel Mai Mic Divizor Comun
print('\n------------   CMMDC - Cel Mai Mare Divizor Comun - The Greatest Common Divisor - GCD ------------------')
def cmmdc(a, b):
    '''    a, b: positive integers     , cmmdc, c.m.m.d.c., Cel Mai Mare Divizor Comun
        returns: a positive integer,  The Greatest Common Divisor of a & b.
    '''
    if b == 0:
       return a
    else:
       return cmmdc(b, a % b)

print(cmmdc(1445, 3005))

########################################
print('\n --------- Fibonacci Recursion Function, HIGHLY INEFFICIENT for Fibonacci without Memoization ----------------')

def Fib_rec(n):     # Fibonacci Recursion
    if ( n == 1 or n == 0 )  :
        return 1
    else :
        return Fib_rec(n-1) + Fib_rec(n-2)

print(Fib_rec(10))      # Already for n > 30 it takes looooong to complete

####################################################

print('\n--------------------    Recursive Solution for Lattice paths in PASCAL TRIANGLE       ------------------------------------------')

def lattice_paths(a, b):
    if a == 0 or b == 0:
        return 1
    else:
        return lattice_paths(a, b - 1) + lattice_paths(a - 1, b)

print(lattice_paths(4,4))

print('\n--------------------    Recursive Multiple For Loop Custom Levels       ------------------------------------------')
def loop_rec(y, number):
    if (number > 1):
        loop_rec( y, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print(' ;')
    else:
        for i in range(y):
            print(i, end=' ')
        print(';')
loop_rec(6,4)

print('---'*15)

def loop_rec(y, number):
    if (number > 1):
        loop_rec( y-1, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print(' ;')
    else:
        for i in range(y):
            print(i, end=' ')
        print('.')
loop_rec(10,10)

print('---'*15)

def loop_rec(y, number):
    if (number > 1):
        loop_rec( y+1, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print(' ;')
    else:
        for i in range(y):
            print(i, end=' ')
        print('.')
loop_rec(1,6)
print('---'*15)

def loop_rec(y, number):
    if (number >= 1):
        loop_rec( y+1, number - 1 )
        for i in range(y):
            print(i, end=' ')
        print('')
    else:
        return

loop_rec(1,5)

####################################################

print('\n--------------------------- RECURSION LOOP FOR WITH LIST ASCENDING, Descending Length ----------------------------')

fives=[5,10,15,20,25,30,35]
def rec_loop_for(i):
    if (i >= 1):
        rec_loop_for(i-1)
        for i in range(len(fives)+1-i):
            print(fives[0:i+1])
        print(';')
    else:
        return

rec_loop_for(len(fives))

print('\n--------------------------- RECURSION LOOP FOR WITH LIST DESCENDING, Descending length ----------------------------')

def rec_loop_for(i):
    if (i >= 1):
        rec_loop_for(i-1)
        for i in range(len(fives)+1-i,0,-1):
            print(fives[0:i])
        print(';')
    else:
        return

rec_loop_for(len(fives))

print('\n--------------------------- RECURSION LOOP FOR WITH LIST DESCENDING, Ascending length ----------------------------')

L=[2,3,5,7]
def rec_loop_for(i):        # *©** Made by Bogdan Trif in 2017-02
    if (i >= 1):
        rec_loop_for(i-1)
        for i in range(i):
            print(L[0:i+1])
        print('---')
    else:
        return

rec_loop_for(len(L))


print('\n---------------- Recursive Mutliplication -------------------')

def multiplication(m , n) :
    if m == 1 : return n
    if n == 1 : return m
    return  n+multiplication(m-1, n)

print(multiplication( 2, 8) )

def power(b , e):
    if e == 1 or b==1 : return b
    return  b * power(b, e-1)

print(power( 3, 5 ))


############ DRAGON HEIGHWAY ##############
print('\n-----------------Dragon Heighway Recursive Algorithm -------------\n')

def dragonpos(n) :
    c = [0,1]
    steps = 1
    length = 1
    while length < n :
        c = [ c[0] + c[1], c[1] - c[0] ]
        length*=2

    if length == n :
        return c

    m = length-n
    c2 = dragonpos(m)
    c2 = [ -c2[1], c2[0] ]

    print(c, length, n, m)

    return [ c[0]+c2[0], c[1]+c2[1] ]


print(dragonpos(5))

print('\n------RECURSION - Sierpinski Fractal, find all the numbers of a Pascal Triangles NON Divisible by 7 ------------')

from math import log

def S(n):
    """ Sum of natural numbers up to and including n. """
    return n*(n+1)//2

def V(z, p):
    """
    Calculates number of non-divisible numbers in the triangle up to and
    including row z*7**p.

    Input:
        p: an exponent of 7
        z: coefficient, 1 < z < 7

    From pattern inspection we know,
        V(1)  = S(1) = 1
        V(7)  = S(7) = 28
        V(49) = 28*V(7) = 28**2
    So we can induce:
        V(7**n) = 28 * V(7**(n-1))
                = 28**n

    Furthermore we know that for any integer constant 1 < z < 7, the expression
        V(z * 7**n) = S(z) * V(7**n)
    is true (can be induced from pattern).
    """
    return S(z)*28**p


def solve(n):
    """
    Strategy

    With V, one can calculate the number non-divisible numbers in the
    triangle easily, for powers of 7 multiplied by a coefficient. Let's call
    such a number c.

    Find the largest c that fits within the questioned size, add V(c) to the
    result, and recurse for the remaining part r = n - c.

    If we hit the bottom and there are no whole triangles left, calculate
    partial values, which are simply S(n).
    """

    # calculate largest 7**p that fits in n.
    p = int(log(n, 7))

    # calculate largest coefficient z such that z*7**p < n
    z = n//7**p
    c = z*7**p

    r = n - c  # the remaining part

    # we don't have whole triangles left, only partial ones.
    if p <= 0:
        return S(n)

    ans = V(z, p)
    ans += solve(r) * (z+1) # The remaining part has one extra triangle.

    return ans


print('\n----------------------------  COMBINATIONS -----------------------------')

def combinations_by_subset(seq, r):
    if r:
        for i in range(r - 1, len(seq)):
            for cl in combinations_by_subset(seq[:i], r - 1):
                print(cl + (seq[i],))
                yield cl + (seq[i],)
    else:
        yield tuple()

print ( list(combinations_by_subset( [1,2,3,4,5], 3)   ) )


print('\n--------------------------NUMBER PARTITION RECURSIVE FUNCTION ---------------------')
def partition(number):
    answer = set()
    answer.add((number, ))
    for x in range(1, number):
        for y in partition(number - x):
            answer.add(tuple(sorted((x, ) + y)))
            #print(answer)
    return answer

print(partition(4))


print('\n---------- Euler 199, Iterative Circle Packing using Descartes Theorem  ---------------------')

# === Sun, 10 Jul 2011, 18:27, MrDrake, New Zeeland
# Great problem once you know Descartes' Theorem!

def descartes(x):
    a, b, c=x
    return a+b+c+2*(a*b+b*c+c*a)**0.5

def f(x, n):
    if not n:
        return 0
    a, b, c = x
    d = descartes(x)
    return 1/d**2 + f ((a, b, d), n-1 ) + f((a, c, d ), n-1)  +  f ((b, c, d ) , n-1 )

k = 3 - 2*3**0.5

n = 10
digits = 8

print ( round(1-(3+3*f((k,1,1),n)+f((1,1,1),n))*k**2, digits) )


################ NESTED LOOPS ################

# While itertools is the way to go, this question is an excellent exercise for practicing generator functions:      !!!!!!!!!!

print('\n ####### NESTED LOOPS , METHOD 3 - RECURSION - ELEGANT, BEAUTIFUL, Must learn it ############  ')

def multirange_rec( L ):
    if len( L ) == 1:
        for i in range( L [0] ):
            yield [i]
    elif len( L ) > 1:
        for i in range( L [-1] ):
            for a in multirange_rec( L [:-1] ) :
                yield a + [i]

def multirange_b(d):
    l = len(d)
    products = [1]
    for k in d:
        products.append(products[-1]*k)
    n = products[-1]
    for i in range(n):
        yield [(i%products[j+1])//products[j] for j in range(l)]

for l in multirange_rec([4,3,2]):
    print(l , end='  ')

print()
for l in multirange_b([4,3,2]):
    print(l, end = '  ')


print('\n--------------------------------  Decimal to binary Recursion ----------------------')

def binary_rec(n, s):    # @ Made by Bogdan Trif @ 2018-05-29
    if n == 1 :
        return str(1) +s
    print(n,'  ', n%2)

    return binary_rec(n//2, str(n%2) +s )

print(binary_rec(248, '') )


######### More advanced Method      #####

def binary_rec2(n) :
    ''' :Explanation: Each time it arrives at the recursive call the previous number is mutiplied by 10
    and add 1 or 0 if n%2 ==0 or 1 . Example : n=11 , just before the last step we have the
    partial result 101 , the last call : 11%2 = 1  and 10 * 101 = 1010 =>
    1 + 1010 = 1011 which is the result for n = 11                      '''
    if n == 1 :
        return 1
    print(n,'  ', n//2, '   ', n%2)

    return (n%2 + 10 * binary_rec2(n//2) )

print(binary_rec2(11))


#################################
print('\n--------   4.3. Calculating the Sum of a List of Numbers  -----------------')
lst = [1, 3, 5, 7, 9]

def sum_rec(lst):   # Made by Bogdan Trif @2018-06-15
    if len(lst) == 1 :
        return lst[0]
    else :
        return lst[0] + sum_rec(lst[1:])

print('sum_rec = ',sum_rec(lst) )



print('\n--------   4.5. Converting an Integer to a String in Any Base  -----------------')
convString = "0123456789abcdef"

def toStr( n , base): # Made by Bogdan Trif @2018-06-15
    if n < base :
        return convString[n]
    else :
        return toStr(n//base, base) + convString[n%base]

print('toStr = ' ,toStr(254, 16) )




print('\n--------     Reverse string with recursion     -----------------')
# Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.

s = 'Bogdan'
def reverse( s ):   # Made by Bogdan Trif @2018-06-15
    if len(s) == 1:
        return s
    else :
        return reverse(s[1:]) + s[0]

print(' reverse = ',reverse(s) )

# Without Recursion

def reverse2( s ):  # Made by Bogdan Trif @2018-06-15
    if len(s) == 1:
        return s
    else :
        return s[::-1]

reverse2('Eugenia')

print('\n--------     Check palindrom recursion     -----------------')
'''Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise. 
Remember that a string is a palindrome if it is spelled the same both forward and backward. 
For example: radar is a palindrome. for bonus points palindromes can also be phrases, 
but you need to remove the spaces and punctuation before checking. for example: madam i’m adam is a palindrome. 

Other fun palindromes include:

kayak 
aibohphobia 
Live not on evil 
Reviled did I live, said I, as evil I did deliver 
Go hang a salami; I’m a lasagna hog. 
Able was I ere I saw Elba 
Kanakanak – a town in Alaska 
Wassamassaw – a town in South Dakota

'''

def palindrom_rec(word):   # Made by Bogdan Trif @2018-06-15

    if len(word) == 0 :
        return True

    elif word[0] == word[-1] :
        return palindrom_rec( word[1:-1] )

    else :
        return False



s = 'abcba'

print('palindrome_rec  :',palindrom_rec(s) )



print('-------------------------    1.7.5   Example: Partitions -----------------------------')

'''

'''

