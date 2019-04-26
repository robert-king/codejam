from math import gcd
from random import shuffle

def monkey():
	print('Warning, monkey patching')
	global input
	it = iter(open('cryptopangrams.in.txt'))
	input = lambda : next(it)

monkey()

T = int(input())

def factor(ab, primes):
	for p in primes:
		if not ab % p:
			return p, ab // p

def charMap(primeSet):
	d = {}
	for c, p in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', sorted(primeSet)):
		d[p] = c
	return d

def resolve(pairs):
	ans = []
	for i, (a, b) in enumerate(pairs):
		if ans:
			if ans[-1] == a:
				ans.append(b)
			else:
				ans.append(a)
		else:
			for j in range(i + 1, len(pairs)):
				x, y = pairs[j]
				if a*b != x*y:
					odd = not (j - i) % 2
					if a == x or a == y:
						if odd:
							ans.append(a)
							ans.append(b)
						else:
							ans.append(b)
							ans.append(a)
					else:
						if odd:
							ans.append(b)
							ans.append(a)
						else:
							ans.append(a)
							ans.append(b)
					break
	return ans

def solve(nums):
	primes = set()
	for ab, bc in zip(nums, nums[1:]):
		# could have aa aa, or ab ab
		if ab != bc:
			# a is not c
			b = gcd(ab, bc)
			primes.add(int(b))
			primes.add(ab//b)
			primes.add(bc//b)
	factors = [factor(ab, primes) for ab in nums]
	ans = resolve(factors)
	d = charMap(primes)
	ans = ''.join(d[p] for p in ans)
	return ans

def run():
	for caseNum in range(1, T + 1):
		N, L = list(map(int, input().split()))
		nums = list(map(int, input().split()))
		ans = solve(nums)
		print('Case #%d: %s' % (caseNum, ans))

def enc(letters, primeMap):
	nums = []
	for a, b in zip(letters, letters[1:]):
		nums.append(primeMap[a] * primeMap[b])
	return nums

def sim():
	primes = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
	primeMap = {}
	for c, p in zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', primes):
		primeMap[c] = p
	letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZAAAAAABBBBBCCCCC')
	while True:
		shuffle(letters)
		nums = enc(letters, primeMap)
		yield nums, ''.join(letters)


def test():
	gen = sim()
	correct = 0
	for _ in range(10**4):
		nums, ans = next(gen)
		if solve(nums) != ans:
			print('got: ', solve(nums))
			print('ans: ', ans)
		else:
			correct += 1
	print('correct: {}'.format(correct))

test()
#run()