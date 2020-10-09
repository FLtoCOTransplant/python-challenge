# dependents
import os
import csv

# Path to collect data from the Resources folder
vote_csv=os.path.join("Resources","election_data.csv")

# Define variables
t_votes = 0
vote_count = 0
candidate = []
w_candidate = ""

#File output
analysis = os.path.join("Resources", "Voting Results for Small Town, USA.txt")

# Open and read csv
with open(vote_csv) as csv_file:
    vote_csv = csv.reader(csv_file, delimiter=",")

#Read the header and skip first row
    vote_csv = next(csv_file)
    #print(f"Header: {budget_csv}")   
    
    #start collecting data denoting each row
    for row in vote_csv:  

        #determine total votes
        t_votes += 1

        #What is the candidate name

# Provide the public with the results of the election 
results = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total # of votes cast : {t_votes}\n"
    f"----------------------------\n"
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
