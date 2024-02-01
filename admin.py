# created by Etienne



import sys
import verify_data


def print_usage():
    print("usage: ...")
    print(sys.argv)



def main():

    if len(sys.argv) < 2:
        print_usage()
    elif sys.argv[1] == "--verify" or sys.argv[1] == "-V":
        verify_data.main()
    elif sys.argv[1] == "--replace" or sys.argv[1] == "-r":
        print("replacing data")
        if len(sys.argv) < 3:
            print("Usage: python3 admin.py -r <filename>")
        else:
            print(f"Replacing with file {sys.argv[2]}")
    elif sys.argv[1] == "-webscrapper" or sys.argv[1] == "-w":
        print("Running the webscraper and updating faculty list!")
    else:
        print("Invalid arguments!")
        print_usage()














if __name__ == "__main__":
    main()