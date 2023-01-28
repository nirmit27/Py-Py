# Finding all prime numbers less than an upper limit using the Sieve of Eratosthenes
# Time Complexity : O(nlog(log n))

def soe(n):
    prime = [True for i in range(n+1)]
    # Algo. starts here!
    p = 2
    while p**2 <= n:
        if prime[p] == True:
            for i in range(p*2, n+1, p):
                prime[i] = False  # Sieving occurs here!
        p += 1

    for x in range(2, n+1):
        if prime[x]:
            print(f" {x}", end='')


if __name__ == "__main__":
    n = int(input("\n Enter a number : "))
    print(
        f"\n All the prime numbers LESS than or EQUAL to {n} are as follows : ")
    soe(n)
