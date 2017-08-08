import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
l=len(arr)
s=""
for i in range(l-1,-1,-1):
	s=s+str(arr[i])+" "
print s