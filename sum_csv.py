import sys
import numpy as np

data = np.loadtxt(sys.argp[1])
print(np.sum(data))
