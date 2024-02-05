# This module serves as the connection between student_interface.py -> gen_data.py -> basicgraph.py
# Author(s): Meagan Beckstrand, Eliza Black, Connie Williamson
# Group 4
# Created 1/29/2024
# Date Last Modified: 2/4/2024
import gen_data
import basicgraph


def get_graph_data(app, root):

    # get the information from the already created UI instance
    options_dict = app.create_dict()

    # Unpacking dictionary values to get graph option values:
    subject_code = options_dict["subject_code"]
    course_number = options_dict["course_number"]
    
    # if course_number doesn't matter (i.e. single department level, whole department)
    # then sub in the department level so gen_data still has class level info from first digit
    if options_dict["graph_type"] != 1:
        course_number = options_dict["department_level"]

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

    # add information about class or instructor level
    x_axis_type = options_dict["x_axis"]
    if x_axis_type == 1:
        x_axis_type = "Class"
    else:
        x_axis_type = "Instructor"

    # should we show the number of classes in a bar in parentheses?
    # yes if in instructor mode, no in class mode
    if x_axis_type == 1: 
        show_nums = True
    else:
        show_nums = False

    # is it all faculty or only regular faculty?
    if options_dict["fac_mode"] == 1:
        reg_fac_only = False
    else:
        reg_fac_only = True

    # get applicable data from database
    graph_dict = gen_data.gen_data(subject_code, course_number, course_mode, year, grade_mode, x_axis_type, show_nums, reg_fac_only)

    basicgraph.basic_graph(graph_dict, options_dict)

