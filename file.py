import time

# File Conversion
def file_to_list(name):
    list_of_data = []                                                  # Create empty list to put the data
    file = open(name,  "r")                                            # Open File to convert "name" is the file name we will recall later
    for line in file:                                                  # Read line by line of file (loop)
        line = tuple(line.split())                                     # For each line removes everything (spaces (\t, enter (\n)) and returns tuples
        list_of_data.append(line)                                      # inseart the converted line into the list we created "list_of_data"
    file.close()                                                       #close the file
    return list_of_data
#########################################################################################################################
# Calculating the distance

def euclidian_distance(vector1, vector2):                              # The two vectors we want to compare
    value = 0                                                          # we start the variable to calculate the sum 
    for i in range(len(vector1)):                                      # The loop will run till the length of "vector 1"
        value += abs(int(vector1[i]) - int(vector2[i]))                # distance calculation
    return value

#########################################################################################################################
# Calculating the untrained vectors class
def find_class(traned_data,  untrained_vector):                        # we will call two data data using the fuction of "euclidian_distance"
    distnace_vector = []                                               # Empty list we will use to store the distance and class
    for vectors in traned_data:                                        # Loop that will run through all the first data (trained) and second (untrained)
        distnace = euclidian_distance(vectors[0:5], untrained_vector)  # and calculate the distance using the fuction we created "Euclidian_distance"
        distnace_vector.append((distnace,vectors[6]))                  # Then adds the "distnace" we found and "class" so that we can use later for comparason
    min_val = distnace_vector[0]                                       # Create a minimal value to use and find the class of our "untrained_vector". We define it as the first array in the "distance_vector" list
    for i in range(len (distnace_vector)):                             # Run through a loop for how many data we hav in "distnace_vector"
        if min_val[0] > (distnace_vector[i][0]):                       # Compare if the value we have si smaller then the next one
            min_val = distnace_vector[i]                               # if this is true we reassigne it and run the loop again. This will give us the smallest distnace possible and the class
    untrained_vector = untrained_vector + tuple(min_val[1])            # After finding the best distance we assigne the class of that distnace to the "untrained_vector"
    return untrained_vector

def class_untrained_vectors(trained_data,untrained_data):
    list_data_untrained = []
    for untrained_vector in untrained_data:
        vector = find_class(trained_data, untrained_vector)
        list_data_untrained.append(vector)
    return list_data_untrained

start = time.time()
# test run with some data
number_of_vectors_untrained = 1000
dataset_trained = file_to_list("trained.txt")                           # Open the untrained data file
dataset_untrained = file_to_list("untrained.txt")
class_untrained_vectors(dataset_trained,dataset_untrained[0:number_of_vectors_untrained]) # we use slices to call the munber of "untrained" vectors we would like to use
stop = time.time()
print('Time: ', stop - start)

input()
