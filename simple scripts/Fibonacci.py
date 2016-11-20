# Fibonacci series
import time

def main():

	print('\n--------------Fibonacci Iterative while Loop, faster than recursion --------------------')

	t1  = time.time()

	print(Fibon(100))

	t2  = time.time()
	print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')

	print('\n--------------Fibonacci Recursive, slower than iteration without dictionary--------------------')

	t1  = time.time()
	import sys
	sys.setrecursionlimit(1500)

	d = {1:1, 2:2}
	print(fib(100, d))

	t2  = time.time()
	print('\n', ' Completed in  in :', round((t2-t1)*1000,4), 'ms\n')






def Fibon(n):
	#	Fibonacci with iteration, while loop
	counter = 0
	a, b = 0, 1
	while counter  < n :
		#print (b, end=" ")
		a  , b = b, a + b
		counter += 1
	return b

print('\n--------------  Recursion function Fibonacci with memoization; Memoization keep tracks of already calculated values --------------')

d={1:1, 2:1}
def fib(n, d):
	#	Recursion function Fibonacci with memoization; Memoization keep tracks of already calculated values

	if n in d:				#	First look up in the dictionary
		return d[n]
	else:
		ans= fib(n-1, d) + fib(n-2, d)
		d[n] = ans
		#print(d)			# Here the new fibonacci value is added to the dictionary
		return ans

print('Recursive  Fibonacci with Memoization : ',fib(12, d))


def fibo(n):
	#	Recursion function Fibonacci with memoization; Memoization keep tracks of already calculated values
	d={1:1, 2:1}
	if n in d:				#	First look up in the dictionary
		return d[n]
	else:
		ans = fibo(n-1) + fibo(n-2)
		d[n] = ans
		#print(d)			# Here the new fibonacci value is added to the dictionary
		return ans

print('\nRecursive  Fibonacci with Memoization : ',fibo(3))
###################################################

def Fibonacci(n):
	iter = 0 		# Number of terms
	#	ORIGINAL Fibonacci with iteration, while loop
	a, b = 0, 1
	while iter < n:
		iter +=1
		print (b, end=" ")
		a  , b = b, a + b



if __name__ == "__main__": main()

Fibonacci(40)