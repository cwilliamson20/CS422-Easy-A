# only scrapes data for professors teaching in Natural Sciences
# Subjects: Biology, Chemistry and Biochemistry, Computer and Information Science, Earth Sciences, General Science Program, 
# Human Physiology, Mathematics, Neuroscience, Physics, and Psychology

import requests    #TODO: list what packages the admin needs to install before installing EasyA
url = 'https://web.archive.org/web/20141107201402/http://catalog.uoregon.edu/arts_sciences/biology/#facultytext'
data = requests.get(url)
print(data.text)
