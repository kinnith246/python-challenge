# import os module and then module for reading csv
import os
import csv


# specify the path and file to write to

base_dir = os.path.dirname(__file__)
budget_path = os.path.join(base_dir, 'Resources', 'budget_data.csv')

# specify variables
def budget_analysis(budget_path):
    total_months = 0
    total_profit_losses = 0
    changes = []
    dates = []
    previous_profit_loss = None

    # open the file using read mode
    with open(budget_path) as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip the header row
        for row in reader:
            date, profit_loss = row
            profit_loss = int(profit_loss)

            # update total months and total profit/losses
            total_months += 1
            total_profit_losses += profit_loss
            
            # calculate change from the previous month
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                changes.append(change)
                dates.append(date)
            
            previous_profit_loss = profit_loss

    # calculate average change
    average_change = sum(changes) / len(changes) if changes else 0

    # determine the greatest increase and decrease in profits
    max_change = max(changes) if changes else 0
    min_change = min(changes) if changes else 0
    max_change_date = dates[changes.index(max_change)]
    min_change_date = dates[changes.index(min_change)]

    # generate the summary of the analysis
    summary_text = (
        "Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total_profit_losses:,.0f}\n"
        f"Average Change: ${average_change:,.2f}\n"
        f"Greatest Increase in Profits: {max_change_date} (${max_change:,.0f})\n"
        f"Greatest Decrease in Profits: {min_change_date} (${min_change:,.0f})\n"

    )
    return summary_text

def main():
    # Path to the directory and file
    output_dir = 'Analysis'
    output_file = 'budget_analysis.txt'
    analysis_path = os.path.join(output_dir, output_file)
    
    # Ensure the directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Perform the analysis
    results = budget_analysis(budget_path)
    
    # Print results to the terminal
    print(results)
    
    # Save the results to a text file in the Analysis folder
    with open(analysis_path, 'w') as file:
        file.write(results)
        
    print(f"The analysis has been saved to '{analysis_path}'.")

if __name__ == "__main__":
    main()
