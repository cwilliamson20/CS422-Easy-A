#!/usr/bin/env python3
import matplotlib.pyplot as plt

def basic_graph(output_dict,options_dict):
    """
    Take the grade data after it has been parsed through and generate a graph.

    Args:
        output_dict (dict): The dictionary containing the grade data, including professor name or class number, and grade the percentage. 
        options_dict (dict): The dictionary containing the selections of the user, used for labeling the graph

    """
    if not output_dict:
        print("Error getting graph data!")
        return


    #Sort the data from output_dict in descending order
    tupled_output = list(output_dict.items())
    sorted_dict = sorted(tupled_output, key = lambda x: x[1], reverse = True)

    
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
    y_data = y_data[:entries]
    x_data = x_data[:entries]
    
    #Read labels for graph
    fig_title = options_dict["course_mode"]  # TODO: fix axis labels and graph title
    
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
    fig, ax = plt.figure(figsize = (10, 5))
    
    #Bar plot
    ax.bar(x_data, y_data, color = 'blue', width=0.7, align='center')
    ax.set_xlim(-0.5, entries)
    ax.set_ylim(0,100)
   
    #Add labels
    ax.set(ylabel=y_label, xlabel=x_label, title=fig_title)
    
    #Rotate x labels
    plt.xticks(rotation=30, ha='center') 


    #Add labels
    #plt.ylabel(y_label) 
    #plt.xlabel(x_label) 
    #plt.title(title)

    #Generate graph
    plt.show()

