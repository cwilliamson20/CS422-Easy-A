# only scrapes data for professors teaching in Natural Sciences
# Subjects: Biology, Chemistry and Biochemistry, Computer and Information Science, Earth Sciences, General Science,
# Human Physiology, Mathematics, Neuroscience, Physics, and Psychology

import requests    #TODO: list what packages the admin needs to install before installing EasyA
from bs4 import BeautifulSoup
import re

# a list of all urls pointing to the faculty page for the Natural Sciences departments
# each entry is a tuple consisting of (Department Name, url)
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

# this is the url for March 2016 faculty data for the Biology department
url = "https://web.archive.org/web/20160321182426/http://catalog.uoregon.edu:80/arts_sciences/biology/"
data = requests.get(url)    # this uses the requests module to get the HTML code located at the url

# insert the html data into the BeautifulSoup parser
soup = BeautifulSoup(data.text, "html.parser")

# collect all elements with the class name facultylist
scraped_faculty = soup.findAll("p", class_="facultylist")

# use a regex search to get the name, which is always followed by a comma and is at the beginning of each object
# some facultyname objects don"t actually contain names, but in these few instances they don"t contain a comma and won"t match
faculty_names = []
for fac in scraped_faculty:
    # name is a Match object from the regex module
    name = re.search("^[^,]*,", fac.text)

    if name:    # don"t add non-matches to the list
        # add the name in text found in the match to the list of names found so far
        # this also trims the comma left from the regex match using Python string manipulation
        faculty_names.append(name.group()[:-1])




