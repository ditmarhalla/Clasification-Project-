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

def euclidian_distance(vector1, vector2):                               # The two vectors we want to compare
    value = 0                                                           # we start the variable to calculate the sum
    for i in range(len(vector1)):                                       # The loop will run till the length of "vector 1"
        value += abs(int(vector1[i]) - int(vector2[i]))                 # distance calculation
    return value


#########################################################################################################################
# Calculating the untrained vectors class
def find_class(traned_data,  untrained_vector):                         # This function recalls the euclidian distance in order to find the class of the untrained vector
    distnace_vector = []                                                # Empty list we will use to store the distance and class
    for vectors in traned_data:                                         # Loop that will run through all the first data (trained) and second (untrained)
        if len(vectors) == 7:
            distnace = euclidian_distance(vectors[0:5], untrained_vector)  # and calculate the distance using the fuction we created "Euclidian_distance"
            distnace_vector.append((distnace,tuple(vectors[6])))               # Then adds the "distnace" we found and "class" so that we can use later for comparason
        elif len(vectors) == 6:
            distnace = euclidian_distance(vectors[0:4],untrained_vector)
            distnace_vector.append((distnace, vectors[5]))              ########## distance is type(int) while vector is type(tuple)
        elif len(vectors) == 5:
            distnace = euclidian_distance(vectors[0:3],untrained_vector)
            distnace_vector.append((distnace, vectors[4]))
        else:
            break
    print(type(distnace_vector[1]))
    min_val = distnace_vector[0]                                        # Create a minimal value to use and find the class of our "untrained_vector". We define it as the first array in the "distance_vector" list
    for i in range(len (distnace_vector)):                              # Run through a loop for how many data we hav in "distnace_vector"
        if min_val[0] > (distnace_vector[i][0]):                        # Compare if the value we have si smaller then the next one
            min_val = distnace_vector[i]                                # if this is true we reassigne it and run the loop again. This will give us the smallest distnace possible and the class
            #print("minval",min_val)
    #print(type(untrained_vector))
    #print(type(min_val[1]))
    untrained_vector = untrained_vector + min_val[1]             # After finding the best distance we assigne the class of that distnace to the "untrained_vector"
    #print ("vectorclass",untrained_vector)
    return untrained_vector


########################################################################################################################
# Finding the class of all the untrained vectors
def class_untrained_vectors(trained_data,untrained_data):     # This function recalls the untrained vectors to find the class (7th value)
    list_data_untrained = []                                            # The list where we will store all the untrained vector after we get the class
    for untrained_vector in untrained_data:                             # Run through the loop for all the untrained vectors
        vector = find_class(trained_data, untrained_vector)   # Recalles the 3rd fucntion "find_class"
        list_data_untrained.append(vector)                              # Appends the untrained vector with the class in the list
    return list_data_untrained


########################################################################################################################
# Remove dimensions to make the algorithm faster
def remove_dimension(data,dimension):                                   # Romves a comumn of data we specify using "dimension" to select it
    vectors = file_to_list(data)
    new_data = []
    for vector in vectors:
        vector = vector[:dimension-1]+ vector[dimension:]               # To remove the dimensions we use slices to remove it since we are using tuples and canot use the comadn "pop"
        new_data.append(vector)
    return new_data


########################################################################################################################
# See the acuracy of the algorithm when we remove the dimension
#def algorithm_accuracy(original_data, reduced_data):
 #   corresponding = 0
  #  not_corresponding = 0
   # for data in list_data_untrained:
    #    if dsdsd == adasd:
     #       corresponding += 1
      #  else:
       #     not_corresponding += 1


start = time.time()
# test run with some data
number_of_vectors_untrained = 10                                     # We use slices to caluclate only the number we would like
dataset_trained = file_to_list("trained.txt")                           # Open the untrained data file
dataset_untrained = file_to_list("untrained.txt")
print(class_untrained_vectors(dataset_trained,dataset_untrained[0:number_of_vectors_untrained])) # we use slices to call the munber of "untrained" vectors we would like to use
#print('Time: ', stop - start)
#trained_data = remove_dimension("trained.txt",2)
#untrained_data = remove_dimension("untrained.txt",2)
#print(class_untrained_vectors(trained_data,untrained_data[0:10]))

stop = time.time()
print('Time: ', stop - start)
