import numpy as np
n = np.array([75.42436315, 42.48558583, 60.32924763])
print("Given array:")
print(n)  
print("\nReplace all elements of array which are greater than 50. to 15.50")
n[n > 50.] = 15.50
  
print("New array :\n")
print(n)
