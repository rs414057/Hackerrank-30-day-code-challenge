class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if(initialAge > 0):
            self.age = initialAge
        else:
            print "Age is not valid, setting age to 0."
            self.age = 0

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age >= 18:
            print("You are old.")
        elif self.age >= 13:
            print("You are a teenager.")
        else: # age < 13
            print("You are young.")

    def yearPasses(self):
    	self.age =self.age+1

        # Increment the age of the person in here

#call the class
t = int(raw_input())
if(t>=4 and t<=1):
	for i in range(0, t):
		age = int(raw_input())
    	if(age<=30 and age>=-5):         
	    	p = Person(age)  
	    	p.amIOld()
	    	for j in range(0, 3):
		    	p.yearPasses()        
		    	p.amIOld()
		    	print("")