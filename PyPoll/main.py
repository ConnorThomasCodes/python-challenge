import os
import csv

# This program loops through election data stored in a csv format and outputs information to the Terminal and 'poll_results.txt' file in the 'analysis' folder
# It begins by opening the 'election_data.csv' file (data in the format "Ballot ID","County","Candidate") in the 'Resources' folder and storing all information in a list of lists
# We then loop through the outer list and along the way we will
#       1. Find the total votes (rows) entered
#       2. Find all candidates who earned votes in the election
#       3. Tally the total votes for each candidate in the election
# We will do this by keeping two lists of candidates and their tallies with matching indices for cross-referencing
# After our loop is finished we will find the winner of the poll by taking the maximum from our list of vote counts, cross-referencing as needed
# We will also find the percentage of the total votes that each candidate earned
# Our program will then output these results to the Terminal and also as a 'poll_results.txt' file

# Initialize variables
total_votes = 0
candidate_list = []
vote_counts = []
winner = ''

# Create file path for csv file
poll_csv = os.path.join("Resources","election_data.csv")

# Open and read csv
with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row first
    csv_header = next(csv_file)

    # Read through each row of data after the header
    for row in csv_reader:
        # Increment vote counter
        total_votes += 1
        # Check if the chosen candidate is in candidate_list
        if row[2] not in candidate_list:
            # If not, add candidate to list and add a 1 to the vote_counts list
            # The index for the candidate and their vote count will be the same in each list - this will be used for cross-referencing data
            candidate_list.append(row[2])
            vote_counts.append(1)
        else:
            # If the candidate is in candidate_list, increment their vote counter by 1
            # This command works by finding the index of the current candidate in candidate_list and then going to the same index in vote_count and incrementing that value by 1
            vote_counts[candidate_list.index(row[2])] += 1

    # Find the index of the max value in vote_counts (the winner of the election) and print out that same index from candidate_list
    winner = candidate_list[vote_counts.index(max(vote_counts))]

# Print results to Terminal
print(f"Election Resuts\n\n-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")
# Loop through candidate_list for individual printouts
# Index i will match across candidate_list and vote_counts
for i in range(len(candidate_list)):
    print(f"{candidate_list[i]}: {vote_counts[i]/total_votes*100:.3f}% ({vote_counts[i]})\n")
print(f"-------------------------\n")
print(f"Winner: {winner}\n")
print(f"-------------------------")

# Set variable for output file
output_file = os.path.join("analysis","poll_results.txt")

# Open the output file
with open(output_file,"w") as outputfile:
    # Write results to 'poll_results.txt'
    outputfile.write(f"Election Resuts\n\n-------------------------\n\n")
    outputfile.write(f"Total Votes: {total_votes}\n\n")
    outputfile.write("-------------------------\n\n")
    for i in range(len(candidate_list)):
        outputfile.write(f"{candidate_list[i]}: {vote_counts[i]/total_votes*100:.3f}% ({vote_counts[i]})\n\n")
    outputfile.write(f"-------------------------\n\n")
    outputfile.write(f"Winner: {winner}\n\n")
    outputfile.write(f"-------------------------")