# modules
import os
import csv

#Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

#create storage variables

total_mon = 0
net_profit = 0
avg_profit = 0
g_increase = 0
g_decrease = 0
g_increase_date = ""
g_decrease_date = ""


# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    # Loop through rows aggregating data
    for row in csvreader:
        total_mon = total_mon + 1
        profit = int(row[1])
        net_profit = net_profit + profit
        if profit > g_increase:
            g_increase = profit
            g_increase_date = row[0]
        if profit < g_decrease:
            g_decrease = profit
            g_decrease_date = row[0]

avg_profit = net_profit/total_mon
        
#print("Financial Analysis")
#print("--------------------------------------------------")
#print(f"Total Months: {total_mon}")
#print(f"Total: ${net_profit}")
#print(f"Average Change: ${avg_profit}")
#print(f'Greatest Increase in Profits: {g_increase_date} (${g_increase})')
#print(f'Greatest Decrease in Profits: {g_decrease_date} (${g_decrease})')

row0 = ["Financial Analysis"]
row1 = ["--------------------------------------------------"]
row2 = [f"Total Months: {total_mon}"]
row3 = [f"Total: ${net_profit}"]
row4 = [f"Average Change: ${avg_profit}"]
row5 = [f'Greatest Increase in Profits: {g_increase_date} (${g_increase})']
row6 = [f'Greatest Decrease in Profits: {g_decrease_date} (${g_decrease})']

print(row0)
print(row1)
print(row2)
print(row3)
print(row4)
print(row5)
print(row6)

#export = zip(row0, row1, row2, row3, row4, row5, row6)

#can't get this to work in a formatted way
#for analysis in export: 
#    print(analysis)

output_file = os.path.join("financial_analysis.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #writer.writerows(export) doesn't seem to work but it works with individual row, problem in tuple?
    writer.writerow(row0)
    writer.writerow(row1)
    writer.writerow(row2)
    writer.writerow(row3)
    writer.writerow(row4)
    writer.writerow(row5)
    writer.writerow(row6)