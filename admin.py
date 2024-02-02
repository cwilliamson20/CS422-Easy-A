# created by Etienne



import sys
import verify_data
import os
import shutil
import webscraper

def print_usage():
    print("usage: python3 admin.py [args..]\n")
    print("-V or --verify\t\t\tverifies the current grade database with the gradedata.js provided by the Daily Emerald System.\n")
    print("-w or --webscraper\t\truns the webscraper and generates the regular faculty list needed for some graph generation.\n")
    print("-r or --replace <filename>\treplace the current database with the one provided. A backup of the old database will be made.\n")
    # print(sys.argv)



def main():
    if len(sys.argv) < 2:
        print_usage()
    elif sys.argv[1] == "--verify" or sys.argv[1] == "-V":
        verify_data.main()
    elif sys.argv[1] == "--replace" or sys.argv[1] == "-r":
        print("Replacing data...")
        if len(sys.argv) < 3:
            print("Usage: python3 admin.py -r <filename>")
        else:
            if os.path.exists("data.csv"):
                print("Backing up file data.csv to data.csv.tmp")
                shutil.copyfile("data.csv", "data.csv.tmp")


            print(f"Replacing data.csv with file {sys.argv[2]}")
            shutil.copyfile(sys.argv[2], "data.csv")
            print("Creating backup file data.csv.old")
            os.replace("data.csv.tmp","data.csv.old")
            print("Done successfully")





    elif sys.argv[1] == "--webscraper" or sys.argv[1] == "-w":
        print("Running the webscraper and updating faculty list!")
        webscraper.run_webscraper_full()
        print("Done!")
    else:
        print("Invalid arguments!")
        print_usage()














if __name__ == "__main__":
    main()