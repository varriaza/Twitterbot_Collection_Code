import os
import sys
from subprocess import call
from os import listdir
from os.path import isfile, join
import collections

# Read csv file of usernames and return a list of usernames
def read_file(file_name):
    username_list = []
    username_file = open(file_name, "r")
    for username in username_file:
        username_list.append(username)
    username_file.close()
    return username_list 

def get_term_tweets(term):
    # Time is year-month-day
    #call(["python", "Exporter.py","--querysearch",KIRATB,"--maxtweets", "3"])
    call(["python", "Exporter_Interactor.py","--since", "2016-01-01", "--until", "2017-11-04","--querysearch", term,"maxtweets","2000"])
    # Note: Tweets for THIS PROGRAM ONLY are stored at "/home/ubuntu/workspace/Retrieved data/Interacter_data/"
    return

def get_user_tweets(user):
    # Time is year-month-day
    #call(["python", "Exporter.py","--querysearch",KIRATB,"--maxtweets", "3"])
    call(["python", "Exporter_Interactor.py","--since", "2016-01-01", "--until", "2017-11-04","--username", user])
    # Note: Tweets for THIS PROGRAM ONLY are stored at "/home/ubuntu/workspace/Retrieved data/Interacter_data/"
    return

def get_text(csv_file_name, username):
    print("Finding text for file: " + csv_file_name)
    text_list = []
    file_user = open(csv_file_name, "r")
    first_row = True
    for line in file_user:
        line_list = line.split(";")
        #Skip first line as it holds column names
        if (first_row):
            first_row = False
        else:
            text = line_list[4]
            text_list.append(text) # + ",") Try without "," as it could be mistaken for text?
            
    file_user.close()
    new_file = open(username + "_text.csv","w")        
    for text in text_list:
        new_file.write(text + "\n")
    new_file.close()
    print("Done finding usernames for file: " + csv_file_name)
    return
####################################################################################################################
# Code starts here

# Loop through files with the usernames of people who responded to a KIRATB
os.chdir("/home/ubuntu/workspace/data/responses_data")

#Command to get all the Files in our directory
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
# Make sure we only have .csv files and no python files or anything like that
only_csv = []
for file in onlyfiles:
    # Checks if the last 9 characters in the string are "names.csv"
    if (file[-9:] == "names.csv"):
        only_csv.append(file)

#ISSUE POSSIBLY IN USERNAME LIST CODE BELOW
#print(len(onlyfiles))
#print(only_csv[1:10])
username_list = []
for file in only_csv:
    # Get a list of all of the usernames (with duplicates)
    username_list = username_list + read_file(file)
    
    #os.remove(file) # THIS WILL DELETE THE FILE!!! ONLY UNCOMMENT WHEN WE KNOW THIS WORKS PERFECTLY!
    
# You can use sets to obtain a merged list of unique values
#username_list = list(set(username_list))

#USERNAME LIST IS EMPTY
#print(len(username_list))
#print("Before eliminating duplicates: " + str(len(username_list)))

# Or we can use collections.Counter to get unique values and number of them
username_counter = collections.Counter(username_list)
# username_counter.values() will print list of number of repeats
# username_counter.keys() will print list of actual list quantities (aka the usernames)
# username_counter.most_common(Number) will print list of lists with key and value of length Number
# ^^^ good for finding the top X results

#print("After eliminating duplicates: " + str(len(username_counter.values())))    

#top_users = username_counter.most_common(5000)

common_user = username_counter.most_common(120000)
high = 101
low = 9
hold_list = []
for user in common_user:
    count = user[1]
    if count < high and count > low:
        hold_list.append(user)
top_users = hold_list

# Testing
print(len(top_users))
print(top_users[1:20])
stop = raw_input("Stop here.")


name_list = []
counts_list = []
for user in top_users:
    name_list.append(user[0])
    counts_list.append(user[1])

# Get rid of bad characters in names (eg the "," and "\n")
name_list2 = []
for name in name_list:
    name_list2.append(name[:-2])

name_list = name_list2

#print("Top 20 Interactors: ")
#print(top_users[0:20])
#
#print(counts_list[1])
#print(top_users[4999])

##### PLOTS!
# os.chdir("/home/ubuntu/workspace/data/Interactor_data/plots")
# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.hist(counts_list, range(1,500), cumulative = -1, log=True)
# fig.savefig("Top_users_hist_cumu_log1.png")

# Return to directory with correct exporter file (we want Exporter_interacter.py)
os.chdir("/home/ubuntu/workspace/Python_Scripts/Interactor/")
# Note: Tweets for THIS PROGRAM ONLY are stored at "/home/ubuntu/workspace/data/Interacter_data/"
print("Gettting Tweets")

# Testing
#print(name_list[0])
#get_user_tweets(name_list[0])
#name_list = name_list[0:2]

# Get the tweets!
for user in name_list:
    get_user_tweets(user)
    

# Go back to data folder
os.chdir("/home/ubuntu/workspace/data/Interactor_data")

#Command to get all the Files in our directory
onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
# Make sure we only have .csv files and no python files or anything like that
only_csv = []
for file in onlyfiles:
    # Checks if the last 4 characters in the string are ".csv"
    if (file[-4:] == ".csv"):
        only_csv.append(file)

#print(only_csv)
for file in only_csv:
    #print("\n")
    #print("Printing user")
    #print(file[:-4])
    get_text(file,file[:-4])




























