def monkey():
	print('Warning, monkey patching')
	global input
	it = iter(open('pylons.in.txt'))
	input = lambda : next(it)

monkey()

from random import choice

def valid(loc, new_loc):
	r1, c1 = loc
	r2, c2 = new_loc
	if r1 == r2 or c1 == c2:
		#same row or column
		return False
	if (r1 - c1) == (r2 - c2):
		# diag 1
		return False
	if (r1 + c1) == (r2 + c2):
		# diag 2
		return False
	return True

def random_attempt(R, C):
	N = R * C
	grid = [(i, j) for i in range(R) for j in range(C)]
	assert(len(grid) == N)
	loc = choice(grid)
	grid.remove(loc)
	invalid = set()
	history = [loc]
	while True:
		new_loc = choice(grid)
		if valid(loc, new_loc):
			#print(loc, new_loc)
			grid.remove(new_loc)
			loc = new_loc
			history.append(loc)
			if len(grid) == 0:
				#print(history)
				return history
			invalid = set()
		else:
			invalid.add(new_loc)

		if len(invalid) == len(grid):
			#print('returning false', invalid, grid)
			return False

def solve_random(R, C):
	impossible = [
		(2, 2),
		(2, 3),
		(3, 2),
		(2, 4),
		(4, 2),
		(3, 3),
	]
	# possible = [
	# 	(3, 4),
	# 	(4, 3),
	# 	(4, 4),
	# ]
	if (R, C) in impossible:
		return False
	# if (R, C) in possible:
	# 	return True
	N = R * C
	for i in range(100000):
		history = random_attempt(R, C)
		if history:
			return history
	return False # cloud be false positive

from random import shuffle
def f(spots, moves, r, c):
	shuffle(spots)
	if len(moves) == r * c:
		return True
	for idx, (i, j) in enumerate(spots):
		if (not moves) or valid(moves[-1], (i, j)):
			moves.append((i, j))
			spots.pop(idx)
			possible = f(spots[:], moves, r, c)
			if possible:
				return possible
			spots.insert(idx, (i, j))
			moves.pop()
	return False

def solve_backtrack(r, c):
	spots = [(i, j) for i in range(r) for j in range(c)]
	moves = []
	possible = f(spots, moves, r, c)
	#print(moves, possible)
	return moves if possible else False

# for r in range(2, 20):
# 	for c in range(2, 20):
# 		print(r, c, not not solve_backtrack(r, c))



for caseNum in range(1, int(input()) + 1):
	R, C = map(int, input().split())
	history = solve_backtrack(R, C)
	ans = 'POSSIBLE' if history else 'IMPOSSIBLE'
	print('Case #{}: {}'.format(caseNum, ans))
	if history:
		for i, j in history:
			print(i+1,j+1)