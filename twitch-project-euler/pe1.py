def primes(upto):
	dp = [True] * (upto + 1)
	for i in range(2, upto):
		if dp[i]:
			yield i
			for not_prime in range(i*i, upto, i):
				dp[not_prime] = False


sqrt = int(600851475143 ** 0.5) + 1
largest = None
for p in primes(sqrt):
	if (600851475143 % p) == 0:
		largest = p
print(largest)