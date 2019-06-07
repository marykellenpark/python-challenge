import csv
import os

path = os.path.join('c:\\' , 'users' , 'Kellen Park' , 'Desktop' , 'budget_data.csv')

total_months = []
total_profit = []
monthly_profit_change = []

with open(path, 'r') as budget_file:
    csv_reader = csv.reader(budget_file, delimiter=',')

    csv_header = next(csv_reader)

    for row in csv_reader: 
        total_months.append(row[0])
        total_profit.append(int(row[1]))

for i in range(len(total_profit)-1):
    monthly_profit_change.append(total_profit[i+1]-total_profit[i])

increase_value = max(monthly_profit_change)
decrease_value = min(monthly_profit_change)

increase_month = monthly_profit_change.index(max(monthly_profit_change)) + 1
decrease_month = monthly_profit_change.index(min(monthly_profit_change)) + 1

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[increase_month]} (${(str(increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[decrease_month]} (${(str(decrease_value))})")

output_file = path("python-challenge", "PyBank", "Financial_Analysis.txt")

with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[increase_month]} (${(str(increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[decrease_month]} (${(str(decrease_value))})")
