# modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#storage variables
total_votes = 0
candidates = {}
percentage_vote = 0
candidate_vote_counter = 0

#open data file and skip header
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else: 
            candidates[row[2]] = candidates[row[2]] + 1
    print(total_votes)
    print(candidates)
            