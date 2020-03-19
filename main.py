import sys

if len(sys.argv) <= 2:
	print('false')
else:
	s1 = sys.argv[1]
	s2 = sys.argv[2]
	if list(map(s1.find, s1)) == list(map(s2.find, s2)):
		print('true')
	else:
		print('false')

