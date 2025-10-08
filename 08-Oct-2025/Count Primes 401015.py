# Problem: Count Primes - https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:
        # def isPrime(num):
        #     if num < 2:
        #         return False
        #     val = int(sqrt(num))
        #     for i in range(2, val + 1):
        #         if num % i == 0:
        #             return False
        #     return True
        # cnt =0 
        # for i in range(n):
        #     if isPrime(i):
        #         cnt += 1
        # return cnt

        # is_prime = [True for _ in range(n + 1)]
        if n <= 1:
            return 0
        # is_prime[0] = False
        # is_prime[1] = False
        # i = 2
        # cnt  = 0
        # while i <= n:
        #     if is_prime[i]:
        #         cnt += 1
        #         j = 2 * i
        #     while j <= n:
        #         is_prime[j] = False
        #         j += i
        #     i += 1
        # return cnt


        def prime_sieve(n: int) -> list[bool]:
            is_prime: list[bool] = [True for _ in range(n )]
            is_prime[0] = is_prime[1] = False
            i = 2
            while i < n:
                if is_prime[i]:
                    j = 2 * i
                while j < n:
                    is_prime[j] = False
                    j += i
                i += 1
            return is_prime
        res = Counter(prime_sieve(n))
        return res[True]
