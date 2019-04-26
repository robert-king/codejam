# from itertools import combinations
# mods = list(reversed(range(11, 19)))
# # mods.remove(4)
# # mods.remove(8)
# # mods.remove(16)
# # mods.remove(9)
# count = 0
# for combo in combinations(mods, r=7):
# 	s = set()
# 	mods = list(combo)
# 	ok = True
# 	for M in range(2,10**6+1):
# 		hash = tuple(M % m for m in mods)
# 		if hash in s:
# 			ok = False
# 			break
# 		s.add(hash)
# 	if ok:
# 		print(mods)

mods = [18, 17, 16, 15, 14, 13, 12]
dp = {}
for i in range(2, 10**6+1):
	hash = tuple(i % m for m in mods)
	dp[hash] = i

for i in range(2, 10**6+1):
	hash = tuple(i % m for m in mods)
	assert(dp[hash] == i)