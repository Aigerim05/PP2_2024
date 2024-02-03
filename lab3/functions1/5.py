'''
Write a function that accepts string from user and print 
all permutations of that string.
'''

word = input()

def find_permutations(s):
	if len(s) == 1:
		return [s]
	else:
		perms = []
		for i, c in enumerate(s):
			for perm in find_permutations(s[:i] + s[i+1:]):
				perms.append(c + perm)
		return perms

print(find_permutations(word))

