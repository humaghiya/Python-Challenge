#import
import csv
import os

#set varaibles
candidates = []
num_votes = 0
vote_counts = []

# join path

filepath = os.path.join("Resources", "election_data.csv")


#open the file and read
with open(filepath,newline="") as csvfile:
   csvreader = csv.reader(csvfile)

#iterate
   line = next(csvreader,None)
   for line in csvreader:
       num_votes = num_votes + 1
       candidate = line[2]
       if candidate in candidates:
           candidate_index = candidates.index(candidate)
           vote_counts[candidate_index] = vote_counts[candidate_index] + 1
       else:
           candidates.append(candidate)
           vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0
for count in range(len(candidates)):
   vote_percentage = vote_counts[count]/num_votes*100
   percentages.append(vote_percentage)
   if vote_counts[count] > max_votes:
       max_votes = vote_counts[count]
       print(max_votes)
       max_index = count
winner = candidates[max_index]

#print results
print("Election Results")
print("--------------------------")
print(f"Total Votes: {num_votes}")
for count in range(len(candidates)):
   print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

write_file = f"pypoll_results_summary.txt"

#output file
output_file = os.path.join("output.txt")
with open (output_file,"w") as new:
new.write("Election Results\n")
new.write("--------------------------\n")
new.write(f"Total Votes: {num_votes}\n")
for count in range(len(candidates)):
   new.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})\n")
new.write("---------------------------\n")
new.write(f"Winner: {winner}\n")
new.write("---------------------------\n")

output_file.close()