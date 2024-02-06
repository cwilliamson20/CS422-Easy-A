# This module interacts with matplotlib and outputs graphs
# Author(s): Meagan Beckstrand, Connie Williamson 
# Group 4
# Created 1/25/2024
# Date Last Modified: 2/4/2024
import matplotlib.pyplot as plt
import student_interface


def basic_graph(output_dict,options_dict):
    """
    Take the grade data after it has been parsed through and generate a graph.

    Args:
        output_dict (dict): The dictionary containing the grade data, including professor name or class number, and grade the percentage. 
        options_dict (dict): The dictionary containing the selections of the user, used for labeling the graph
    """
    if not output_dict:
        print("No data in the database fits the given criteria.")
        student_interface.show_popup("No data in the database fits the given criteria.")

        return
    
    #Sort the data from output_dict in descending order
    tupled_output = list(output_dict.items())
    sorted_output = sorted(tupled_output, key=lambda x: x[1])

    #Get graph data on professor/class names
    x_data = [x[0] for x in sorted_output]
    #Get graph data on grade percentages
    y_data = [x[1] for x in sorted_output]

    #Determine the number of entries in graph
    entries_len = len(sorted_output) if len(sorted_output) < 5 else 5
    entries = entries_len
    
    #Get the top 5 data entries by percentage
    y_data = y_data[-entries:]
    x_data = x_data[-entries:]
    
    #Read labels for graph
    title = "EasyA" 
    
    # determine y label by if its %As or not
    if options_dict["grade_mode"] == 1:
        y_label = "% As"
    else:
        y_label = "% Ds and Fs"
    
    #if showing class count, update x label
    if options_dict["x_axis"] == 1:
        x_label = "Class"
    else:
        x_label = "Instructor"


    #Assign figure size
    fig = plt.figure(figsize = (10, 5))
    
    #add dotted lines at 20% marks for readability
    for interval in range(20, 100, 20):
        plt.axhline(y=interval, color = 'gray', linestyle='--')

    #Bar plot
    plt.bar(x_data, y_data, color = 'blue', width = .5, align='center' ) 
    plt.ylim(0, 100)
    
    #Rotate x labels
    plt.xticks(rotation=-90) 

    #Add labels
    plt.ylabel(y_label) 
    plt.xlabel(x_label) 
    plt.title(title)

    #make bottom margin larger
    fig.tight_layout()

    #Generate graph
    plt.show()

