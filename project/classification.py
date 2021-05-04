from vector import Vectors

class Classification:
    def __init__(self, trained_vector, untrained_vector):
        """Initiate a classification by calling the vectors class """
        self.vector = Vectors(trained_vector, untrained_vector)
        self.classification = []

    def distance_method(self):
        distance_vector = []
        tvectors = self.vector.tvector
        uvectors = self.vector.uvector
        print("this is tvecotr ",tvectors)
        print("this is uvecotr ",uvectors)
        if len(tvectors) == 7:
            test = self.vector.euclidian_distance(5)
            distance_vector.append((uvectors, tvectors[6]))              # Then adds the "distance" we found and "class" so that we can use later for comparison

        if len(tvectors) == 6:
            test = self.vector.euclidian_distance(4)
            distance_vector.append((uvectors, tvectors[5]))              # Then adds the "distance" we found and "class" so that we can use later for comparison

        if len(tvectors) == 5:
            test = self.vector.euclidian_distance(3)
            distance_vector.append((uvectors, tvectors[4]))              # Then adds the "distance" we found and "class" so that we can use later for comparison

        print ("this is the distance",test)
        print("This is the vector", distance_vector)

        min_val = distance_vector[0]                                        # Create a minimal value to use and find the class of our "untrained_vector". We define it as the first array in the "distance_vector" list
        for n in range(len(distance_vector)):                               # Run through a loop for how many data we hav in "distance_vector"
            if min_val[0] > (distance_vector[n][0]):                        # Compare if the value we have is smaller then the next one
                min_val = distance_vector[n]                                # if this is true we re-assign it and run the loop again. This will give us the smallest distance possible and the class
        untrained_vector = list(uvectors)                           #######  try using t = ('A',) + t[1:] instead of converting it to a list #########
        untrained_vector.append(min_val[1])                                 # After finding the best distance we assign the class of that distance to the "untrained_vector"
        untrained_vector = tuple(untrained_vector)
        return untrained_vector



"""

    def distance_method(self):
        distance_vector = []
        tvectors = self.vector.tvector
        uvectors = self.vector.uvector
        if len(tvectors) == 7:
            distance = self.vector.euclidian_distance[0:5]()
            distance_vector.append((distance, vector[6]))              # Then adds the "distance" we found and "class" so that we can use later for comparison
        elif len(vector) == 6:
            distance = self.vector.euclidian_distance[0:4]()
            distance_vector.append((distance, vector[5]))
        elif len(vector) == 5:
            distance = self.vector.euclidian_distance[0:3]()
            distance_vector.append((distance, vector[4]))

        min_val = distance_vector[0]                                        # Create a minimal value to use and find the class of our "untrained_vector". We define it as the first array in the "distance_vector" list
        for n in range(len(distance_vector)):                               # Run through a loop for how many data we hav in "distance_vector"
            if min_val[0] > (distance_vector[n][0]):                        # Compare if the value we have is smaller then the next one
                min_val = distance_vector[n]                                # if this is true we re-assign it and run the loop again. This will give us the smallest distance possible and the class
        untrained_vector = list(uvectors)                           #######  try using t = ('A',) + t[1:] instead of converting it to a list #########
        untrained_vector.append(min_val[1])                                 # After finding the best distance we assign the class of that distance to the "untrained_vector"
        untrained_vector = tuple(untrained_vector)
        return untrained_vector
        """

def file_to_list(name):
    list_of_data = []                                                  # Create empty list to put the data
    file = open(name,  "r")                                            # Open File to convert "name" is the file name we will recall later
    for line in file:                                                  # Read line by line of file (loop)
        line = tuple(line.split())                                     # For each line removes everything (spaces (\t, enter (\n)) and returns tuples
        list_of_data.append(line)                                      # insert the converted line into the list we created "list_of_data"
    file.close()                                                       # close the file
    return list_of_data

tdata ='C:\\Users\\Ditmar\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\trained.txt'
udata = 'C:\\Users\\Ditmar\\\Desktop\\University\\2 Semester\\Introduction to Programing\\Clasification-Project-\\untrained.txt'

dataset_trained = file_to_list(tdata)                               # Open the untrained data file
dataset_untrained = file_to_list(udata)
number_of_vectors = 2

for i in range (number_of_vectors):
    for n in range(number_of_vectors):
        classification = Classification(dataset_trained[i],dataset_untrained[i])
        print("This is the distance final : ",classification.distance_method())
