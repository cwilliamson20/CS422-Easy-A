#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np

#def basic_graph(output_dict, title, y_label, x_label, class_count):
def basic_graph(output_dict, title, y_label, x_label, class_count):
    x_data = list(output_dict.keys()) #get percentage data from dict
    y_data = list(output_dict.values()) #get prof/class data from dict

#    x_data = ['ProfA', 'ProfB', 'ProfC']
#    y_data = [10, 20, 30]
    fig = plt.figure(figsize = (10, 5))
    plt.bar(x_data, y_data) #color = , width = , label = ) 

    plt.ylabel(y_label) 
    plt.xlabel(x_label) 
    plt.title(title)

#    plt.ylabel("Prof")
#    plt.xlabel("Per") 
#    plt.title("graph")

    plt.show()
