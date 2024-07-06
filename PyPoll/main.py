import os 
import csv


# csvpath = os.path.join('..', 'Resources','election_data')
csvpath = r"C:\Users\TheuriM\BootCamp\Challenges\Python_Challenge\PyPoll\Resources\election_data.csv"
print(csvpath) 


from collections import Counter

# Load the dataset
# file_path = '/mnt/data/election_data.csv'

# Initialize variables
total_votes = 0
candidates = Counter()

# Read the CSV file
with open(csvpath, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total_votes += 1
        candidates[row['Candidate']] += 1

# Calculate the percentage of votes each candidate won
vote_percentages = {candidate: (votes / total_votes) * 100 for candidate, votes in candidates.items()}

# Determine the winner of the election based on popular vote
winner = max(candidates, key=candidates.get)

# Print the results
print(f"Total Votes: {total_votes}")
print("Candidates:")
for candidate, votes in candidates.items():
    print(f"{candidate}: {votes} votes ({vote_percentages[candidate]:.2f}%)")
print(f"Winner: {winner}")

