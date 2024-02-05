# This module handles pulling relevant data from data.csv for basicgraph.py to use and display
# Author(s): Etienne Casal-Jouaux, Connie Williamson
# Group 4
# Created 1/23/2024
# Date Last Modified: 2/4/2024
import csv
from enum import Enum

# see gen_data documentation
class Course_Data_Mode(Enum):
    SINGLE_COURSE = 1
    DEPARTMENT = 2
    COURSE_LEVEL = 3

# see gen_data documentation
class Value_Data_Mode(Enum):
    PERC_AS= "aprec"
    # PERC_BS="bprec"
    # PERC_CS="cprec"
    # PERC_DS="dprec"
    # PERC_FS="fprec"
    PERC_D_AND_PERC_F="D/F"



#helper function for gen_data
def proc_row(row: dict, mode: Value_Data_Mode):
    # Either take the %As from a course or combine the % Ds and Fs from a course.
    if mode is not Value_Data_Mode.PERC_D_AND_PERC_F:
        return float(row[mode.value])
    elif mode is Value_Data_Mode.PERC_D_AND_PERC_F:
        return (float(row[Value_Data_Mode.PERC_DS.value])+float(row[Value_Data_Mode.PERC_FS.value]))

# generate data for graph
# params:
# subject - the subject of the course. For example MATH
# course -  the subject code for the course. For example 251, or the entire department level (100 to 400) 
# mode - the data criteria mode. For example SINGLE_COURSE
#    If you choose mode SINGLE_COURSE, then only the course code will be matched
#    If you choose mode COURSE_LEVEL, then the first digit of the string will determine the level
#    If you choose mode DEPARTMENT, then the value of course will be ignored
# year - the years you want to search. For example, "2015 2016"
#   You can put a single year (e.g. "2014"),
#   multiple years (e.g. "2014 2016"),
#   or an asterix for all years (e.g. "*.")
# values -  what values do you want to retrieve. What do tou want to measure? For example, PERC_AS
#   PERC_AS will only take percent As
#   PERC_D_AND_PERC_F will compound the nonpassing grades D + F
# output_mode - what you want the keys in the return dict to be. Either "Instructor" or "Class".
# show_nums - put the number of coures in the key for the dictionary in the format PROF_NAME (NUM). Either True or False (default)
# reg_fac_only - show only regular faculty. output.csv must exist or else nothing will be returned. Either True or False (default(
# return:
# a dict in the format {string : float} {PROFESSOR_NAME : METRIC} or {CLASS_NUM : METRIC}.
# the values in the dictionary will be averaged for every class the professor teaches
# the dictionary will be unsorted
def gen_data(subject: str, course: int, mode: Course_Data_Mode, year: str, values: Value_Data_Mode,  output_mode, show_nums, reg_fac_only) :
    output_dict = {}
    ctr_dict = {}
    reg_fac = []


    # check to see if output.csv exists and if it does build the regular faculty dictionary
    if reg_fac_only:
        try:
            # open file and use python csv import to take care of reading csv file
            with open('output.csv', mode= "r", encoding="latin-1") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # print(row["IS_FACULTY"])
                    if row["IS_FACULTY"] == "1":
                        reg_fac.append(row["NAME"])
        except IOError as e:
            print(f"Faculty list retrieval error. Couldn't read output.csv ({e}). Have you run the webscraper?")
            print("Proceeding as if all faculty is selected. ")
    # print(reg_fac)
    # open file and use python csv import to take care of reading csv file
    with open('data.csv', mode= "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            # print(row["TERM"][:4] +" is "+ year)
            # break
            # if row["TERM"][:4] == year:

            # check for the year
            if year in row["TERM_DESC"] or year == "*":
                # print("year pass")
                # print(row["SUBJ"] +"is" +subject)
                # check for subject
                if row["SUBJ"] == subject:
                    # print("subj pass")
                    # print("MATCH!" + row["SUBJ"] +":" +row["NUMB"])
                    #check the data mode if it does not meet criteria move on to next entry
                    if mode == Course_Data_Mode.SINGLE_COURSE:
                        if row["NUMB"] != course:
                            continue # does not meet criteria
                    elif mode == Course_Data_Mode.COURSE_LEVEL:
                        if row["NUMB"][:1] != course[:1]:
                            continue # does not meet criteria
                    elif mode != Course_Data_Mode.DEPARTMENT:
                        continue # neither of the above

                    prof = row["INSTRUCTOR"]
                    # use the data from output.csv
                    if reg_fac_only:
                        # splits  = prof.split()
                        # if splits[0][-1] == ',':
                        #     splits[0] = splits[0][:-1]
                        b = False
                        # try to match the prof name for the course and find it in the CSV. if we cant find it then move
                        # onto next course
                        for s in reg_fac:
                            splits2 = s.split()
                            # print(splits)
                            # print(splits2)
                            # First M Last
                            # Last, First M
                            if splits2[0] in prof and splits2[-1] in prof:
                                b= True
                                break

                        if not b:
                            continue

                    # if we get to this point then we meet the criteria


                    # store class name if this mode is selected
                    if output_mode == "Class":
                        prof = row["NUMB"]


                    
                    print("storing info on Prof. " + prof +" for course "+row["SUBJ"]+" "+row["NUMB"]+" for "+row["TERM_DESC"])
                    # if its not in the dict than put it in
                    if prof not in output_dict:
                        output_dict[prof] = 0.0
                        ctr_dict[prof] = 0
                    # append the value and counter (for average calc)
                    ctr_dict[prof] += 1
                    output_dict[prof] += proc_row(row, values)


    # compute the average for each prof name / course numb
    for key in output_dict:
        output_dict[key] = output_dict[key] / ctr_dict[key]

    print(f"output_dict: {output_dict}")
    # if not show nums then just return. we're done
    if not show_nums:
        return output_dict
    outdict_2 = {}
    #otherwise add the (X) to each key and return that
    for key in output_dict:
        outdict_2[key + f" ({ctr_dict[key]})"] = output_dict[key]
    
    return outdict_2



