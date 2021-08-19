''' reducer.py'''

import sys

A = {}
B = {}

for line in sys.stdin:
	line = line.strip()
	key,value = line.split('\t')
	v = value.split(',')

	if key == "A":
		A[(int(v[1]),int(v[2]))] = int(v[3])
	elif key == "B":
		B[(int(v[1]),int(v[2]))] = int(v[3])

result = 0
for i in range(0,2):
	for j in range(0,2):
		for k in range(0,2):
			result = result + A[(i,k)]*B[(k,j)]
		print("{0},{1}\t{2}".format(i,j,result))
		result = 0
