import numpy as np
import timeit
# List of 10 million integers
num = list(range(1, 10_000_001))

# Basic implementation (for loop)
def sum_of_squares_basic(num):
    result = 0
    for num in num:
        result += num * num
    return result

# Implementation (list comprehension)
def sum_of_squares_listcomp(num):
    return sum([num * num for num in num])

# Optimized (NumPy)
def sum_of_squares_numpy(num):
    arr = np.array(num, dtype=np.int64)
    return np.sum(arr * arr)

# Profiling
setup_code = '''
from __main__ import sum_of_squares_basic, sum_of_squares_listcomp, sum_of_squares_numpy, num
import numpy as np
'''

#Timeit method for each implementation
basic_time = timeit.timeit('sum_of_squares_basic(num)', setup=setup_code, number=10) / 10
listcomp_time = timeit.timeit('sum_of_squares_listcomp(num)', setup=setup_code, number=10) / 10
numpy_time = timeit.timeit('sum_of_squares_numpy(num)', setup=setup_code, number=10) / 10

# Final Profiling results
print("\n--- Profiling Results (average time per run in seconds):\n")
print(f">> List Comprehension: {listcomp_time:.4f} seconds")
print(f">> Basic (for loop): {basic_time:.4f} seconds")
print(f">> Numpy: {numpy_time:.4f} seconds")

#explanation: 
# The GIL lock in python is essentially a mechanism that ensures only one thread runs a Python object and avoids issues such as race conditions. The GIL becomes an issue when doing the sum of squares because each thread has to take turns runnning which can slow it down. To improve this we can use Numpy because it's faster than a standard loop and can do heavy computations faster.
#execution output:
#--- Profiling Results (average time per run in seconds):
#>> List Comprehension: 0.7394 seconds
#>> Basic (for loop): 0.4864 seconds
#>> Numpy: 0.3701 seconds

#As you can see Numpy is very effective