import sys
n = int(raw_input().strip())
phonebook={}
while n>=1:
    name =str(raw_input().strip())
    value =str(raw_input().strip())
    if(len(value)<8):
        break
    else:
        phonebook[name]=value
        n=n-1
query=str(raw_input().strip())

if query in phonebook:
    print "%s= %s" %(query,str(phonebook[query]))
else:
    print "Not found"