#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

def basic_graph(output_dict, options_dict):
    #Extract graph data from output_dict
    x_data = list(output_dict.keys()) #get percentage data from dict
    y_data = list(output_dict.values()) #get professor or class data from dict

    #Read labels for graph
    title = options_dict["TITLE"] 
    y_label = options_dict["PROF"]
    x_label = options_dict["per"]

    #Assign figure size
    fig = plt.figure(figsize = (10, 5))
    #Bar plot
    plt.bar(x_data, y_data, color = blue, width = 0.8, label =, align='center' ) 

    # Add gridlines
    #plt.grid(b = True, color = 'grey', linestyle = '-.', linewidth = 0.5, alpha = 0.2)


    #Add labels
    plt.ylabel(y_label) 
    plt.xlabel(x_label) 
    plt.title(title)

    #Generate graph
    plt.show()
