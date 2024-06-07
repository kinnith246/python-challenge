# import os module and then module for reading csv
import os
import csv

# specify the path and file to write to

base_dir = os.path.dirname(__file__)
election_path = os.path.join(base_dir, 'Resources', 'election_data.csv')

# specify variables
def election_analysis(election_data):
    candidate = str(election_data[2])
    voter_id = str(election_data[0])
    total_votes = 0
    candidate_votes = {}


    # open the file using read mode
    with open(election_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the header row
        for row in reader:
            total_votes += 1
            candidate = row[2]
            if candidate in candidate_votes:
                candidate_votes[candidate] += 1
            else:
                candidate_votes[candidate] = 1

    # calculate percentage of votes and find winner
    results = {}
    max_votes = 0
    winner = ""

    for candidate, votes in candidate_votes.items():
        vote_percentage = (votes / total_votes) * 100
        results[candidate] = (vote_percentage, votes)
        if votes > max_votes:
            max_votes = votes
            winner = candidate

    # generate the summary of the analysis
    output = [
        "Election Results\n"
        "-------------------------\n"
        f"Total Votes: {total_votes}\n"
        "-------------------------\n"
    ]

    for candidate, data in results.items():
        output.append(f"{candidate}: {data[0]:.3f}% ({data[1]})\n")
    
    output += [
        "-------------------------\n"
        f"Winner: {winner}\n"
        "-------------------------\n"
    ]
    return output

def main():
    # path to the directory and file
    output_dir = 'Analysis'
    output_file = 'election_analysis.txt'
    analysis_path = os.path.join(output_dir, output_file)
    
    # ensure the directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # perform the analysis
    results = election_analysis(election_path)
    
    # print results to the terminal
    for line in results:
        print(line, end='')
    
    # save the results to a text file in the Analysis folder
    with open(analysis_path, 'w') as file:
        file.writelines(results)
        
    print(f"The analysis has been saved to '{analysis_path}'.")

if __name__ == "__main__":
    main()