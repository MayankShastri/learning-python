    def sum_of_primes(n):
        #Calculates the sum of prime numbers till the given limit 
        total=0
        for num in range(2,n+1): #loops from 2 till the given limit
            prime=True #Assumes its a prime number
            for i in range(2,int(num**0.5)+1): #Checks the factors from 2 till the square root of current number "num"
                if num%i==0: #Checks if it's completely divisible by i
                    prime=False
                    break #Breaks if its divisible
            if prime: #checks if it's prime or not
                total+=num #if it is prime it adds it to total
        return total
    n=int(input("Enter your Number: "))
    result=sum_of_primes(n)
    print(f"The sum of primes upto {n} is {result}")