# Formatting script to feed out data into Language Analysis Tool
# by Victor Arriaza, Nazim Karaca, Mecheal Greene

import os
from datetime import datetime
import re

#Create list_of_lists of empty list of 23
def create_months_list():
    months = [ [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [] ]
    return months

#from alphabet_detector import AlphabetDetector

#def has_cyrillic(text):
    #ad = AlphabetDetector()
    #return ad.is_cyrillic(unicode(text,"utf-16"))

def move_sadb(csv_file_name, list_of_lists):
    os.chdir("/home/ubuntu/workspace/Contaminated/Interactor_data_V3/")
#    Read in file
    #print("Starting to read file " + csv_file_name)
    with open(csv_file_name) as fp:
        #content = fp.readlines()
#    In this loop, loop over lines in the file (aka tweets)
        skip_first = True
        for line in fp:
            if (skip_first):
                skip_first = False
                continue
            # print line
            if ("\\x" in line):
            #if (has_cyrillic(line)):
                continue
            # Turn line into list (elements separated by semicolon) so we can index it
            # print("not cyrillic")
            listBuffer = line.split(";")
            
            #    Get date from line: date is first 9 characters of second element
            date = listBuffer[1]
            text = listBuffer[4]
            
            #    Parse date into date format
            #    Add text from line into appropriate list (one for each month/year)
            list_of_lists = date_list(date,list_of_lists,text)
    fp.close()
    return list_of_lists


def move_nons(csv_file_name, list_of_lists):
    os.chdir("/home/ubuntu/workspace/Uncontaminated/Term_Tweets_Together/")
    #file_KIRATB = open(csv_file_name, "r")
    #for line in file_KIRATB
#    Read in file
    with open(csv_file_name, "r") as fp:
        #content = fp.readlines()
#    In this loop, loop over lines in the file (aka tweets)
        #print("Starting to read file " + csv_file_name)
        skip_first = True
        for line in fp:
            if (skip_first):
                skip_first = False
                continue
            # print line
            # Turn line into list (elements separated by semicolon) so we can index it
            listBuffer = line.split(";")
            #    Get date from line: date is first 9 characters of second element
            date = listBuffer[1]
            text = listBuffer[4]
            #    Parse date into date format
            #    Add text from line into appropriate list (one for each month/year)
            list_of_lists = date_list(date,list_of_lists,text)
    fp.close()
    return list_of_lists
#return
###############################################################

def date_list(date,list_of_lists,text):

    # Figure out which list to add it to out of 23
    if ("2016-01" in date): #>= d_16_01 and date < d_16_02):
        list_of_lists[0].append(text)
    elif ("2016-02" in date):
        list_of_lists[1].append(text)
    elif ("2016-03" in date):
        list_of_lists[2].append(text)
    elif ("2016-04" in date):
        list_of_lists[3].append(text)
    elif ("2016-05" in date):
        list_of_lists[4].append(text)
    elif ("2016-06" in date):
        list_of_lists[5].append(text)
    elif ("2016-07" in date):
        list_of_lists[6].append(text)
    elif ("2016-08" in date):
        list_of_lists[7].append(text)
    elif ("2016-09" in date):
        list_of_lists[8].append(text)
    elif ("2016-10" in date):
        list_of_lists[9].append(text)
    elif ("2016-11" in date):
        list_of_lists[10].append(text)
    elif ("2016-12" in date):
        list_of_lists[11].append(text)
    # End of 2016
    elif ("2017-01" in date):
        list_of_lists[12].append(text)
    elif ("2017-02" in date):
        list_of_lists[13].append(text)
    elif ("2017-03" in date):
        list_of_lists[14].append(text)
    elif ("2017-04" in date):
        list_of_lists[15].append(text)
    elif ("2017-05" in date):
        list_of_lists[16].append(text)
    elif ("2017-06" in date):
        list_of_lists[17].append(text)
    elif ("2017-07" in date):
        list_of_lists[18].append(text)
    elif ("2017-08" in date):
        list_of_lists[19].append(text)
    elif ("2017-09" in date):
        list_of_lists[20].append(text)
    elif ("2017-10" in date):
        list_of_lists[21].append(text)
    elif ("2017-11" in date):
        list_of_lists[22].append(text)
    return list_of_lists


def main():
    # inform user that something is happening
    print("Working on user:")
    #Loop over files in contaminated folder
    Contaminated_list = create_months_list()
    path = '/home/ubuntu/workspace/Contaminated/Interactor_data_V3/'
    list_of_files = os.listdir(path)
    for filename in list_of_files:
        print("  "+filename)
        if (filename.endswith("_text.csv")): continue
        Contaminated_list = move_sadb(filename, Contaminated_list)
    #print(Contaminated_list)

    os.chdir("/home/ubuntu/workspace/Output/Contaminated/")

    #for month in Contaminated_list:
    with open ("16-01","w") as f_16_01:
        for x in Contaminated_list[0]:
            f_16_01.write(x+'\n')
    f_16_01.close()
    with open ("16-02","w") as f_16_02:
        for x in Contaminated_list[1]:
            f_16_02.write(x+'\n')
    f_16_02.close()
    with open ("16-03","w") as f_16_03:
        for x in Contaminated_list[2]:
            f_16_03.write(x+'\n')
    f_16_03.close()
    with open ("16-04","w") as f_16_04:
        for x in Contaminated_list[3]:
            f_16_04.write(x+'\n')
    f_16_04.close()
    with open ("16-05","w") as f_16_05:
        for x in Contaminated_list[4]:
            f_16_05.write(x+'\n')
    f_16_05.close()
    with open ("16-06","w") as f_16_06:
        for x in Contaminated_list[5]:
            f_16_06.write(x+'\n')
    f_16_06.close()
    with open ("16-07","w") as f_16_07:
        for x in Contaminated_list[6]:
            f_16_07.write(x+'\n')
    f_16_07.close()
    with open ("16-08","w") as f_16_08:
        for x in Contaminated_list[7]:
            f_16_08.write(x+'\n')
    f_16_08.close()
    with open ("16-09","w") as f_16_09:
        for x in Contaminated_list[8]:
            f_16_09.write(x+'\n')
    f_16_09.close()
    with open ("16-10","w") as f_16_10:
        for x in Contaminated_list[9]:
            f_16_10.write(x+'\n')
    f_16_10.close()
    with open ("16-11","w") as f_16_11:
        for x in Contaminated_list[10]:
            f_16_11.write(x+'\n')
    f_16_11.close()
    with open ("16-12","w") as f_16_12:
        for x in Contaminated_list[11]:
            f_16_12.write(x+'\n')
    f_16_12.close()
# End of 2016
################################
    with open ("17-01","w") as f_17_01:
        for x in Contaminated_list[12]:
            f_17_01.write(x+'\n')
    f_17_01.close()
    with open ("17-02","w") as f_17_02:
        for x in Contaminated_list[13]:
            f_17_02.write(x+'\n')
    f_17_02.close()
    with open ("17-03","w") as f_17_03:
        for x in Contaminated_list[14]:
            f_17_03.write(x+'\n')
    f_17_03.close()
    with open ("17-04","w") as f_17_04:
        for x in Contaminated_list[15]:
            f_17_04.write(x+'\n')
    f_17_04.close()
    with open ("17-05","w") as f_17_05:
        for x in Contaminated_list[16]:
            f_17_05.write(x+'\n')
    f_17_05.close()
    with open ("17-06","w") as f_17_06:
        for x in Contaminated_list[17]:
            f_17_06.write(x+'\n')
    f_17_06.close()
    with open ("17-07","w") as f_17_07:
        for x in Contaminated_list[18]:
            f_17_07.write(x+'\n')
    f_17_07.close()
    with open ("17-08","w") as f_17_08:
        for x in Contaminated_list[19]:
            f_17_08.write(x+'\n')
    f_17_08.close()
    with open ("17-09","w") as f_17_09:
        for x in Contaminated_list[20]:
            f_17_09.write(x+'\n')
    f_17_09.close()
    with open ("17-10","w") as f_17_10:
        for x in Contaminated_list[21]:
            f_17_10.write(x+'\n')
    f_17_10.close()
    with open ("17-11","w") as f_17_11:
        for x in Contaminated_list[22]:
            f_17_11.write(x+'\n')
    f_17_11.close()
    # End of 2017
    
    # flush list of lists to save memory
    # Contaminated_list.clear()
    # del Contaminated_list[:]
    
    # stop = input("Stop here.")
    
    #Loop over files in uncontaminated folder
    UnContaminated_list = create_months_list()
    path = '/home/ubuntu/workspace/Uncontaminated/Term_Tweets_Together/'
    for filename in os.listdir(path):
        print("  "+filename)
        UnContaminated_list = move_nons(filename,UnContaminated_list)
    
    os.chdir("/home/ubuntu/workspace/Output/Uncontaminated/")

    #for month in Contaminated_list:
    with open ("16-01","w") as f_16_01:
        for x in UnContaminated_list[0]:
            f_16_01.write(x+'\n')
    f_16_01.close()
    with open ("16-02","w") as f_16_02:
        for x in UnContaminated_list[1]:
            f_16_02.write(x+'\n')
    f_16_02.close()
    with open ("16-03","w") as f_16_03:
        for x in UnContaminated_list[2]:
            f_16_03.write(x+'\n')
    f_16_03.close()
    with open ("16-04","w") as f_16_04:
        for x in UnContaminated_list[3]:
            f_16_04.write(x+'\n')
    f_16_04.close()
    with open ("16-05","w") as f_16_05:
        for x in UnContaminated_list[4]:
            f_16_05.write(x+'\n')
    f_16_05.close()
    with open ("16-06","w") as f_16_06:
        for x in UnContaminated_list[5]:
            f_16_06.write(x+'\n')
    f_16_06.close()
    with open ("16-07","w") as f_16_07:
        for x in UnContaminated_list[6]:
            f_16_07.write(x+'\n')
    f_16_07.close()
    with open ("16-08","w") as f_16_08:
        for x in UnContaminated_list[7]:
            f_16_08.write(x+'\n')
    f_16_08.close()
    with open ("16-09","w") as f_16_09:
        for x in UnContaminated_list[8]:
            f_16_09.write(x+'\n')
    f_16_09.close()
    with open ("16-10","w") as f_16_10:
        for x in UnContaminated_list[9]:
            f_16_10.write(x+'\n')
    f_16_10.close()
    with open ("16-11","w") as f_16_11:
        for x in UnContaminated_list[10]:
            f_16_11.write(x+'\n')
    f_16_11.close()
    with open ("16-12","w") as f_16_12:
        for x in UnContaminated_list[11]:
            f_16_12.write(x+'\n')
    f_16_12.close()
# End of 2016
################################
    with open ("17-01","w") as f_17_01:
        for x in UnContaminated_list[12]:
            f_17_01.write(x+'\n')
    f_17_01.close()
    with open ("17-02","w") as f_17_02:
        for x in UnContaminated_list[13]:
            f_17_02.write(x+'\n')
    f_17_02.close()
    with open ("17-03","w") as f_17_03:
        for x in UnContaminated_list[14]:
            f_17_03.write(x+'\n')
    f_17_03.close()
    with open ("17-04","w") as f_17_04:
        for x in UnContaminated_list[15]:
            f_17_04.write(x+'\n')
    f_17_04.close()
    with open ("17-05","w") as f_17_05:
        for x in UnContaminated_list[16]:
            f_17_05.write(x+'\n')
    f_17_05.close()
    with open ("17-06","w") as f_17_06:
        for x in UnContaminated_list[17]:
            f_17_06.write(x+'\n')
    f_17_06.close()
    with open ("17-07","w") as f_17_07:
        for x in UnContaminated_list[18]:
            f_17_07.write(x+'\n')
    f_17_07.close()
    with open ("17-08","w") as f_17_08:
        for x in UnContaminated_list[19]:
            f_17_08.write(x+'\n')
    f_17_08.close()
    with open ("17-09","w") as f_17_09:
        for x in UnContaminated_list[20]:
            f_17_09.write(x+'\n')
    f_17_09.close()
    with open ("17-10","w") as f_17_10:
        for x in UnContaminated_list[21]:
            f_17_10.write(x+'\n')
    f_17_10.close()
    with open ("17-11","w") as f_17_11:
        for x in UnContaminated_list[22]:
            f_17_11.write(x+'\n')
    f_17_11.close()
    # End of 2017
    
    
    print("done")

# At the end write each list into an appropriate file

main()