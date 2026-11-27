# Exercise 11: Primes (one function using another)
# Write is_prime(n) that returns True or False. Then write primes_up_to(n) that uses
# is_prime to return a list of all primes from 2 to n.
# Test: is_prime(1) → False · is_prime(29) → True · primes_up_to(20) → [2, 3, 5, 7, 11, 13, 17, 19]


def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False

    return True



def primes_up_to(n):
    prime_num=[]
    for i in range (2,n):
        if is_prime(i):
            prime_num.append(i)


    return prime_num


            

prime_or_not = is_prime(4)
print(prime_or_not)
print(is_prime(1))
print(is_prime(7))
print(primes_up_to(20))


