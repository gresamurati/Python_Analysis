#import directories
import os
import csv
import pandas as pd

#set path
dir_path = os.path.dirname(os.path.realpath(''))
csvpath = os.path.join(dir_path, 'today/election_data.csv')

#open csv files
with open(csvpath) as election_data:
    # CSV reader
    csvreader = csv.reader(election_data, delimiter=',')
    print(csvreader)

    #create empty lists to hold variables
    votes=[]
    unique_names=[]

    #turn csv into a df
    election_data_df=pd.read_csv('election_data.csv')
    election_data_df.head()

    #The total number of votes cast
    total_votes=election_data_df['Voter ID'].count()

    #A complete list of candidates who received votes
    unique_names=election_data_df.Candidate.unique()

    #empty lists for unique candidates
    Khan_list=[]
    Correy_list=[]
    OTooley_list=[]
    Li_list=[]

    number=len(election_data_df)

    #loop to find specific values based on their names
    for row in range(number):
        if election_data_df["Candidate"][row] == "Khan":
            Khan_list.append(election_data_df["Voter ID"][row])
        elif election_data_df["Candidate"][row] == "Correy":
            Correy_list.append(election_data_df["Voter ID"][row])
        elif election_data_df["Candidate"][row] == "O'Tooley":
            OTooley_list.append(election_data_df["Voter ID"][row])
        elif election_data_df["Candidate"][row] == "Li":
            Li_list.append(election_data_df["Voter ID"][row])

    #The total number of votes each candidate won 
    Khan_total=len(Khan_list)
    Correy_total=len(Correy_list)
    Li_total=len(Li_list)
    OTooley_total=len(OTooley_list)

    #The percentage of votes each candidate won
    Khan_percentage=round(Khan_total/total_votes*100,2)
    Correy_percentage=round(Correy_total/total_votes*100,2)
    Li_percentage=round(Li_total/total_votes*100,2)
    OTooley_percentage=round(OTooley_total/total_votes*100,2)

    #new df based on percentages and names
    df=pd.DataFrame(
        {"Name": ["Khan", "Correy", "Li","O'Tooley"],
        "Percentages": [Khan_percentage, Correy_percentage, Li_percentage, OTooley_percentage]})
   
    highest_percentage_location=df["Percentages"].idxmax()

    #The winner of the election based on popular vote
    Winner=df["Name"][highest_percentage_location]
    
    #writing to text file
    file=open("PyPollOutput.txt","w")
    file.write("Election Results" + "\n")
    file.write("----------------------------\n")
    file.write("Total Votes:" + str(total_votes) + "\n")
    file.write("----------------------------\n")
    file.write("Khan:" + str(Khan_percentage) + "%" +" " + "("+ str(Khan_total) + ")" + "\n")
    file.write("Correy:" + str(Correy_percentage) + "%" +" " + "("+ str(Correy_total) + ")" + "\n")
    file.write("Li:" + str(Li_percentage)+ "%" +" " + "("+ str(Li_total) + ")" + "\n")
    file.write("O'Tooley:" + str(OTooley_percentage) + "%" +" " + "("+ str(OTooley_total) + ")" + "\n")
    file.write("----------------------------\n")
    file.write("Winner:" + str(Winner))
  