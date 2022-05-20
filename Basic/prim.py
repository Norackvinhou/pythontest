import math
n =int(input("give number above 1 :"))
primes = []
count=0
def isPrime(num):
    root=int(math.sqrt(num))
    for i in range(2, root + 1):
 	    if num%i == 0:
 		    return False
    else:
        return True


for i in range(2, n + 1):
    if(isPrime(i)):
        primes.append(i)
        count+=1

print("there are ",count,"prime number")
print(primes)