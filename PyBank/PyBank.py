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
h_rev = -100000000
l_rev = 100000000
cur_month_rev = 0

#File output
analysis = os.path.join("Results_Bank_Revenue_Analysis.txt")

# Open and read csv
with open(budget_csv) as csv_file:
    budget_csv = csv.reader(csv_file, delimiter=",")

#Read the header and skip first row
    header = next(csv_file)

    #start collecting data denoting each row
    for row in budget_csv:

        #total months
        t_months+= 1

        #total revenue
        cur_month_rev = int(row[1])
        t_rev += cur_month_rev

        #Calculate greatest increase in revenue
        if t_months >1:
            rev_delta = int(row[1]) - prev_rev
            if rev_delta > h_rev:
                h_rev = rev_delta
                h_rev_d = (row[0])
        
        #Calculate greatest decrease in revenue
        if t_months >1:
            rev_delta = int(row[1]) - prev_rev
            if rev_delta < l_rev:
                l_rev = rev_delta
                l_rev_d = (row[0])

#Calculate the average monthly revenue
ave_monthly_rev = t_rev/t_months

# Provide the board with the final results 
results = (
    f"     Financial Overview\n"
    f"----------------------------\n"
    f"Total # of Months : {t_months}\n"
    f"Total Revenue for {t_months} Months: ${t_rev}\n"
    f"Average Monthly Revenue : ${ave_monthly_rev}\n"
    f"Month with Greatest Increase in Revenue: {h_rev_d} & {h_rev}\n"
    f"Month with Greatest Decrease in Revenue: {l_rev_d} & {l_rev}\n"
)    

#Show output in terminal
print(results)

#Output results to file
with open(analysis, "w") as txt_file:
    txt_file.write(results)