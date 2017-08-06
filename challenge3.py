def get_total_cost_of_meal():
	meal_cost = float(raw_input())
	tip_percent = int(raw_input())
	tax_percent = int(raw_input())
	tip=meal_cost*(float(tip_percent)/100)
	tax=meal_cost*(float(tax_percent)/100)
	total_cost=meal_cost+tip+tax
	total_cost = int(round(total_cost))
	return str(total_cost)
    
    
    # tax percentage
    

    # Write your calculation code here
    
    
    # cast the result of the rounding operation to an int and save it as total_cost 
    
    
    

# Print your result
print("The total meal cost is " + get_total_cost_of_meal() + " dollars.")