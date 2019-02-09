# © o(^_^)o  Solved by Bogdan Trif  @
#The  Euler Project  https://projecteuler.net
'''
                Lenticular holes            -               Problem 295


We call the convex area enclosed by two circles a lenticular hole if:

The centres of both circles are on lattice points.
The two circles intersect at two distinct lattice points.
The interior of the convex area enclosed by both circles does not contain any lattice points.

Consider the circles:

C0:     x^2+y^2=25
C1:     (x+4)^2+(y-4)^2=1
C2:     (x-12)^2+(y-4)^2=65

The circles C0, C1 and C2 are drawn in the picture below.

C0 and C1 form a lenticular hole, as well as C0 and C2.

We call an ordered pair of positive real numbers (r1, r2) a lenticular pair if there exist two circles
with radii r1 and r2 that form a lenticular hole.

We can verify that (1, 5) and (5, √65) are the lenticular pairs of the example above.

Let L(N) be the number of distinct lenticular pairs (r1, r2) for which 0 < r1 ≤ r2 ≤ N.
We can verify that L(10) = 30 and L(100) = 3442.

Find L(100 000).


'''
import time, zzz
from math import sqrt, floor, ceil

'''
https://en.wikipedia.org/wiki/Pythagorean_triple

'''



print('\n--------------------------TESTS------------------------------')
t1  = time.time()


def brute_force_first( L ) :
    lim = floor( L/2**(1/2) )
    for a in range(0, lim) :
        b = a+1
        print('a= ', a, '    b=', b, '     ' ,  (a*a+b*b)**(1/2) )
        for c in range(0, L ) :
            for d in range(c+1, L ) :
                print('c= ', c , '   d= ', d)





        # b_lim = ceil( (L*L - a*a)**(1/2) )
        # for b in range(a+1, b_lim ) :




# brute_force_first(10**1 )

lim = 10**1
D = dict()

for a in range(1, lim+1):
    b_lim = ceil( (lim*lim - a*a)**(1/2) )
    for b in range(a+1, lim+1 ) :
        if (a*a+b*b )**(1/2) <= lim :

            if a*a+b*b not in D :
                D[a*a+b*b] = [(a, b) ]
            else : D[a*a+b*b].append( (a, b)  )

for k,v in D.items():
    if sqrt(k) %1 ==0 or len(v) > 1  :
        print(k,': ' ,v ,'       ', sqrt(k) )


t2  = time.time()
print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')

print('\n================  My FIRST SOLUTION,   ===============\n')
# t1  = time.time()





# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')


# print('\n===============OTHER SOLUTIONS FROM THE EULER FORUM ==============')
# print('\n--------------------------SOLUTION 1,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 2,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 3,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 4,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 5,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 6,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 7,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 8,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 9,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 10,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 11,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')
#
#
# print('\n--------------------------SOLUTION 12,   --------------------------')
# t1  = time.time()
#
#
#
# t2  = time.time()
# print('\n# Completed in :', round((t2-t1)*1000,2), 'ms\n\n')




