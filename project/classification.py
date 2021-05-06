from vector import Vector

class Nearest_Neighbour:

    def __init__(self, trained_vector, untrained_vector, classification = -1):
        """Initiate a classification by calling the vectors class """
        self.trained_vector = Vector(trained_vector)
        self.untrained_vector = Vector(untrained_vector)
        self.classification = classification

    def distance_method(self):
        distance_vector = []
        print("\n\nthis is uvecotr ",self.trained_vector.vector)
        print("this is uvecotr ",self.untrained_vector.vector)

        distance = self.trained_vector.euclidian_distance(self.untrained_vector)
        distance_vector.append((distance, self.trained_vector.vector[-1:]))              

        print ("this is the distance",distance)
        print("This is the vector", distance_vector)

        min_val = distance_vector[0]                                        # Create a minimal value to use and find the class of our "untrained_vector". We define it as the first array in the "distance_vector" list

        print("MINVAL", min_val)
        for n in range(len(distance_vector)):                               # Run through a loop for how many data we hav in "distance_vector"
            if min_val[0] > (distance_vector[n][0]):                        # Compare if the value we have is smaller then the next one
                min_val = distance_vector[n]                                # if this is true we re-assign it and run the loop again. This will give us the smallest distance possible and the class
        self.untrained_vector.vector= list(self.untrained_vector.vector)                           #######  try using t = ('A',) + t[1:] instead of converting it to a list #########
        self.untrained_vector.vector.append(min_val[1])                                 # After finding the best distance we assign the class of that distance to the "untrained_vector"
        self.untrained_vector.vector= tuple(self.untrained_vector.vector)

        print("The is the final form ", self.untrained_vector.vector)
        return self.untrained_vector.vector


    """
    def distance_method(self):
        distance = [(get_classification.classification, self.euclidian_distance(get_classification)) for get_classification in self.untrained_vector.vector]
        distnace = [ (self.trained_vector.euclidian_distance(get_classification), self.trained_vector.vector[-1:]) for get_classification in other]
        distance.sort(key=lambda tup: tup[1]) #sorts the tuple
        self.classification = distance[0][0] #sets the value to the nearest vector
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
number_trained= 2
number_untrained = 2

for i in range (number_trained):
    classification = Nearest_Neighbour(dataset_trained[i],dataset_untrained[i])
    print("FINAL VALUE ",classification.distance_method())
