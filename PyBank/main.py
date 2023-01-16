import os
import csv

# This program loops through financial data stored in a csv format and outputs information to the Terminal and a 'budget_results.txt' file in the 'analysis' folder
# It begins by opening the 'budget_data.csv' file (data in the format "Month-Year","Profit/Loss") in the 'Resources' folder and storing all information in a list of lists
# We then loop through the outer list and along the way we will
#       1. Find the total months (rows) entered
#       2. Find the net total profit/loss for the period
#       3. Calculate the month-to-month changes and save them in a list, and also the average month-to-month change
#       4. Find the greatest month-to-month increase and decrease
# Our program will then output this information to the Terminal and also as a 'budget_results.txt' file


# Create file path for csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous = None
changes = []
changes_total = 0
changes_average = 0
greatest_inc = 0
inc_date = ''
greatest_dec = 0
dec_date = ''



# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        # Increment month counter
        total_months += 1
        # Accumulate net total
        net_total += int(row[1])
        # Check if we have a previous entry
        if previous != None:
            # Add change to list of changes
            changes.append(int(row[1])-previous)
            # Compare against current greatest increase and decrease
            if greatest_inc < int(row[1])-previous:
                greatest_inc = int(row[1])-previous
                inc_date = row[0]
            if greatest_dec > int(row[1])-previous:
                greatest_dec = int(row[1])-previous
                dec_date = row[0]
            # Accumulate total changes (for use in average calculation)
            changes_total += int(row[1])-previous
            # Overwrite previous value
            previous = int(row[1])
        # If no previous value then store the first entry as the previous for next iteration
        else:
            previous = int(row[1])

changes_average = changes_total/len(changes)

# Print output text in Terminal  
print("Financial Analysis \n\n----------------------------\n")
print(f"Total Months: {total_months}\n")
print(f"Net Total: ${net_total}\n")
print(f"Average Change: ${changes_average:.2f}\n")
print(f"Greatest Increase: {inc_date} (${greatest_inc})\n")
print(f"Greatest Decrease: {dec_date} (${greatest_dec})")

# Set variable for output file
output_file = os.path.join("analysis","budget_results.txt")

#  Open the output file
with open(output_file, "w") as outputfile:
    # Write output text to 'budget_results.txt'
    outputfile.write("Financial Analysis\n\n----------------------------\n\n")
    outputfile.write(f"Total Months: {total_months}\n\n")
    outputfile.write(f"Net Total: ${net_total}\n\n")
    outputfile.write(f"Average Change: ${changes_average:.2f}\n\n")
    outputfile.write(f"Greatest Increase: {inc_date} (${greatest_inc})\n\n")
    outputfile.write(f"Greatest Decrease: {dec_date} (${greatest_dec})")