import time


# File Conversion
def file_to_list(name):
    list_of_data = []                                                  # Create empty list to put the data
    file = open(name,  "r")                                            # Open File to convert "name" is the file name we will recall later
    for line in file:                                                  # Read line by line of file (loop)
        line = tuple(line.split())                                     # For each line removes everything (spaces (\t, enter (\n)) and returns tuples
        list_of_data.append(line)                                      # insert the converted line into the list we created "list_of_data"
    file.close()                                                       # close the file
    return list_of_data


########################################################################################################################
# Calculating the distance

def euclidean_distance(vector1, vector2):                               # The two vectors we want to compare
    value = 0                                                           # we start the variable to calculate the sum
    for n in range(len(vector1)):                                       # The loop will run till the length of "vector 1"
        value += abs(int(vector1[n]) - int(vector2[n]))                 # distance calculation
    return value


########################################################################################################################
# Calculating the untrained vectors class
def find_class(trained_vector, untrained_vector):                       # This function recalls the euclidean distance in order to find the class of the untrained vector
    distance_vector = []                                                # Empty list we will use to store the distance and class
    for vectors in trained_vector:                                      # Loop that will run through all the first data (trained) and second (untrained)
        if len(vectors) == 7:
            distance = euclidean_distance(vectors[0:5], untrained_vector)  # and calculate the distance using the function we created "euclidean_distance"
            distance_vector.append((distance, vectors[6]))              # Then adds the "distance" we found and "class" so that we can use later for comparison
        elif len(vectors) == 6:
            distance = euclidean_distance(vectors[0:4], untrained_vector)
            distance_vector.append((distance, vectors[5]))
        elif len(vectors) == 5:
            distance = euclidean_distance(vectors[0:3], untrained_vector)
            distance_vector.append((distance, vectors[4]))
        else:
            break
    min_val = distance_vector[0]                                        # Create a minimal value to use and find the class of our "untrained_vector". We define it as the first array in the "distance_vector" list
    for n in range(len(distance_vector)):                               # Run through a loop for how many data we hav in "distance_vector"
        if min_val[0] > (distance_vector[n][0]):                        # Compare if the value we have is smaller then the next one
            min_val = distance_vector[n]                                # if this is true we re-assign it and run the loop again. This will give us the smallest distance possible and the class
    untrained_vector = list(untrained_vector)                           #######  try using t = ('A',) + t[1:] instead of conferting it to a list #########
    untrained_vector.append(min_val[1])                                 # After finding the best distance we assign the class of that distance to the "untrained_vector"
    untrained_vector = tuple(untrained_vector)
    return untrained_vector


########################################################################################################################
# Finding the class of all the untrained vectors
def class_untrained_vectors(trained_vectors, untrained_vectors):        # This function recalls the untrained vectors to find the class (7th value)
    list_data_untrained = []                                            # The list where we will store all the untrained vector after we get the class
    for untrained_vector in untrained_vectors:                          # Run through the loop for all the untrained vectors
        vector = find_class(trained_vectors, untrained_vector)          # Re-call the 3rd function "find_class"
        list_data_untrained.append(vector)                              # Appends the untrained vector with the class in the list
    return list_data_untrained


########################################################################################################################
# Remove dimensions to make the algorithm faster
def remove_dimension(data, dimension):                                  # Remove a collum of data we specify using "dimension" to select it
    vectors = file_to_list(data)
    new_data = []
    for vector in vectors:
        if dimension == 0:
            vector = vector[(dimension+1):(len(vector)+1)]
            new_data.append(vector)
        else:
            vector = vector[:dimension-1] + vector[dimension:]          # To remove the dimensions we use slices to remove it since we are using tuples and can not use the command "pop"
            new_data.append(vector)
    return new_data


########################################################################################################################
# See the accuracy of the algorithm when we remove the dimension
def algorithm_accuracy(original_data, reduced_data):                    # Calculating how accurate is the program when we delete one dimension
    corresponding = 0
    not_corresponding = 0
    for n in range(len(original_data)):
        if original_data[n][6] == reduced_data[n][5]:                   # If the "class" is the same we count it as viable
            corresponding += 1
        else:
            not_corresponding += 1
    return(corresponding*100)/(corresponding+not_corresponding)

print ("The program has started calculateing")
print ("-"*100)

start = time.time()
# test run with some data
number_of_vectors_untrained = 1000                                            # We use slices to calculate only the number we would like

# loading original data
dataset_trained = file_to_list("trained.txt")                               # Open the untrained data file
dataset_untrained = file_to_list("untrained.txt")
original = class_untrained_vectors(dataset_trained, dataset_untrained[0:number_of_vectors_untrained])  # we use slices to call the number of "untrained" vectors we would like to use

# Run a loop to delete the dimensions one by one and see the percentage after we remove each dimension
for i in range(0, 6):
    trained_data = remove_dimension("trained.txt", i)
    untrained_data = remove_dimension("untrained.txt", i)
    reduced = class_untrained_vectors(trained_data[0:number_of_vectors_untrained], untrained_data[0:number_of_vectors_untrained])
    print("Accuracy when deleting the", i+1, " dimension: ", algorithm_accuracy(original, reduced), "%")

    stop1 = time.time()
    print('Time it takes to calculate the ', i+1, 'dimension', round(stop1 - start, 1), "seconds")
stop2 = time.time()
print('Total time to run the program: ', round(stop2 - start, 1), "seconds")

input("Finished")
