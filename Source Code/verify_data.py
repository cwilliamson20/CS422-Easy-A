# This module verifies that data.csv matches the data in gradedata.js and is a funciton of Administrator Mode
# Author(s): Etienne Casal-Jouaux, Connie Williamson
# Group 4
# Created 1/28/2024
# Date Last Modified: 2/4/2024

import csv
import re
from decimal import *

#parses the file looking for the specfic class, the year/term it was taught, crn, and aprec in the gradedata.js file
# compares it to the given. if it matches then our data is accurate
def look_for_it(cl, yr, crn, jsf, aprec_in):
    mode = 0
    ap = ""

    for line in jsf:
        if mode == 0 and line.startswith(f"    \"{cl}\":"):
            mode=1
            continue

        if mode != 0 and "]" in line:
            mode =0
            continue

        if mode > 1 and "}" in line:
            mode =1
            continue


        if mode == 1:
            if f"\"TERM_DESC\": \"{yr}\"" in line:
                mode +=1
                continue




        if mode == 2:
            if "\"aprec\"" in line:
                regexx = re.findall(r"[-+]?[0-9]*\.?[0-9]+", line)
                ap = regexx[0]
                mode +=1
                continue





        if mode == 3:
            if f"\"crn\": \"{crn}\"" in line:
                mode +=1
                continue





                
        if mode == 4:
            mode =0
            # some changes had to be done here because python float rounds incorrectly.
            # see https://stackoverflow.com/questions/18473563/python-incorrect-rounding-with-floating-point-numbers
            dec = Decimal(ap)
            getcontext().rounding = ROUND_UP
            if round(dec,1).__str__() == ap:
                return True
            else:
                print(f"aprec match failed for {cl} with CRN {crn} taught in {yr}!")
                return False


    print(f"match failed for {cl} with CRN {crn} taught in {yr}!")
    return False


def main():
    dcsv = "data.csv"
    djs = "gradedata.js"
    
    f = open(djs, "r")
    jsf = []
    for ln in f:
        jsf.append(ln)
    f.close()

    i=0
    wr=0
    length = 0
    with open(dcsv, mode= "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)
        length = len(rows)
        for row in rows:
            cl = row["class"]
            yr = row["TERM_DESC"]
            crn = row["CRN"]
            aprec = row["aprec"]
            print(f"looking for {cl} in {yr} with CRN {crn} ({i}/{length-1})")
            if not look_for_it(cl,yr,crn,jsf, aprec):
                wr += 1
            i += 1
            



    
    print("\n\n\n------")
    print(f"total entries: {length}")
    print(f"bad matches: {wr}")
    print("------")




if __name__ == "__main__":
    main()



