
def monkey():
	print('Warning, monkey patching')
	global input
	it = iter(open('alien_rhyme.in.txt'))
	input = lambda : next(it)

monkey()
for caseNum in range(1, int(input()) + 1):
	N = int(input())
	words = sorted(input().strip()[::-1] for _ in range(N))
	taken = set()
	for prefix_length in range(50, 0, -1):
		for a, b in list(zip(words, words[1:])):
			if a[:prefix_length] == b[:prefix_length]:
				if a[:prefix_length] not in taken:
					taken.add(a[:prefix_length])
					words.remove(a)
					words.remove(b)
	print('Case #%d: %d' % (caseNum, N - len(words)))
