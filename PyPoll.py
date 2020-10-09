# dependents
import os
import csv

# Path to collect data from the Resources folder
vote_csv=os.path.join("Resources","election_data.csv")

# Define variables
t_votes = 0
vote_count = 0
w_candidate = ""

#File output
analysis = os.path.join("Resources", "Voting Results for Small Town, USA.txt")

# Open and read csv
with open(vote_csv) as csv_file:
    vote_csv = csv.reader(csv_file, delimiter=",")