# This module contains the webscraper to scrape Natural Sciences faculty names from the Wayback Machine
# Author(s): Angel Soto, Connie Williamson
# Group 4
# Created 1/18/2024
# Date Last Modified: 2/1/2024

import requests   
from bs4 import BeautifulSoup
import re
from discresolution import begin_resolution #import begin_resolution from discresolution.py to be able to use the discrepancy resolution process
def run_webscraper_full():
    # a list of all urls pointing to the faculty page for the Natural Sciences departments
    # each entry is a tuple consisting of (Department Name, url)
    # Note: General Science does not contain faculty names at the time of writing, but is included for consistency and in case that changes in the future
    urls = [
        ("Biology", "https://web.archive.org/web/20160321182426/http://catalog.uoregon.edu:80/arts_sciences/biology/"),
        ("Chemistry and Biochemistry", "https://web.archive.org/web/20161003083410/http://catalog.uoregon.edu/arts_sciences/chemistry/"),
        ("Computer and Information Science", "https://web.archive.org/web/20160917011026/http://catalog.uoregon.edu/arts_sciences/computerandinfoscience/"),
        ("Earth Sciences", "https://web.archive.org/web/20161016044139/http://catalog.uoregon.edu/arts_sciences/geologicalsciences/"),
        ("General Science", "https://web.archive.org/web/20161003081936/http://catalog.uoregon.edu/arts_sciences/generalscience/"),
        ("Human Physiology", "https://web.archive.org/web/20161003083732/http://catalog.uoregon.edu/arts_sciences/humanphysiology/"),
        ("Mathematics", "https://web.archive.org/web/20161020064848/http://catalog.uoregon.edu/arts_sciences/mathematics/"),
        ("Neuroscience", "https://web.archive.org/web/20161016060405/http://catalog.uoregon.edu/arts_sciences/neuroscience/"),
        ("Physics", "https://web.archive.org/web/20161003084126/http://catalog.uoregon.edu/arts_sciences/physics/"),
        ("Psychology", "https://web.archive.org/web/20161203073058/http://catalog.uoregon.edu/arts_sciences/psychology/")
    ]

    # faculty names is the end product of the web scraper. After running the loop to scrape each department page,
    # it will be filled with tuples of the form (Instructor Name, Department Name)
    faculty_names = []

    # track how many names are added for each department
    scraped_names_stats = {}

    # use a loop to scrape each page for faculty names
    for department_index in range(0, len(urls)):
        url = urls[department_index][1]
        data = requests.get(url)    # this uses the requests module to get the HTML code located at the url
        scraped_names_stats[urls[department_index][0]] = 0  # set intial found name count to 0 for each department

        # insert the html data into the BeautifulSoup parser
        soup = BeautifulSoup(data.text, "html.parser")

        # collect all elements with the class name facultylist
        scraped_faculty = soup.findAll("p", class_="facultylist")

        # use a regex search to get the name, which is always followed by a comma and is at the beginning of each object
        # some facultyname objects don"t actually contain names, but in these few instances they don"t contain a comma and won"t match
        for fac in scraped_faculty:
            # name is a Match object from the regex module
            name = re.search("^[^,]*,", fac.text)

            if name:    # don"t add non-matches to the list
                # add the name in text found in the match to the list of names found so far
                # this also trims the comma left from the regex match using Python string manipulation
                # the second element in the tuple is the department name for use in other parts of the application
                faculty_names.append((name.group()[:-1], urls[department_index][0]))
                # add one to the found name count for this department
                scraped_names_stats[urls[department_index][0]] += 1


    """------------------------BEGIN DISCREPANCY RESOLUTION------------------------"""
    begin_resolution(faculty_names) # call resolution function from discresolution.py