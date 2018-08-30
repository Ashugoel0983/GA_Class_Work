'''

Assignment : Project 1
Name: Ashu Goel

batch : Data Science

'''


##Summation of Primes
def sum_primes():
    prime_Sum = 5
    for i in range(5,2001):
        if i%2 != 0 and i%3 !=0 :
            prime_Sum = prime_Sum + i 
    return print("The Sum of all Prime number till 2000 is : ", prime_Sum)

sum_primes()