# dependents
import os
import csv

# Path to collect data from the Resources folder
budget_csv=os.path.join("Resources","budget_data.csv")

# Define the variables for calcs
t_months = 0
t_rev = 0
rev_delta = 0
prev_rev = 0
h_rev = 0
l_rev = 0
cur_month_rev = 0

#File output
analysis = os.path.join("Resources", "Results of Bank Revenue Analysis.txt")

# Open and read csv
with open(budget_csv) as csv_file:
    budget_csv = csv.reader(csv_file, delimiter=",")

#Read the header and skip first row
    budget_csv = next(csv_file)
    #print(f"Header: {budget_csv}")

    #start collecting data denoting each row
    for row in budget_csv:

        #total months
        t_months = t_months + 1

        #total revenue
        cur_month_rev = int(row[1])
        #t_rev = t_rev = cur_month_rev
        t_rev += cur_month_rev

        #Calculate greatest increase in revenue
        #rev_delta = int(row["Profit/losses"]) - prev_rev
        #prev_rev =  int(row["Profit/losses"])
        

#Calculate the average monthly revenue
#ave_monthly_rev = t_rev/t_months

# Provide the board with the final results 
results = (
    f"Financial Overview\n"
    f"----------------------------\n"
    f"Total # of Months : {t_months}\n"
    f"Total Revenue for {t_months} Months: ${t_rev}\n"
    f"Average Monthly Revenue : $\n"
    f"Month with Greatest Increase in Revenue: \n"
    f"Month with Greatest Decrease in Revenue: \n"
)    

#Show output in terminal
print(results)

#Output results to file
with open(analysis, "w") as txt_file:
    txt_file.write(results)