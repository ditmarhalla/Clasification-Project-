import numpy as np

class Vector:
    """Class for defining defining vector and a method
    called 'euclidian_distance' to calculate the value

    Parameters:
        vectro: an array of data with length n

    Method: 
        euclidian_distance
    """

    def __init__(self,vector):
        self.vector = vector  

    def euclidian_distance(self,other):
        """Method to calculate the difference in value between
        elements of two vectors.

        Formual:
        The formual is a simplifed version of the "Euclidian Distnace"

        value += (n-th element of 1-st vector) - (n-th element of 2-st vector) 
        """
        value = 0

        print (self.vector,other.vector)
        value = np.subtract(self.vector[:5],other.vector)
        return value



""" Test
"""
def file_to_list(name):
    list_of_data = []                                                  # Create empty list to put the data
    file = open(name,  "r")                                            # Open File to convert "name" is the file name we will recall later
    for line in file:                                                  # Read line by line of file (loop)
        line = np.array(line)# For each line removes everything (spaces (\t, enter (\n)) and returns tuples
    file.close()                                                       # close the file
    return list_of_data

tdata ='C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\trained.txt'
udata = 'C:\\Users\\Ditmar\\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\untrained.txt'

dataset_trained = file_to_list(tdata)                               # Open the untrained data file
dataset_untrained = file_to_list(udata)

for i in range (3):
    for n in range(1):
        vector_trained = Vector(dataset_trained[i])
        vector_untrained = Vector(dataset_untrained[n])
        print("This is the distance: ", vector_trained.euclidian_distance(vector_untrained))
