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

row0 = "Financial Analysis"
row1 = "--------------------------------------------------"
row2 = f"Total Months: {total_mon}"
row3 = f"Total: ${net_profit}"
row4 = f"Average Change: ${avg_profit}"
row5 = f'Greatest Increase in Profits: {g_increase_date} (${g_increase})'
row6 = f'Greatest Decrease in Profits: {g_decrease_date} (${g_decrease})'

export_zip = [row0, row1, row2, row3, row4, row5, row6]

for row in export_zip:
    print(row)


output_file = os.path.join("financial_analysis.csv")

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)
    #writer.writerow(export_zip)
    data = [i.strip()split(',') for i in export_zip]
    for d in data
        writer.writerow(d)
    #writer.writerow(row0)
    #writer.writerow(row1)
    #writer.writerow(row2)
    #writer.writerow(row3)
    #writer.writerow(row4)
    #writer.writerow(row5)
    #writer.writerow(row6)