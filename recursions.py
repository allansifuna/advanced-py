"""
Sample practice code on recursions for data structures and algorithms (greedy algorithm,Brute-force algorithm)

@author Allan Sifuna

23-2-2020
"""
import time
def decorator(f):
    def wrapper(*args,**kwargs):
        start=time.time()
        v=f(*args,**kwargs)
        stop=time.time()
        print(f"i ran in {stop-start}seconds")
        return v
    return wrapper

def multiply(a,b):
    ''' Multiplication of two numbers using recursion ie a * b'''
    if b==1:
        return a
    else:
        return a+multiply(a,b-1)

multi=multiply(4,5)

# print(multi)

@decorator
def factorial(n):
    ''' Get factorial of a number using recursion ie. n!'''

    if n==1:
        return n
    else:
        return n* factorial(n-1)

# fact=factorial(200)

# print(fact)



@decorator
def fact_memo(n,memo={}):
    #Recursion implementing memoisation
    ''' Get factorial of a number using recursion ie. n!'''

    if n==1:
        return n
    else:
        try:
            return memo[n]
        except KeyError:
            v=n* fact_memo(n-1)
            memo[n]=v
            return v

# fact=fact_memo(200)

# print(fact)

def palindrome(n):
    '''Check whether a string or any iretable is palindrome'''
    if len(n)<=1:
        return True
    return n[0]==n[-1] and palindrome(n[1:-1])

pal=palindrome('abcdefedcba')
# print(pal)

def fine_list(n):
    '''Make a fine list from a series of nested lists using recursion'''
    if len(n)==1:
        return n
    else:
        l=[n[0]]
        return l+(fine_list(n[1]))

unfine_list=[1,[2,[3,[4,[5,[6,[7,[8]]]]]]]]
fine=fine_list(unfine_list)
# print(fine)

def define_list(n):
    '''Make a nested list from a fine lists using recursion'''
    if len(n)==1:
        return [n]
    else:
        return [[n[0]]+(define_list(n[1:]))]

f_list=[i for i in range(1,10)]
unfine_list=define_list(f_list)[0]
# print(unfine_list)
# print(fine_list(unfine_list))

def reverse_string(n):
    if len(n)==0:
        return n
    else:
        return n[-1]+reverse_string(n[:-1])

rev=reverse_string('reversed string')
# print(rev)


