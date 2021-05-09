import numpy as np

class Vector:
    """Class for defining defining vector and a method
    called 'euclidian_distance' to calculate the value

    Parameters:
        vectro: an array of data with length n

    Method:     euclidian_distance"""
    def __init__(self,vector):
        self.vector = vector  


    def euclidian_distance(self,other):
        """Method to calculate the difference in value between
        elements of two vectors.

        Formual:
        The formual is a simplifed version of the "Euclidian Distnace"

        value += (n-th element of 1-st vector) - (n-th element of 2-st vector)"""
        value = np.abs(np.subtract(other[:-1],self.vector))
        value = value.sum()
        return value

"""Test

trained_data ='C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\trained.txt'
untraiend_data = 'C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\untrained.txt'

trained_file = np.loadtxt(trained_data,dtype=np.int16)
untrained_file= np.loadtxt(untraiend_data,dtype=np.int16)

vector_untrained = Vector(untrained_file[0])
vector_trained = Vector(trained_file[:5])

for train in vector_trained.vector:
    print("This is the distance: ", vector_untrained.euclidian_distance(train))
    """
