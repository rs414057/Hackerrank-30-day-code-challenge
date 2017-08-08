n = int(raw_input().strip())
if(n>=2 and n<=20):
    for i in range(1,11):
        print "%d x %d = %d" %(n,i,(n*i))
