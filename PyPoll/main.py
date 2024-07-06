import csv

# The file path
file_path = 'budget_data.csv'

# Initializing the  variables
total_months = 0
net_total = 0
changes = []
previous_profit = None
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float('inf')}

# Reading the CSV file
with open(file_path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  # This skips the header row
    
    for row in csvreader:
        # Extract date and profit/losses
        date = row[0]
        profit = int(row[1])
        
        # Count of total months
        total_months += 1
        
        # Calculating net total
        net_total += profit
        
        # Calculating the changes and tracking greatest increase and decrease
        if previous_profit is not None:
            change = profit - previous_profit
            changes.append(change)
            
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date
                
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date
        
        # Update previous profit
        previous_profit = profit

# Calculate average change
average_change = sum(changes) / len(changes)

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
