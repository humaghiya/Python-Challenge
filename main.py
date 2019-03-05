
#import
import os
import csv

#set variables

month_count = []
profit = []
change_profit = []

#join paths

filepath = os.path.join("Resources", "budget_data.csv")

#open and read csv file -make sure to set delimiter
with open(filepath, newline= "") as csvfile:
   csvreader=csv.reader(csvfile, delimiter= ",")
   header = next(csvreader)



#iterate through all values
   for row in csvreader:
       month_count.append(row[0])
       profit.append(int(row[1]))
   for i in range(len(profit)-1):
       change_profit.append(profit[i+1]-profit[i])


   increase=max(change_profit)
   decrease=min(change_profit)

   month_increase = change_profit.index(max(change_profit))+1
   month_decrease = change_profit.index(min(change_profit))+1

#print results
print(" Financial Analysis:")
print("--------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits:{month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profit:{month_count[month_decrease]}(${(str(decrease))})")


write_file = f"pybank_results_summary.txt"

#insert output file
output_file = os.path.join("output.txt")
with open (output_file,"w") as new:
    new.write("Financial Analysis\n")
    new.write("--------------------------\n")
    new.write(f"Total Months:{len(month_count)}\n")
    new.write(f"Total: ${sum(profit)}\n")
    new.write(f"Average Change:{round(sum(change_profit)/len(change_profit),2)}\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})\n")

    output_file.close()