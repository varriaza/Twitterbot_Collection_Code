#-------
# Victor, use the GetOldTweets to get a list of users who replied to or retweeted KIRATB tweets. 
# I think to do this you will need to search for tweets that mention the KIRATBs.
#-------

# Take in list of KIRATB

# For each KIRATB call exporter.py with mentions of the KIRATB
import os
import sys
from subprocess import call

import Exporter_replies


def find_Tweets(KIRATB_list):
    for KIRATB in KIRATB_list:
        # Time is year-month-day
        #call(["python", "Exporter.py","--querysearch",KIRATB,"--maxtweets", "3"])
        call(["python", "Exporter_replies.py","--since", "2016-01-01", "--until", "2017-11-04","--querysearch",KIRATB])
    return


# There is no way to check if a tweet is a reply and this removes tweets that reply to KIRATBs
# Scratch the above, found a way. Use this.
def remove_false_positives(csv_file_name, KIRATB_name):
    print("Removing false positives for file: " + csv_file_name)
    file_KIRATB = open(csv_file_name, "r")
    new_file = open(KIRATB_name + "_Users_Tweets.csv","w")
    #Skip first line as it holds column names
    first_row = True
    for line in file_KIRATB:
        # Create boolians to see if the KIRATB username shows up in those sections
        mentioned_in_text = False
        mentioned_in_mentions = False
        mentioned_in_replies = False
        #Skip first line as it holds column names
        if (first_row):
            first_row = False
            new_file.write(line)
        else:
            line_list = line.split(";")
            text = line_list[4]
            replies = line_list[-1]
            mentions = line_list[6]
            # Remove @ before usernames
            # if (mentions[0] != None):
            #     index = 0
            #     for name in mentions:
            #         mentions[index] = name[1:]
            
            if KIRATB_name in text:
                mentioned_in_text = True
            if KIRATB_name in mentions:
                mentioned_in_mentions = True
            if KIRATB_name in replies:
                mentioned_in_replies = True
            
            # If we found the name in one of the sections the line is good.    
            if (mentioned_in_mentions or mentioned_in_text or mentioned_in_replies):
                new_file.write(line)
    print("False positives removed" + "\n")
    file_KIRATB.close()
    new_file.close()
    return       

def get_usernames(csv_file_name, KIRATB_name):
    print("Finding usernames for file: " + csv_file_name)
    username_list = []
    #os.chdir("/home/ubuntu/workspace/Retrieved data/KIRATB_Responses/")
    file_KIRATB = open(csv_file_name, "r")
    first_row = True
    for line in file_KIRATB:
        line_list = line.split(";")
        #Skip first line as it holds column names
        if (first_row):
            first_row = False
        else:
            username = line_list[0]
            username_list.append(username + ",")
            #print(username)
    file_KIRATB.close()
    new_file = open(KIRATB_name + "_Usernames.csv","w")        
    for user in username_list:
        new_file.write(user + "\n")
    new_file.close()
    print("Done finding usernames for file: " + csv_file_name)
    return

####################################################################################################################
# Running Code starts here




KIRATB_list = []

# NOTE: I (Victor) edited RobbyDelaware out of this list
file_KIRATB_list = open("KIRATB list.txt", "r")
for KIRATB in file_KIRATB_list:
    #print(KIRATB[:-1])
    # There are two strange characters at the end of every name so we get rid of them with [:-2]
    KIRATB_list.append(KIRATB[:-2])
file_KIRATB_list.close()

#KIRATB_list = ["2ndHalfOnion"]
#KIRATB_list = KIRATB_list[1:6]

find_Tweets(KIRATB_list)

# Go to directory with data
os.chdir("/home/ubuntu/workspace/data/responses_data")

for KIRATB in KIRATB_list:
    remove_false_positives(KIRATB + ".csv",KIRATB) 
    get_usernames(KIRATB + "_Users_Tweets.csv",KIRATB) 
    #os.remove(KIRATB + "_Users_Tweets.csv")
    #os.remove(KIRATB + ".csv")



