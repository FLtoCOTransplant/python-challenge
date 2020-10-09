# dependents
import os
import csv

# Path to collect data from the Resources folder
vote_csv=os.path.join("Resources","election_data.csv")

# Define variables
t_votes = 0
candidate = {}

#File output
analysis = os.path.join("Voting Results for Small_Town, USA.txt")

# Open and read csv
with open(vote_csv) as csv_file:
    vote_reader = csv.reader(csv_file, delimiter=",")

#Read the header and skip first row
    header = next(vote_reader)
    #print(f"Header: {budget_csv}")   
    
    #start collecting data denoting each row
    for row in vote_reader:  

        #determine total votes
        t_votes+= 1

        #Total up the votes for each candidate as we collect candicate names
        if row[2] in candidate:
            candidate[row[2]]+= 1
        #if that candidate is not in the list add them
        else:
            candidate[row[2]] = 1

#Output results to file
with open(analysis, "w") as txt_file:

    #Who is the winner
    winner = max(candidate.keys())

    # Provide the public with the results of the election 
    results = (
        f"      Election Results\n"
        f"----------------------------\n"
        f"Total # of votes cast : {t_votes}\n"
        f"----------------------------\n"
        f"Result for Each Candidate\n"
        
    )           

    #Show output in terminal
    print(results)
    txt_file.write(results)

        #Calc the percent of each candidates votes
    for key,value in candidate.items():
        perc_vote = str(round((value/t_votes)*100,3))+ "%" + " ("+str(value)+ ")"
        print (f"Results for {key} - {perc_vote}")
    print (f"Winner of the Election is: {winner}\n")
        
            