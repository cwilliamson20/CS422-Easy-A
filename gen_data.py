import csv
from enum import Enum

class Course_Data_Mode(Enum):
    SINGLE_COURSE = 1
    DEPARTMEMT = 2
    COURSE_LEVEL = 3


class Value_Data_Mode(Enum):
    PERC_AS= "aprec"
    PERC_DFs= "d/F"




def proc_row(row: dict, mode: Value_Data_Mode):
    if mode is not Value_Data_Mode.PERC_DFs:
        return float(row[mode.value])

def gen_data(subject: str, course: int, mode: Course_Data_Mode, year: str, values: Value_Data_Mode) :
    output_dict = {}
    ctr_dict = {}
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
                        if row["NUMB"] == course:
                            prof = row["INSTRUCTOR"]
                            print("storing info on Prof. "+prof)
                            if prof not in output_dict:
                                output_dict[prof] = 0.0
                                ctr_dict[prof] = 0
                            ctr_dict[prof]+=1
                            output_dict[prof]+= proc_row(row,values)



    for key in output_dict:
        output_dict[key] = output_dict[key] / ctr_dict[key]
    return output_dict



