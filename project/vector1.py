class Vectors:
    def __init__(self, trained_vector, untrained_vector):
        self.tvector = trained_vector
        self.uvector = untrained_vector

    def euclidian_distance(self):
        value = 0                                                         # we start the variable to calculate the sum
        for vector_1, vector_2 in zip(self.tvector,self.uvector): # The loop will run till the length of "vector 1"
            for value_1,value_2 in zip(vector_1,vector_2):
                value += abs(int(value_1) - int(value_2))
                print ("Value = ", value)
        return value


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

for i in range (10):
    vector = Vectors(dataset_trained[i],dataset_untrained[i])
print("This is the distance: ",vector.euclidian_distance())
