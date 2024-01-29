import csv
import os

#data for this list comes from the scraper. Created separately for ease of testing and so scraper isnt run every time you want to test this. 
faculty_names = [('Yashar Ahmadian', 'Biology'), ('Alice Barkan', 'Biology'), ('Brendan J. M. Bohannan', 'Biology'), ('Bruce A. Bowerman', 'Biology'), ('William E. Bradshaw', 'Biology'), ('Scott D. Bridgham', 'Biology'), 
    ('Mark C. Carrier', 'Biology'), ('John S. Conery', 'Biology'), ('William A. Cresko', 'Biology'), ('Alan Dickman', 'Biology'), ('Chris Q. Doe', 'Biology'), ('Judith S. Eisen', 'Biology'), ('Richard B. Emlet', 'Biology'), 
    ('Jessica L. Green', 'Biology'), ('Karen J. Guillemin', 'Biology'), ('Victoria Herman', 'Biology'), ('Janet Hodder', 'Biology'), ('Cristin L. Hulslander', 'Biology'), ('Santiago Jaramillo', 'Biology'), ('Eric A. Johnson', 'Biology'), 
    ('Alan J. Kelly', 'Biology'), ('Diana E. Libuda', 'Biology'), ('Shawn R. Lockery', 'Biology'), ('V. Patteson Lombardi', 'Biology'), ('Svetlana Maslakova', 'Biology'), ('Cristopher M. Neill', 'Biology'), ('Peter M. O’Day', 'Biology'), 
    ('Patrick C. Phillips', 'Biology'), ('John H. Postlethwait', 'Biology'), ('Anne Powell', 'Biology'), ('Jana Prikryl', 'Biology'), ('William Roberts', 'Biology'), ('Bitty A. Roy', 'Biology'), ('Debbie Schlenoff', 'Biology'), ('Eric Selker', 'Biology'), 
    ('Alan Shanks', 'Biology'), ('George F. Sprague Jr.', 'Biology'), ('Karen U. Sprague', 'Biology'), ('Kryn Stankunas', 'Biology'), ('Carl A. Stiefbold', 'Biology'), ('Matthew A. Streisfeld', 'Biology'), ('Terry Takahashi', 'Biology'), 
    ('Nathan J. Tublitz', 'Biology'), ('George R. von Dassow', 'Biology'), ('Philip E. Washbourne', 'Biology'), ('Janis C. Weeks', 'Biology'), ('Monte Westerfield', 'Biology'), ('Peter B. Wetherwax', 'Biology'), ('A. Michelle Wood', 'Biology'), 
    ('Craig M. Young', 'Biology'), ('Steven S. Rumrill', 'Biology'), ('David H. Wagner', 'Biology'), ('Andrew S. Bajer', 'Biology'), ('Howard T. Bonnett Jr.', 'Biology'), ('Roderick A. Capaldi', 'Biology'), ('George C. Carroll', 'Biology'),
    ('Richard W. Castenholz', 'Biology'), ('Charles B. Kimmel', 'Biology'), ('Frederick W. Munz', 'Biology'), ('Paul P. Rudy', 'Biology'), ('Eric Schabtach', 'Biology'), ('Lynda P. Shapiro', 'Biology'), ('Franklin W. Stahl', 'Biology'), ('Nora B. Terwilliger', 'Biology'), 
    ('Daniel Udovic', 'Biology'), ('Norman K. Wessells', 'Biology'), ('James A. Weston', 'Biology'), ('Herbert P. Wisner', 'Biology'), ('Shannon W. Boettcher', 'Chemistry and Biochemistry'), ('Jeffrey A. Cina', 'Chemistry and Biochemistry'), 
    ('Victoria J. De Rose', 'Chemistry and Biochemistry'), ('Kenneth M. Doxsee', 'Chemistry and Biochemistry'), ('Deborah B. Exton', 'Chemistry and Biochemistry'), ('Marina G. Guenza', 'Chemistry and Biochemistry'), ('Julie A. Haack', 'Chemistry and Biochemistry'), 
    ('Michael M. Haley', 'Chemistry and Biochemistry'), ('Diane K. Hawley', 'Chemistry and Biochemistry'), ('Darren W. Johnson', 'Chemistry and Biochemistry'), ('David C. Johnson', 'Chemistry and Biochemistry'), ('Michael E. Kellman', 'Chemistry and Biochemistry'), 
    ('Michael Koscho', 'Chemistry and Biochemistry'), ('Andrew H. Marcus', 'Chemistry and Biochemistry'), ('George V. Nazin', 'Chemistry and Biochemistry'), ('Brad J. Nolen', 'Chemistry and Biochemistry'), ('Catherine J. Page', 'Chemistry and Biochemistry'), 
    ('Michael D. Pluth', 'Chemistry and Biochemistry'), ('Kenneth E. Prehoda', 'Chemistry and Biochemistry'), ('James Prell', 'Chemistry and Biochemistry'), ('Geraldine L. Richmond', 'Chemistry and Biochemistry'), ('Tom H. Stevens', 'Chemistry and Biochemistry'), 
    ('David R. "Randy" Sullivan', 'Chemistry and Biochemistry'), ('David R. Tyler', 'Chemistry and Biochemistry'), ('Gregory M. Williams', 'Chemistry and Biochemistry'), ('Cathy Wong', 'Chemistry and Biochemistry'), ('John Hardwick', 'Chemistry and Biochemistry'), 
    ('Ralph J. Barnhard', 'Chemistry and Biochemistry'), ('Bruce P. Branchaud', 'Chemistry and Biochemistry'), ('Frederick W. Dahlquist', 'Chemistry and Biochemistry'), ('Thomas R. Dyke', 'Chemistry and Biochemistry'), ('O. Hayes Griffith', 'Chemistry and Biochemistry'), 
    ('David R. Herrick', 'Chemistry and Biochemistry'), ('John F. W. Keana', 'Chemistry and Biochemistry'), ('James W. Long', 'Chemistry and Biochemistry'), ('Robert M. Mazo', 'Chemistry and Biochemistry'), ('Peter H. von Hippel', 'Chemistry and Biochemistry'), 
    ('Zena M. Ariola', 'Computer and Information Science'), ('Hank Childs', 'Computer and Information Science'), ('Dejing Dou', 'Computer and Information Science'), ('Stuart Faulk', 'Computer and Information Science'), ('Stephen F. Fickas', 'Computer and Information Science'), 
    ('Kathleen Freeman Hennessy', 'Computer and Information Science'), ('Michael Hennessy', 'Computer and Information Science'), ('Anthony J. Hornof', 'Computer and Information Science'), ('Jun Li', 'Computer and Information Science'), ('Daniel Lowd', 'Computer and Information Science'),
    ('Allen D. Malony', 'Computer and Information Science'), ('Reza Rejaie', 'Computer and Information Science'), ('Joseph Sventek', 'Computer and Information Science'), ('Dave Wilkins', 'Computer and Information Science'), ('Eric D. Wills', 'Computer and Information Science'),
    ('Christopher B. Wilson', 'Computer and Information Science'), ('Xiaodi Wu', 'Computer and Information Science'), ('Sarah A. Douglas', 'Computer and Information Science'), ('Arthur M. Farley', 'Computer and Information Science'), 
    ('Virginia M. Lo', 'Computer and Information Science'), ('Eugene M. Luks', 'Computer and Information Science'), ('Andrzej Proskurowski', 'Computer and Information Science'), ('Jeffrey Stolet', 'Computer and Information Science'), 
    ('Joseph W. Thornton', 'Computer and Information Science'), ('Don M. Tucker', 'Computer and Information Science'), ('Ilya N. Bindeman', 'Earth Sciences'), ('Rebecca J. Dorsey', 'Earth Sciences'), ('Thomas Giachetti', 'Earth Sciences'), 
    ('Emilie Hooft Toomey', 'Earth Sciences'), ('Eugene D. Humphreys', 'Earth Sciences'), ('Qusheng Jin', 'Earth Sciences'), ('A. Dana Johnston', 'Earth Sciences'), ('Leif A. Karlstrom', 'Earth Sciences'), ('Marli B. Miller', 'Earth Sciences'), 
    ('Mark H. Reed', 'Earth Sciences'), ('Alan W. Rempel', 'Earth Sciences'), ('Gregory J. Retallack', 'Earth Sciences'), ('Joshua J. Roering', 'Earth Sciences'), ('David A. Sutherland', 'Earth Sciences'), ('Douglas R. Toomey', 'Earth Sciences'), 
    ('Paul J. Wallace', 'Earth Sciences'), ('James M. Watkins', 'Earth Sciences'), ('Ray J. Weldon', 'Earth Sciences'), ('Katharine V. Cashman', 'Earth Sciences'), ('David Krinsley', 'Earth Sciences'), ('John M. Logan', 'Earth Sciences'), 
    ('John Donovan', 'Earth Sciences'), ('Dennis K. Fletcher', 'Earth Sciences'), ('James Palandri', 'Earth Sciences'), ('Sam Boggs', 'Earth Sciences'), ('M. Allan Kays', 'Earth Sciences'), ('Alexander R. McBirney', 'Earth Sciences'), ('William N. Orr', 'Earth Sciences'), 
    ('Jack M. Rice', 'Earth Sciences'), ('Norman M. Savage', 'Earth Sciences'), ('Harve S. Waff', 'Earth Sciences'), ('Daniel Weill', 'Earth Sciences'), ('Li-Shan Chou', 'Human Physiology'), ('Anita Christie', 'Human Physiology'), ('Brian Dalton', 'Human Physiology'),
    ('Sierra Dawson', 'Human Physiology'), ('Hans Dreyer', 'Human Physiology'), ('Michael Hahn', 'Human Physiology'), ('John Halliwill', 'Human Physiology'), ('Robin Hopkins', 'Human Physiology'), ('Adrianne Huxtable', 'Human Physiology'),
    ('Andrew Karduna', 'Human Physiology'), ('Andrew Lovering', 'Human Physiology'), ('Philip Matern', 'Human Physiology'), ('Carrie McCurdy', 'Human Physiology'), ('Christopher Minson', 'Human Physiology'), ('Jon Runyeon', 'Human Physiology'), 
    ('John Brandon', 'Human Physiology'), ('Alice Callahan', 'Human Physiology'), ('Mark Chesnutt', 'Human Physiology'), ('Michael Colasurdo', 'Human Physiology'), ('Dennis Collis', 'Human Physiology'), ('Mathews Fish', 'Human Physiology'),
    ('Daniel Fitzpatrick', 'Human Physiology'), ('Eben Futral', 'Human Physiology'), ('Igor Gladstone', 'Human Physiology'), ('Randall Goodman', 'Human Physiology'), ('Stanley James', 'Human Physiology'), ('Brian Jewett', 'Human Physiology'), 
    ('Donald Jones', 'Human Physiology'), ('Sungwoo Kang', 'Human Physiology'), ('Paul Kaplan', 'Human Physiology'), ('Vern Katz', 'Human Physiology'), ('Peter Kosek', 'Human Physiology'), ('Brett "Brick" Lantz', 'Human Physiology'),
    ('Samuel Lau', 'Human Physiology'), ('Victor Lin', 'Human Physiology'), ('Kimber Mattox', 'Human Physiology'), ('John Melton', 'Human Physiology'), ('Jennifer Miner', 'Human Physiology'), ('Brian Nichols', 'Human Physiology'), 
    ('Richard Padgett', 'Human Physiology'), ('Joshua Pfeiffer', 'Human Physiology'), ('Matthew Shapiro', 'Human Physiology'), ('Kenneth M. Singer', 'Human Physiology'), ('Kimberly Terrell', 'Human Physiology'), ('Brad Wilkins', 'Human Physiology'), 
    ('Louis R. Osternig', 'Human Physiology'), ('Richard K. Troxel', 'Human Physiology'), ('Marjorie Woollacott', 'Human Physiology'), ('Shabnam Akhtari', 'Mathematics'), ('Arkadiy D. Berenstein', 'Mathematics'), ('Boris Botvinnik', 'Mathematics'), 
    ('Marcin Bownik', 'Mathematics'), ('Jonathan Brundan', 'Mathematics'), ('Daniel K. Dugger', 'Mathematics'), ('Peter B. Gilkey', 'Mathematics'), ('Hayden Harker', 'Mathematics'), ('Weiyong He', 'Mathematics'), ('Fred Hervert', 'Mathematics'), 
    ('James A. Isenberg', 'Mathematics'), ('Alexander S. Kleshchev', 'Mathematics'), ('David A. Levin', 'Mathematics'), ('Huaxin Lin', 'Mathematics'), ('Peng Lu', 'Mathematics'), ('Jean B. Nganou', 'Mathematics'), ('Victor V. Ostrik', 'Mathematics'),
    ('N. Christopher Phillips', 'Mathematics'), ('Alexander Polishchuk', 'Mathematics'), ('Michael R. Price', 'Mathematics'), ('Nicholas J. Proudfoot', 'Mathematics'), ('Hal Sadofsky', 'Mathematics'), ('Brad S. Shelton', 'Mathematics'), 
    ('Christopher D. Sinclair', 'Mathematics'), ('Dev P. Sinha', 'Mathematics'), ('Bartlomiej A. Siudeja', 'Mathematics'), ('Craig Tingey', 'Mathematics'), ('Arkady Vaintrob', 'Mathematics'), ('Hao Wang', 'Mathematics'), ('Micah Warren', 'Mathematics'), 
    ('Yuan Xu', 'Mathematics'), ('Benjamin Young', 'Mathematics'), ('Sergey Yuzvinsky', 'Mathematics'), ('Robert M. Solovay', 'Mathematics'), ('Fred C. Andrews', 'Mathematics'), ('Bruce A. Barnes', 'Mathematics'), ('Richard B. Barrar', 'Mathematics'),
    ('Glenn T. Beelman', 'Mathematics'), ('Charles W. Curtis', 'Mathematics'), ('Micheal N. Dyer', 'Mathematics'), ('Robert S. Freeman', 'Mathematics'), ('William M. Kantor', 'Mathematics'), ('Richard M. Koch', 'Mathematics'), 
    ('Shlomo Libeskind', 'Mathematics'), ('Theodore W. Palmer', 'Mathematics'), ('Kenneth A. Ross', 'Mathematics'), ('Gary M. Seitz', 'Mathematics'), ('Allan J. Sieradski', 'Mathematics'), ('Stuart Thomas', 'Mathematics'),
    ('Marie A. Vitulli', 'Mathematics'), ('Marion I. Walter', 'Mathematics'), ('Lewis E. Ward Jr.', 'Mathematics'), ('Jerry M. Wolfe', 'Mathematics'), ('Charles R. B. Wright', 'Mathematics'), ('Yashar Ahmadian', 'Neuroscience'), 
    ('Judith S. Eisen', 'Neuroscience'), ('Clifford Kentros', 'Neuroscience'), ('Charles B. Kimmel', 'Neuroscience'), ('Shawn R. Lockery', 'Neuroscience'), ('Michael Wehr', 'Neuroscience'), ('Monte Westerfield', 'Neuroscience'), 
    ('Marjorie Woollacott', 'Neuroscience'), ('Benjamín Alemán', 'Physics'), ('Dietrich Belitz', 'Physics'), ('Gregory D. Bothun', 'Physics'), ('James E. Brau', 'Physics'), ('Spencer Chang', 'Physics'), ('Timothy Cohen', 'Physics'), ('Eric Corwin', 'Physics'), 
    ('Paul L. Csonka', 'Physics'), ('Nilendra G. Deshpande', 'Physics'), ('Miriam Deutsch', 'Physics'), ('R. Scott Fisher', 'Physics'), ('Raymond E. Frey', 'Physics'), ('Stephen Gregory', 'Physics'), ('Roger Haydock', 'Physics'), ('James N. Imamura', 'Physics'), 
    ('Timothy Jenkins', 'Physics'), ('Stephen D. Kevan', 'Physics'), ('Graham Kribs', 'Physics'), ('Dean W. Livelybrooks', 'Physics'), ('Stephanie Majewski', 'Physics'), ('Brian W. Matthews', 'Physics'), ('Benjamin McMorran', 'Physics'), 
    ('Stanley J. Micklavzina', 'Physics'), ('Jens Nöckel', 'Physics'), ('Raghuveer Parthasarathy', 'Physics'), ('Michael G. Raymer', 'Physics'), ('Stephen J. Remington', 'Physics'), ('James M. Schombert', 'Physics'), ('Brian J. Smith', 'Physics'), 
    ('Davison E. Soper', 'Physics'), ('Daniel Steck', 'Physics'), ('David M. Strom', 'Physics'), ('Richard P. Taylor', 'Physics'), ('John J. Toner', 'Physics'), ('Eric Torrence', 'Physics'), ('Steven J. van Enk', 'Physics'), ('Hailin Wang', 'Physics'), 
    ('Robert Schofield', 'Physics'), ('Nikolai Sinev', 'Physics'), ('Frank Vignola', 'Physics'), ('Bernd Crasemann', 'Physics'), ('Rudolph C. Hwa', 'Physics'), ('Harlan Lefevre', 'Physics'), ('Joel W. McClure Jr.', 'Physics'), ('David K. McDaniels', 'Physics'), 
    ('John T. Moseley', 'Physics'), ('George W. Rayfield', 'Physics'), ('David R. Sokoloff', 'Physics'), ('Robert L. Zimmerman', 'Physics'), ('Jennifer Ablow', 'Psychology'), ('Nicholas Allen', 'Psychology'), ('Holly Arrow', 'Psychology'), ('Dare A. Baldwin', 'Psychology'),
    ('Elliot Berkman', 'Psychology'), ('Paul Dassonville', 'Psychology'), ('Crystal Dehle', 'Psychology'), ('Dagmar Zeithamova Demircan', 'Psychology'), ('Nicole M. Dudukovic', 'Psychology'), ('Caitlin M. Fausey', 'Psychology'), ('Philip A. Fisher', 'Psychology'),
    ('Jennifer J. Freyd', 'Psychology'), ('Gordon C. Nagayama Hall', 'Psychology'), ('Sara D. Hodges', 'Psychology'), ('Christina M. Karns', 'Psychology'), ('Jagdeep Kaur-Bala', 'Psychology'), ('Brice A. Kuhl', 'Psychology'), ('Robert Mauro', 'Psychology'), 
    ('Ulrich Mayr', 'Psychology'), ('Jeffrey Measelle', 'Psychology'), ('Pranjal Mehta', 'Psychology'), ('Louis J. Moses', 'Psychology'), ('Helen Neville', 'Psychology'), ('Jordan Pennefather', 'Psychology'), ('Jennifer Pfeifer', 'Psychology'), 
    ('Gerard Saucier', 'Psychology'), ('Margaret E. Sereno', 'Psychology'), ('Azim Shariff', 'Psychology'), ('Paul Slovic', 'Psychology'), ('Matt Smear', 'Psychology'), ('Sanjay Srivastava', 'Psychology'), ('Don M. Tucker', 'Psychology'), ('Nash Unsworth', 'Psychology'), 
    ('Michael Wehr', 'Psychology'), ('Maureen Zalewski', 'Psychology'), ('Lewis R. Goldberg', 'Psychology'), ('Barbara Gordon-Lickey', 'Psychology'), ('Marvin Gordon-Lickey', 'Psychology'), ('Douglas L. Hintzman', 'Psychology'), ('Ray Hyman', 'Psychology'), 
    ('Carolin Keutzer', 'Psychology'), ('Daniel P. Kimble', 'Psychology'), ('Peter M. Lewinsohn', 'Psychology'), ('Edward Lichtenstein', 'Psychology'), ('Richard Marrocco', 'Psychology'), ('Michael I. Posner', 'Psychology'), ('Mary K. Rothbart', 'Psychology'), 
    ('Myron Rothbart', 'Psychology'), ('Marjorie Taylor', 'Psychology'), ('Robert L. Weiss', 'Psychology')]


#function to adjust name format to make formats between scraped and data.csv the
def adjust_name(original_name):
    if ',' not in original_name:
        return original_name

    last_name, first_and_middle = map(str.strip, original_name.split(',',1))
    first, *middle = first_and_middle.split()
    middle_initials = ' '.join([name[0] + '.' for name in middle])
    
    # Combine the parts into the desired format
    transformed_name = f"{first} {middle_initials} {last_name}"
    
    return transformed_name


# Read data from data.csv into memory
def read_data(file_path):
    name_data = []
    with open(file_path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            original_name = row['INSTRUCTOR']
            adjusted_name = adjust_name(original_name)
            name_data.append((adjusted_name, row))
    return name_data


# Compare data and modify original data.csv
def compare_names(name_data, scraped_data, file_path):
    unmatched_names = set()
    matched_names = set()
    temp_file = 'temp.csv'  # Temporary file for modifications

    with open(temp_file, 'w', newline='') as csvfile:
        field_names = list(name_data[0][1].keys()) + ['is_faculty'] # add is_faculty parameter column
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()

        # Store existing names and set is_faculty for existing rows
        existing_names = set()

        #open data.csv
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader: #for every row in data.csv
                existing_names.add(row['INSTRUCTOR']) 
                
                row['is_faculty'] = 1 if row['INSTRUCTOR'] in [name[0] for name in name_data] else 0 #<--- this is where is_faculty is set for existing rows in csv file


                """In the line above: We set the value is_faculty for existing rows in the csv file. 
                    It basically says: Set row[is_faculty] to 1 if the value of 'INSTRUCTOR' key in the row 
                    dictionary is found within the name_data (name_data being names from the scraper).
                    If it is not found, set the value of is_faculty to 0. 

                    contents of name_data (from scraper) are in a tuple of this format: (name, department)
                
                """
                writer.writerow(row)  # Write existing rows to temp.csv


        # Compare and append unmatched names
        for scraped_row in scraped_data:
            scraped_name = scraped_row[0]
            if scraped_name not in existing_names:
                unmatched_names.add(scraped_name)
                row = {'INSTRUCTOR': scraped_name, 'is_faculty': 1}
                writer.writerow(row)
            else:
                matched_names.add(scraped_name)

    # Replace original data.csv with the modified file
    os.replace(temp_file, file_path)
    return unmatched_names

# Function to print out the number of elements in the unmatched_names set
def display_statistics(unmatched_names):
    print("# of unmatched names: ", len(unmatched_names))


# Get data from data.csv
file_path = 'data.csv'
name_data = read_data(file_path)

# Set scrapedData to the list of faculty names obtained by scraper
scraped_data = faculty_names


unmatched_names = compare_names(name_data, scraped_data, file_path)

# Display statistics
display_statistics(unmatched_names)