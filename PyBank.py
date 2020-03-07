import os
import csv
import pandas as pd
import numpy as np
dir_path = os.path.dirname(os.path.realpath(''))

csvpath = os.path.join(dir_path, 'today/budget_data.csv')

with open(csvpath) as budget_data:

    # CSV reader
    csvreader = csv.reader(budget_data, delimiter=',')
    csv_header = next(csvreader)
    months = []
    numbers  =[]
    for row in csvreader:
        months.append(row[0])
        numbers.append(row[1])
        
    budget_data = pd.DataFrame(list(zip(months, numbers)), columns =['Date', 'Profit/Losses'])
    total_months=budget_data["Date"].count()

    #create a list
    mylist_change=[]
    mylist_months=[]
    Dates = list(budget_data['Date'][1:])
    for row in range(total_months-1):
      
        firstvalue=budget_data["Profit/Losses"][row]
        secondvalue=budget_data["Profit/Losses"][row+1]
        secondmonth=budget_data["Date"][row]

        mylist_change.append(int(secondvalue)-int(firstvalue))
        mylist_months.append(secondmonth)
   
    changedataframe = pd.DataFrame(list(zip(Dates, mylist_change)), columns =['Date', 'Change'])
    profit_losses_mean=changedataframe.mean()[0]  

    min_location=changedataframe['Change'].idxmin()
    max_location=changedataframe['Change'].idxmax()
    min_change=changedataframe['Change'][min_location]
    min_month=changedataframe['Date'][min_location]
    max_change=changedataframe['Change'][max_location]
    max_month=changedataframe['Date'][max_location]

    net_total = pd.to_numeric(budget_data["Profit/Losses"]).sum()

    file=open("output.txt","w")
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write("Total Months:" + str(total_months) + "\n")
    file.write("Total:" + "$" + str(net_total) + "\n")
    file.write("Average Change:" + str(round(profit_losses_mean, 2)) + "\n")
    file.write("Greatest Increase in Profits:" + ' ' + str(min_month) + ' ' + "$" + "(" + str(max_change) + ")" + "\n")
    file.write("Greatest Decrease in Profits:" + ' ' + str(max_month) + ' ' + "$" + "(" + str(min_change) + ")")