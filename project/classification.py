from vector import Vectors


class Classification:
    """Represents a function that can compare one untrained vector to all the trained
    vectors. Then we compare all the distances that the untrained vector has with the
    trained vectors. The one with which the untrained has the lowest distance we get
    its classification and appoint it to the untrained vector"""
    def __init__(self, vector, the_class):
        """Initiate a classification by calling the vectors class """
        self.vector = Vectors(vector, the_class)
        self.classification = []

    def distance_method(self, other):
        distance_vector = []
        vectors = self.vector.tvector
        print(vectors)
        for vector in vectors:
            print("this is vector",vector)
            print("This is the length of the vector",len(vector))
            if len(vector) == 7:
                distance = self.vector.euclidian_distance[0:5](other)
                distance_vector.append((distance, vector[6]))              # Then adds the "distance" we found and "class" so that we can use later for comparison
            elif len(vector) == 6:
                distance = self.vector.euclidian_distance[0:4](other)
                distance_vector.append((distance, vector[5]))
            elif len(vector) == 5:
                distance = self.vector.euclidian_distance[0:3](other)
                distance_vector.append((distance, vector[4]))
            else:
                break
        min_val = distance_vector[0]                                        # Create a minimal value to use and find the class of our "untrained_vector". We define it as the first array in the "distance_vector" list
        for n in range(len(distance_vector)):                               # Run through a loop for how many data we hav in "distance_vector"
            if min_val[0] > (distance_vector[n][0]):                        # Compare if the value we have is smaller then the next one
                min_val = distance_vector[n]                                # if this is true we re-assign it and run the loop again. This will give us the smallest distance possible and the class
        untrained_vector = list(other)                           #######  try using t = ('A',) + t[1:] instead of converting it to a list #########
        untrained_vector.append(min_val[1])                                 # After finding the best distance we assign the class of that distance to the "untrained_vector"
        untrained_vector = tuple(untrained_vector)
        return untrained_vector

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


classification = Classification(dataset_trained[0:5],dataset_untrained[0:5])

print(classification.distance_method(dataset_untrained[0:5]))
