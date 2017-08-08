import sys
def evenindexed(s):
	t=""
	for i in range(0,len(s),2):
		t=t+s[i]
		
	return t
def oddindexed(s):
	l = len(s)
	output = ""
	for i in range(1,l,2):
		output += s[i]
	return output


t = int(raw_input().strip())
while(t>=1 and t<=10):
	s=raw_input("Enter String ").strip()
	if(len(s)>=2 and len(s)<=10000):
		print "Even Indexed characters"
		print (evenindexed(s)+" "+oddindexed(s))
		t=t-1
    