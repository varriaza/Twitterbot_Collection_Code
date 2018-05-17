from os import listdir
import os

count = 0
count_con = 0
count_uncon = 0

# Contaminated first
os.chdir("/home/ubuntu/workspace/Output/Contaminated/")
current_dir = os.getcwd()
file_list = os.listdir(current_dir)
#print(file_list)

for file in file_list:
    with open(file, "r") as cur_file:
        for line in cur_file:
            count = count + 1
            count_con += 1


# Contaminated first
os.chdir("/home/ubuntu/workspace/Output/Uncontaminated/")
current_dir = os.getcwd()
file_list = os.listdir(current_dir)
#print(file_list)

for file in file_list:
    with open(file, "r") as cur_file:
        for line in cur_file:
            count = count + 1
            count_uncon += 1

print("The total tweet count is: " + str(count))
print("The total Contaminated tweet count is: " + str(count_con))
print("The total Uncontaminated tweet count is: " + str(count_uncon))













