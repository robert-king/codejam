from sys import stdout
from sys import stderr
from sys import exit

def p(s):
	print(s)
	stdout.flush()

def r():
	return input().strip()

def ints():
	return list(map(int, r().split()))

DP = {}
MODS = [18, 17, 16, 15, 14, 13, 12]

def build_dp():
	for i in range(1, 10**6+1):
		DP[tuple(i % m for m in MODS)] = i

def test_case():
	hash = []
	for mod in MODS:
		p(' '.join(map(str, [mod]*18)))
		hash.append(sum(ints()) % mod)
	ans = DP[tuple(hash)]
	p(ans)
	if ints()[0] == -1:
		exit()


def run():
	build_dp()
	T, N, M = ints()
	for _ in range(T):
		test_case()
	exit()

run()
