import csv
import os


#function to adjust name format to make formats between scraped and data.csv the same
#Paramteres:
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



#function to start the discrepancy resolution process between scraped and data.csv information 
#Parameters:
#   faculty_names: list of (name, department) tuples that is obtained from web scraper in webscraper.py
def begin_resolution(faculty_names):
    # path of data.csv file 
    file_path = '/Users/angelsoto/Desktop/mostRecent/CS422-Easy-A/data.csv' #TODO: Change this file path 
    name_data = read_data(file_path)

    # Set scrapedData to the list of faculty names obtained by scraper
    scraped_data = faculty_names

    #path to output csv file
    output_file = '/Users/angelsoto/Desktop/mostRecent/CS422-Easy-A/output.csv' #TODO: Change this file path 
    compare_names(name_data, scraped_data, output_file)
