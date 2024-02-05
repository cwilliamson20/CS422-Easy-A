# This module serves as the connection between student_interface.py -> gen_data.py -> basicgraph.py
# Author(s): Meagan Beckstrand, Eliza Black, Connie Williamson
# Group 4
# Created 1/29/2024
# Date Last Modified: 2/5/2024
import gen_data
import basicgraph


def get_graph_data(app, root):

    # get the information from the already created UI instance
    options_dict = app.create_dict()
    print(f"options_dict = {options_dict}")

    # Unpacking dictionary values to get graph option values:
    subject_code = options_dict["subject_code"]
    course_number = options_dict["course_number"]

    # Renaming "All" year selection so it is compatible with gen_data functionality
    year = options_dict["year"]
    if year == "All":
        year = "*"

    # Reformatting graph_type input using Enum values compatible with gen_data.py
    course_mode = 0
    if options_dict["graph_type"] == 1:
        course_mode = gen_data.Course_Data_Mode.SINGLE_COURSE
    elif options_dict["graph_type"] == 2:
        course_mode = gen_data.Course_Data_Mode.DEPARTMENT
    elif options_dict["graph_type"] == 3:
        course_mode = gen_data.Course_Data_Mode.COURSE_LEVEL

    # TODO: add options for %Cs, etc
    # Reformatting grade_mode input using Enum values compatible with gen_data.py
    grade_mode = 0
    if options_dict["grade_mode"] == 1:
        grade_mode = gen_data.Value_Data_Mode.PERC_AS
    elif options_dict["grade_mode"] == 2:
        grade_mode = gen_data.Value_Data_Mode.PERC_D_AND_PERC_F

    # Reformatting x_axis input to make compatible with gen_data.py
    x_axis_type = options_dict["x_axis"]
    if x_axis_type == 1:
        x_axis_type = "Class"
    else:
        x_axis_type = "Instructor"


    print(f"x_axis_type = {x_axis_type}")
    print(f"This is the info going into gen_data: {options_dict}")
    graph_dict = gen_data.gen_data(subject_code, course_number, course_mode, year, grade_mode, x_axis_type)
    # graph_dict = gen_data.gen_data("BI", "121", gen_data.Course_Data_Mode.SINGLE_COURSE, "*", gen_data.Value_Data_Mode.PERC_AS)
    print(f"this is what was returned by gen_data: {graph_dict}")

    basicgraph.basic_graph(graph_dict, options_dict)

