# This module contains the tkinter UI and methods to kickstart data collection and graph creation when user interacts with the UI
# Author(s): Eliza Black, Connie Williamson
# Group 4
# Created 1/25/2024
# Date Last Modified: 2/4/2024
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import user_create_graph

"""
TODO:
- selection of if you want to show grades per instructor or class 
(class option only works when user selects Single Department Level) 
"""


class EasyAUserInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("EasyA")

        # Set minimum size for main window
        self.root.minsize(500, 300)

        # Create frames for each page
        self.home_frame = Frame(root)
        self.user_frame = Frame(root)
        self.supervisor_frame = Frame(root)

        # Initialize pages
        self.create_home_page()
        self.create_user_page()
        self.create_supervisor_page()

        # Show home page initially
        self.show_home_page()

    def create_home_page(self):
        Label(self.home_frame, text="Welcome to EasyA!").pack()
        Button(self.home_frame, text="Student Mode", command=self.show_user_page).pack()
        default_data_info_string = """The data for EasyA was copied directly from https://emeraldmediagroup.github.io/grade-data/ on 01-16-2024.

Years included: 2013-2016


Limitations:

"If your class doesn't show up here, it means the data was redacted.

Data from 67 percent of the 48,309 classes was redacted by the UO Public Records Office and is not displayed here. Upon inquiry about the removed data, the office cited three conditions which must be met in order to release grade data without violating student privacy via the Family Educational Rights and Privacy Act (FERPA).


The numbers are reflection only of students who received letter grades.


1) The actual class enrollment must be greater than or equal to ten students


2) All students in the class do not receive the same grade.


3) A person would need to figure out the grades of at least six students in the class to deduce the grades of other students. (In other words, a class redacted for this reason — whether a class of 10 or 300 — awarded every student the same grade except for five or fewer students.)


27,013 classes were redacted solely for the first condition. 5,737 classes were redacted because of the second two conditions.

The Emerald omitted the Pass, No Pass and Withdrawls from the data presented in the graphs to display the information in a digestible format."

Source: https://emeraldmediagroup.github.io/grade-data/
"""    
        Label(self.home_frame, text=default_data_info_string).pack()

    def create_user_page(self):

        # Column 1:

        Label(self.user_frame, text="Graph Type:").grid(row=0, column=0, padx=(0, 20), pady=(0, 10))
        # Add radio buttons
        self.var = IntVar()
        self.R1 = Radiobutton(self.user_frame, text="Single Class", variable=self.var, value=1)
        self.R1.grid(row=2, column=0, sticky=W, padx=(0, 20))
        self.R2 = Radiobutton(self.user_frame, text="Single Department", variable=self.var, value=2)
        self.R2.grid(row=3, column=0, sticky=W, padx=(0, 20))
        self.R3 = Radiobutton(self.user_frame, text="Single Department Level", variable=self.var, value=3)
        self.R3.grid(row=4, column=0, sticky=W, padx=(0, 20))

        # Department Level drop-down list
        Label(self.user_frame, text="Department Level:").grid(row=5, column=0, sticky=W, pady=(10, 0))
        self.class_level_box = ttk.Combobox(
            self.user_frame,
            state="readonly",
            values=["100", "200", "300", "400"]
        )
        self.class_level_box.grid(row=6, column=0, sticky=W)

        # Year drop-down list
        Label(self.user_frame, text="Year:").grid(row=7, column=0, sticky=W, pady=(10, 0))
        self.year_box = ttk.Combobox(
            self.user_frame,
            state="readonly",
            values=["All", "2013", "2014", "2015", "2016"]
        )
        self.year_box.grid(row=8, column=0, sticky=W)

        # Subject Code drop-down list
        Label(self.user_frame, text="Course Code:").grid(row=9, column=0, sticky=W, pady=(10, 0))
        self.subject_box = ttk.Combobox(
            self.user_frame,
            state="readonly",
            values=["BI", "CH", "CIS", "GEOL", "HPHY", "MATH", "PHYS", "PSY"] 
        )
        self.subject_box.grid(row=10, column=0, sticky=W)

        # Course Number text box
        Label(self.user_frame, text="Course Number:").grid(row=11, column=0, sticky=W, pady=(10, 0))

        # Create Entry / text box with visible border
        self.course_num_entry = ttk.Entry(self.user_frame, style='TEntry')
        self.course_num_entry.grid(row=12, column=0, sticky=W, pady=(0, 10))

        # Create a style
        style = ttk.Style()

        # Configure style to have a border
        style.configure('TEntry', borderwidth=2, relief="solid")

        # Column 2:
        Label(self.user_frame, text="Display Options:").grid(row=0, column=1, sticky=W, pady=(0, 10))

        # EasyA vs JustPass: radio buttons
        Label(self.user_frame, text="Mode: EasyA vs JustPass").grid(row=2, column=1, sticky=W, pady=(10, 0))
        self.var_grade_mode = IntVar()
        self.r_easya = Radiobutton(self.user_frame, text="EasyA: Show Percent As", variable=self.var_grade_mode, value=1)
        self.r_easya.grid(row=3, column=1, sticky=W, padx=(0, 20))
        self.r_justpass = Radiobutton(self.user_frame, text="JustPass: Show Percent Ds or Fs", variable=self.var_grade_mode, value=2)
        self.r_justpass.grid(row=4, column=1, sticky=W, padx=(0, 20))

        # Display all instructors or just regular faculty
        Label(self.user_frame, text="Instructors To Display:").grid(row=5, column=1, sticky=W, pady=(10, 0))
        self.var_fac = IntVar()
        self.r_all_fac = Radiobutton(self.user_frame, text="Display All Instructors", variable=self.var_fac, value=1)
        self.r_all_fac.grid(row=6, column=1, sticky=W, padx=(0, 20), pady=(10, 0))
        self.r_reg_fac = Radiobutton(self.user_frame, text="Display Only Regular Faculty", variable=self.var_fac, value=2)
        self.r_reg_fac.grid(row=7, column=1, sticky=W, padx=(0, 20))

        # Show grades per instructor or per class: radio buttons
        Label(self.user_frame, text="Show grades per:").grid(row=8, column=1, sticky=W, pady=(10, 0))
        self.var_x_axis = IntVar()
        self.r_per_class = Radiobutton(self.user_frame, text="Class", variable=self.var_x_axis, value=1)
        self.r_per_class.grid(row=9, column=1, sticky=W, padx=(0, 20))
        self.r_per_fac = Radiobutton(self.user_frame, text="Instructor", variable=self.var_x_axis, value=2)
        self.r_per_fac.grid(row=10, column=1, sticky=W, padx=(0, 20), pady=(10, 0))

        # Enter button
        Button(self.user_frame, text="Enter", command=self.enter_graph).grid(row=13, column=1, sticky=W, pady=(30, 0))

        # SET DEFAULT VALUES
        # Radio buttons:
        self.var.set(1)  # Single Class
        self.var_grade_mode.set(1)  # EasyA: Show Percent As
        self.var_fac.set(1)  # Display All Faculty
        self.var_x_axis.set(1)

        # Box selections:
        self.class_level_box.set("100")  # Set default value for department level
        self.year_box.set("All")  # Set default value for year
        self.subject_box.set("BI")  # Set default value for subject codes

    def enter_graph(self):
        user_create_graph.get_graph_data(app, root)

    def create_dict(self):
        # Retrieve selected values from radio buttons, check buttons, and comboboxes

        graph_type = self.var.get()
        grade_mode = self.var_grade_mode.get()
        fac_mode = self.var_fac.get()
        department_level = self.class_level_box.get()
        year = self.year_box.get()
        subject_code = self.subject_box.get()
        course_number = self.course_num_entry.get()
        x_axis = self.var_x_axis.get()

        # Create dictionary with the selected values
        data_dict = {
            "graph_type": graph_type,
            "grade_mode": grade_mode,
            "fac_mode": fac_mode,
            "department_level": department_level,
            "year": year,
            "subject_code": subject_code,
            "course_number": course_number,
            "x_axis": x_axis
        }

        print(f"data_dict = {data_dict}")
        print(f"department_level = {self.class_level_box.get()}")

        return data_dict


    def create_supervisor_page(self):

        # Main Menu button
        main_menu_button = Button(self.root, text="Main Menu", command=self.show_home_page)
        main_menu_button.pack(side=TOP, anchor=NE)

        Label(self.supervisor_frame, text="Supervisor Page").pack()
        Button(self.supervisor_frame, text="Select File", command=self.select_file).pack()

    def show_home_page(self):
        self.hide_frames()
        self.home_frame.pack()

    #def enter_graph(self):
        #Label(self.user_frame, text="Graph data entered").grid(row=6, column=1, sticky=W)

    def show_user_page(self):
        self.hide_frames()
        self.user_frame.pack()

    def show_supervisor_page(self):
        self.hide_frames()
        self.supervisor_frame.pack()

    def hide_frames(self):
        self.home_frame.pack_forget()
        self.user_frame.pack_forget()
        self.supervisor_frame.pack_forget()

    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select a File")
        if file_path:
            print(f"Selected File: {file_path}")

if __name__ == "__main__":
    root = Tk()
    app = EasyAUserInterface(root)
    root.mainloop()


