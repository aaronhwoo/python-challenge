# modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#storage variables
total_votes = 0
candidates = {}
percentage_vote = 0

#open data file and skip header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
#tally up dictionary total dynamically
    for row in csvreader:
        total_votes = total_votes + 1
        current_vote = row[2]
        if current_vote not in candidates:
            candidates[current_vote] = 1
        else: 
            candidates[current_vote] = candidates[current_vote] + 1
    print(total_votes)
    print(candidates)
            