from vector import Vector
import numpy as np
import time

class Nearest_Neighbour:

    def __init__(self, trained_vector, untrained_vector):
        """Nearest Neighbour is a class that classifies a vector 
        using the 'distance ' method. The classification is made
        using the trained data that have a 7th value. That is the
        class

        Parameters:
            trained_vector: an array of data of length n+1
            untrained_vector: an array of data of length n

        Method:     distance"""
        self.trained_vector = Vector(trained_vector)
        self.untrained_vector = Vector(untrained_vector)
        

    def distance(self):
        """Clasifie the untrained arrays in the dataset using the method
        'euclidian distnace' from the 'Vector' class.

        Parameters: trained and untraiend dataset called from the
        Nearest Neighbour class"""
        distance_vector = []
        distance = np.array([(train[-1:],self.untrained_vector.euclidian_distance(train)) for train in self.trained_vector.vector],dtype=np.uint16)
        distance_vector.append(distance)

        base = distance_vector[0][0]
        for n in range(len(distance_vector[0])):
            if base[1] > (distance_vector[0][n][1]):
                base = distance_vector[0][n]          

        classified_vector =np.array(np.append(self.untrained_vector.vector,base[0]),dtype=np.uint16)
        return classified_vector
