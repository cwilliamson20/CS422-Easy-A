import student_interface
import gen_data
import basicgraph
from tkinter import Tk

"""
TODO: 
- send course_mode as parameter of basicgraph
basicgraph(output_dict, course_mode, options_dict)
"""

def get_graph_data():

    # Create an instance of EasyAUserInterface
    root = Tk()
    user_interface_instance = student_interface.EasyAUserInterface(root)
    options_dict = user_interface_instance.create_dict()

    # Unpacking dictionary values to get graph option values:

    subject_code = options_dict["subject_code"]
    course_number = int(options_dict["course_number"])
    # course_number = 210

    year = options_dict["year"]
    if year == "All":
        year = "*"

    course_mode = 0
    if options_dict["graph_type"] == 1:
        course_mode = gen_data.Course_Data_Mode.SINGLE_COURSE
    elif options_dict["graph_type"] == 2:
        course_mode = gen_data.Course_Data_Mode.DEPARTMENT
    elif options_dict["graph_type"] == 3:
        course_mode = gen_data.Course_Data_Mode.COURSE_LEVEL

    # TODO: add options for %Cs, etc
    grade_mode = 0
    if options_dict["grade_mode"] == 1:
        grade_mode = gen_data.Value_Data_Mode.PERC_AS
    elif options_dict["grade_mode"] == 2:
        grade_mode = gen_data.Value_Data_Mode.PERC_D_AND_PERC_F

    graph_dict = gen_data.gen_data(subject_code, course_number, course_mode, year, grade_mode)

    print(graph_dict)

    # basicgraph.basic_graph(graph_dict, "TITLE", "y_label", "x_label", 10)
    basicgraph.basic_graph(graph_dict, options_dict)

