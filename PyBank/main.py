import os
import csv

# Path to the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_profit_losses = 0
previous_profit = None
changes = []
months = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

# Open and read the CSV file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if your CSV has no header)
    header = next(csvreader)
    
    # Loop through each row of data after the header
    for row in csvreader:
        # Count the total number of months
        total_months += 1
        
        # Track the month
        months.append(row[0])
        
        # Calculate the net total of "Profit/Losses"
        profit_losses = int(row[1])
        total_profit_losses += profit_losses
        
        # Calculate changes in "Profit/Losses" between months
        if previous_profit is not None:
            change = profit_losses - previous_profit
            changes.append(change)
            
            # Check for greatest increase in profits
            if change > greatest_increase[1]:
                greatest_increase[0] = row[0]
                greatest_increase[1] = change
            
            # Check for greatest decrease in profits
            if change < greatest_decrease[1]:
                greatest_decrease[0] = row[0]
                greatest_decrease[1] = change
        
        # Set the current profit/loss to previous for the next loop
        previous_profit = profit_losses

# Calculate the average change in "Profit/Losses"
if len(changes) > 0:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Write the results to a text file
output_path = os.path.join("Analysis", "financial_analysis.txt")
with open(output_path, "w") as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_losses}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    txtfile.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
