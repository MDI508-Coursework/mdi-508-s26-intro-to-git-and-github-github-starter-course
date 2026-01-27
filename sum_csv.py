import sys
import numpy as np

data = np.loadtxt(sys.argv[1], delimiter=",")
print(np.sum(data))
