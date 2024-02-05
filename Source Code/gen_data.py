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
    PERC_BS="bprec"
    PERC_CS="cprec"
    PERC_DS="dprec"
    PERC_FS="fprec"
    PERC_D_AND_PERC_F="D/F"



#helper function for gen_data
def proc_row(row: dict, mode: Value_Data_Mode):
    if mode is not Value_Data_Mode.PERC_D_AND_PERC_F:
        return float(row[mode.value])
    elif mode is Value_Data_Mode.PERC_D_AND_PERC_F:
        return (float(row[Value_Data_Mode.PERC_DS.value])+float(row[Value_Data_Mode.PERC_FS.value]))

# generate data for graph
# params:
# subject - the subject of the course. For example MATH
# course -  the subject code for the course. For example 251
# mode - the data criteria mode. For example SINGLE_COURSE
#    If you choose mode COURSE_LEVEL, then the first digit of the string will determine the level
#    If you choose mode DEPARTMENT, then the value of course will be ignored
# year - the years you want to search. For example, "2015 2016"
#   You can put a single year (e.g. "2014"),
#   multiple years (e.g. "2014 2016"),
#   or an asterix for all years (e.g. "*.")
# values -  what values do you want to retrieve. What do tou want to measure? For example, PERC_AS
#   PERC_D_AND_PERC_F will compound the nonpassing grades D + F
# output_mode - what you want the keys in the return dict to be. Either PROF_NAME (default) or CLASS_NUM.
# show_nums - put the number of coures in the key for the dictionary in the format PROF_NAME (NUM). Either True or False (default)
# reg_fac_only - show only regular faculty. output.csv must exist or else nothing will be returned. Either True or False (default(
# return:
# a dict in the format {string : float} {PROFESSOR_NAME : METRIC} or {CLASS_NUM : METRIC}.
# the values in the dictionary will be averaged for every class the professor teaches
# the dictionary will be unsorted
def gen_data(subject: str, course: int, mode: Course_Data_Mode, year: str, values: Value_Data_Mode,  output_mode, show_nums = False, reg_fac_only = False) :
    output_dict = {}
    ctr_dict = {}
    reg_fac = []

    if reg_fac_only:
        try:
            with open('output.csv', mode= "r", encoding="utf-8-sig") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    # print(row["IS_FACULTY"])
                    if row["IS_FACULTY"] == "1":
                        reg_fac.append(row["NAME"])
        except IOError as e:
            print(f"Faculty list retrieval error. Couldn't read output.csv ({e}). Have you run the webscraper?")
            print("Proceeding as if all faculty is selected. ")
    # print(reg_fac)
    with open('data.csv', mode= "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row)
            # print(row["TERM"][:4] +" is "+ year)
            # break
            # if row["TERM"][:4] == year:
            if year in row["TERM_DESC"] or year == "*":
                # print("year pass")
                # print(row["SUBJ"] +"is" +subject)
                if row["SUBJ"] == subject:
                    # print("subj pass")
                    # print("MATCH!" + row["SUBJ"] +":" +row["NUMB"])
                    if mode == Course_Data_Mode.SINGLE_COURSE:
                        if row["NUMB"] != course:
                            continue # does not meet criteria
                    elif mode == Course_Data_Mode.COURSE_LEVEL:
                        if row["NUMB"][:1] != course[:1]:
                            continue # does not meet criteria
                    elif mode != Course_Data_Mode.DEPARTMENT:
                        continue # neither of the above

                    prof = row["INSTRUCTOR"]

                    if reg_fac_only:
                        # splits  = prof.split()
                        # if splits[0][-1] == ',':
                        #     splits[0] = splits[0][:-1]
                        b = False
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

                        # meets criteria
                        if output_mode == "Class":
                            prof = row["NUMB"]


                    
                    print("storing info on Prof. " + prof +" for course "+row["SUBJ"]+" "+row["NUMB"]+" for "+row["TERM_DESC"])
                    if prof not in output_dict:
                        output_dict[prof] = 0.0
                        ctr_dict[prof] = 0
                    ctr_dict[prof] += 1
                    output_dict[prof] += proc_row(row, values)



    for key in output_dict:
        output_dict[key] = output_dict[key] / ctr_dict[key]

    print(f"output_dict: {output_dict}")
    if not show_nums:
        return output_dict
    outdict_2 = {}

    for key in output_dict:
        outdict_2[key + f" ({ctr_dict[key]})"] = output_dict[key]
    
    return outdict_2



