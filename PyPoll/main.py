# modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

#storage variables
total_votes = 0
candidates = {}
percentage_vote = 0
winner = ""
winner_votes = 0

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



    print(type(candidates))
output_file = os.path.join("Election_results.csv")

with open(output_file, "w", newline="") as text_file:
    text_file.write("Election Results\n")
    text_file.write("---------------------------\n")
    for candidates, votes in candidates.items():
        text_file.write(f'Candidates : {candidates}     Votes: {votes}     Percent:{votes*100/total_votes}%\n')
    text_file.write(f'The winner is {winner}')      

print(type(candidates))
print("Election Results")
print("---------------------------")
for candidates, votes in candidates.items():
    print(type(candidates))
    print(f'Candidate : {c_candidate}     Votes: {c_votes}     Percent:{c_votes*100/total_votes}%')
    if votes > winner_votes:
        winner = candidates
        winner_votes = votes
print("The winner is " + winner)