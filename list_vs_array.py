import numpy as np
import sys 

# Python list containing numbers from 1 to 1000
python_list = list(range(1, 1001))

# NumPy array containing numbers from 1 to 1000
numpy_array = np.arange(1, 1001)

print("Python List:")
print(python_list)

print("\nNumPy Array:")
print(numpy_array)
python_list = list(range(1, 1001))

numpy_array = np.arange(1, 1001)

# Memory usage
list_memory = sys.getsizeof(python_list)
array_memory = numpy_array.nbytes

print("\nMemory Usage:")
print("Python List:", list_memory, "bytes")
print("NumPy Array:", array_memory, "bytes")

sys.getsizeof(python_list)
numpy_array.nbytes

import time

def compare_addition_speed():
    # Create list and NumPy array
    python_list = list(range(10000))
    numpy_array = np.arange(10000)

    # Python list addition
    start_time = time.time()

    list_result = [x + 5 for x in python_list]

    end_time = time.time()
    list_time = end_time - start_time

    # NumPy array addition
    start_time = time.time()

    array_result = numpy_array + 5

    end_time = time.time()
    array_time = end_time - start_time

    # Print results
    print("\nAddition Speed:")
    print("Python List Time:", list_time, "seconds")
    print("NumPy Array Time:", array_time, "seconds")
# Zomato-style restaurant ratings

ratings = [4.1, 3.8, 4.5, 4.0, 3.5]

# Using a for-loop
loop_result = []

for rating in ratings:
    loop_result.append(rating * 2)

print("\nRatings using for-loop:")
print(loop_result)

# Using NumPy vectorization
ratings_array = np.array(ratings)

vectorized_result = ratings_array * 2

print("\nRatings using NumPy vectorization:")
print(vectorized_result)