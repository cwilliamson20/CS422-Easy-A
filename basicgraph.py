#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


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
    sorted_dict = sorted(output_dict.items(), key = lambda x: x[1], reverse = True)
    
    #Get graph data on professor/class names
    x_data = list(sorted_dict.keys()) 
    #Get graph data on grade percentages
    y_data = list(sorted_dict.values()) 

    #Determine the number of entries in graph
    entries = 5
    
    #Get the top 5 data entries by percentage
    y_data = y_data[:entries]
    x_data = x_data[:entries]
    
    #Read labels for graph
    title = options_dict["course_mode"]
    y_label = options_dict["grade_mode"]
    x_label = options_dict["x_axis"]
    
    #if showing class count, update x label
    if options_dict["show_class_count"] == True:
        x_label += "(and number of classes taught)"


    #Assign figure size
    fig = plt.figure(figsize = (10, 5))
    
    #Bar plot
    plt.bar(x_data, y_data, color = blue, width = 1, align='center' ) 
    plt.ylim(0, 100)
    
    #Rotate x labels
    plt.xticks(rotation=90) 

    #Add labels
    plt.ylabel(y_label) 
    plt.xlabel(x_label) 
    plt.title(title)

    #Generate graph
    plt.show()

