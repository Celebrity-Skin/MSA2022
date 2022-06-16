#INPUT
#Declare variables for known values
hourly_labor_cost = 62.25
unit_of_wall_area = 350
hours_labor_per_unit = 6
#prompt the user to enter the amount of wall to paint
#Convert to a float
#If error ask user to reenter input/ inpurt should be greater than 0
run_again = True
while (run_again):
    try:
        wall_area = float(input("What is the area of wall in sq/ft: "))
        if(wall_area <+ 0 ):
            continue
    except:
        print("ERROR: Wall area must be a number.\n")
    else:
        run_again = False
#prompt user to enter cost of paint per gallon
#Convert to a float
paint_price = float(input("What is the price of paint per gallon: "))


#PROCESS
#Calculate to hours of labor
#Calculate the cost of labor
#Calculate the amount of paint
#Calculate the cost of the paint
#Calculate total cost of the job

#OUTPUT
#Print hours of labor, cost of labor, amount of paint, 
#cost of paint, total job cost
