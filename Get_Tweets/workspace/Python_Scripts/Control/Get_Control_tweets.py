import os
import sys
from subprocess import call
from os import listdir
from os.path import isfile, join
import collections
import time

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
    call(["python", "Exporter_Control.py","--since", "2016-01-01", "--until", "2017-11-04","--querysearch", term,"maxtweets","2000"])
    # Note: Tweets for THIS PROGRAM ONLY are stored at "/home/ubuntu/workspace/Retrieved data/Interacter_data/"
    return

def get_user_tweets(user):
    # Time is year-month-day
    #call(["python", "Exporter.py","--querysearch",KIRATB,"--maxtweets", "3"])
    call(["python", "Exporter_Control.py","--since", "2016-01-01", "--until", "2017-11-04","--username", user])
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

# Control_list_terms = ["a","and","the"]
# Control_list_terms_files = ["a.csv","and.csv","the.csv"]

# for term in Control_list_terms:
#     get_term_tweets(term)

# # Go to control data, term tweets location
# os.chdir("/home/ubuntu/workspace/data/Control_data")

# username_list = []
# for file_name in Control_list_terms_files:
#     first_row = True
#     file_term = open(file_name, "r")
#     for line in file_term:
#         line_list = line.split(";")
#         if (first_row):
#             first_row = False
#         else:
#             username = line_list[0]
#             username_list.append(username)
#     file_term.close()

# # take out duplicates
# username_counter = collections.Counter(username_list)
# username_list = username_counter.keys()

# new_file = open("Usernames_list.csv","w")        
# for user in username_list:
#     new_file.write(user + "\n")
# new_file.close()



# Go to control data location
os.chdir("/home/ubuntu/workspace/data/Control_data/")
new_file = open("Usernames_list.csv","r")
user_list = []
for line in new_file:
    user_list.append(line[:-1])
new_file.close()

#print(user_list[0:20])

# Find out where code previously stopped so we don't have to run this from scratch
# Find index of last non empty user file
#print(user_list.index("gouravkhandel16"))
#print(user_list[1769])
# we get 1768
# Make list start from there and stop at an arbitrary high value we will never get to
user_list = user_list[1769:20000]

#print(user_list[0])
stop = raw_input("Stop here for testing.")

os.chdir("/home/ubuntu/workspace/Python_Scripts/Control/")
for user in user_list:
    get_user_tweets(user)
    time.sleep(10)




















