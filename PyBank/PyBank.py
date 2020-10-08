# dependents
import os
import csv

# Path to collect data from the Resources folder
budget_csv=os.path.join("Resources","budget_data.csv")

# Define the variables for calcs
t_months = 0
t_rev = 0
t_rev_delta = 0

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

#Read the header and skip first row
    csv_reader = next(csv_file)
    #print(f"Header: {csv_header}")

    #start collecting data
    for row in csv_reader:

        #total months
        t_months = t_months = 1
        
#Calculate the average monthly revenue
    
    
    
