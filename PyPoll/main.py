import csv
import os

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Variables to hold election results
total_votes = 0
candidates = {}
winner = ""
winning_votes = 0

# Open the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # Skip the header

    # Process each row
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Tally votes for each candidate
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 0
        candidates[candidate_name] += 1

# Calculate the percentage of votes for each candidate
results = []
for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {vote_percentage:.3f}% ({votes})")

    # Determine the winner
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

# Generate the election results summary
election_results = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
)  # This closing parenthesis closes the tuple

# Joining results and appending to election_results
election_results += "\n".join(results)
election_results += (
    f"\n-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)  # This closes the second tuple

# Print the results to terminal
print(election_results)

# Save the results to a text file in the Analysis folder
output_path = os.path.join("Analysis", "election_results.txt")
with open(output_path, "w") as txt_file:
    txt_file.write(election_results)
