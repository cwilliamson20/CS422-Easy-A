# This module resolves discrepancies between the webscraper and updating names as regular faculty
# Author(s): Etienne Casal-Jouaux, Angel Soto, Connie Williamson
# Group 4
# Created 1/28/2024
# Date Last Modified: 2/4/2024
import csv
import os
import operator


#function to adjust name format to make formats between scraped and data.csv the same
#Parameters:
#   Original_name: name from data.csv in the format of "last, middleinitial. first"
#                  The name will be changed into  "first middleinitial. last"
def adjust_name(original_name):
    if ',' not in original_name:
        return original_name

    last_name, first_and_middle = map(str.strip, original_name.split(',',1))
    first, *middle = first_and_middle.split()
    middle_initials = ' '.join([name[0] + '.' for name in middle])
    transformed_name = f"{first} {middle_initials} {last_name}"
    
    return transformed_name



# Read data from data.csv into memory
#Parameters:
#   file_path: path to the data.csv file which will be read into
#Returns:
#    name_data: list of adjusted names after they are ran through adjusted_name()
def read_data(file_path):
    name_data = []
    with open(file_path) as file: #open data.csv file 
        reader = csv.DictReader(file)
        # for loop to adjust the format of the name and save the appropriate row to a list
        for row in reader: 
            adjusted_name = adjust_name(row['INSTRUCTOR'])
            name_data.append((adjusted_name, row))
    return name_data



#function to handle comparison between names as well as write information to output file
#output is stored in file named: "output.csv"
#Parameters:
#   name_data: list of (name, row) tuples that is obtained from data.csv
#   scraped_data: list of (name, department) tuples that is obtained from web scraper
#   output_file: path to the output csv file where the name and is_faculty paramer will be stored
def compare_names(name_data, scraped_data, output_file):
    with open(output_file, 'w', newline='') as csvfile: #open output file where name and is_faculty data is to be saved 
        csvfile.truncate() #clear the output file (important when running more than once so that new data overrides old data)
        field_names = ['NAME', 'IS_FACULTY'] #set field_names for output csv file
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()


        existing_names = set()
        # for loop to store existing names and set is_faculty for existing rows
        for name, row in name_data:
            existing_names.add(name)
            writer.writerow({'NAME': name, 'IS_FACULTY': 1 if name in [n[0] for n in scraped_data] else 0})

        # for loop to append unmatched names
        for name, _ in scraped_data:
            if name not in existing_names:
                writer.writerow({'NAME': name, 'IS_FACULTY': 1})
                
# this function is used to sort and delete duplicates in the outpuf.csv file
#Parameters:
#       output_file: the csv file where output is stored from compare_names
def cleanup_output(output_file):
    with open(output_file, 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Sort the data by 'NAME'
    sorted_data = sorted(data, key=lambda x: x['NAME'])

    # Remove duplicates
    deduplicated_data = []
    seen_names = set()
    for row in sorted_data:
        if row['NAME'] not in seen_names:
            deduplicated_data.append(row)
            seen_names.add(row['NAME'])

    # Write the sorted and deduplicated data back to the output file
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['NAME', 'IS_FACULTY']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(deduplicated_data)


#function to start the discrepancy resolution process between scraped and data.csv information 
#Parameters:
#   faculty_names: list of (name, department) tuples that is obtained from web scraper in webscraper.py
def begin_resolution(faculty_names):
    # path of data.csv file 
    file_path = 'data.csv' #TODO: Change this file path
    name_data = read_data(file_path)

    # Set scrapedData to the list of faculty names obtained by scraper
    scraped_data = faculty_names

    #path to output csv file
    output_file = 'output.csv' #TODO: Change this file path
    compare_names(name_data, scraped_data, output_file)

    cleanup_output(output_file)
