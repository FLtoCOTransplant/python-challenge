# dependents
import os
import csv

# Path to collect data from the Resources folder
budget_csv=os.path.join("Resources","budget_data.csv")

# Define the variables for calcs
t_months = 0
t_rev = 0
t_rev_delta = 0
h_rev = 0
l_rev = 0

# Open and read csv
with open(budget_csv) as csv_file:
    budget_csv = csv.reader(csv_file, delimiter=",")

#Read the header and skip first row
    budget_csv = next(csv_file)
    #print(f"Header: {csv_header}")

    #start collecting data denoting each row as a row
    for row in budget_csv:

        #total months
        t_months = t_months + 1

        #total revenue
        t_rev = t_rev + int(row[1])

#Calculate the average monthly revenue
#ave_monthly_rev = t_rev/t_months

# Provide the board with the final results 
results = (
    f"Financial Overview\n"
    f"----------------------------\n"
    f"Total # of Months : {t_months}\n"
    f"Total Revenue for {t_months} Months: ${t_rev}\n"
    f"Average Monthly Revenue : $\n"



)    

#Show output in terminal
print(results)
