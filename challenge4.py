#!/bin/python



while 1:
    N = int(raw_input())
    if(N<1 and N>100):
        break
    else:
        if(N%2!=0):
            print "Weird"
        if(N%2==0 and (N>=2 and N<=5)):
            print "Not Weird"
        if(N%2==0 and (N>=6 and N<=20)):
            print "Weird"
        if(N%2==0 and (N>20)):
            print "Not Weird"
        