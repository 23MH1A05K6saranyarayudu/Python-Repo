def sum_of_divisors(num):
    total = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            total += i
    return total

# Taking inputs for N and M
N = int(input())
M = int(input())

# Checking if N and M are amicable
if sum_of_divisors(N) == M and sum_of_divisors(M) == N:
    print("Amicable")
else:
    print("Not Amicable")