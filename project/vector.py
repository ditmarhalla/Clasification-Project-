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
        value = np.abs(np.subtract(self.vector[:-1],other.vector))
        value = value.sum()
        return value

"""Test


trained_data ='C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\trained.txt'
untraiend_data = 'C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\untrained.txt'

trained_file = np.loadtxt(trained_data,dtype=np.int16)
untrained_file= np.loadtxt(untraiend_data,dtype=np.int16)

for i in range (2):
    for n in range(2):
        vector_trained = Vector(trained_file[i])
        vector_untrained = Vector(untrained_file[n])
        print("This is the distance: ", vector_trained.euclidian_distance(vector_untrained))
        """
