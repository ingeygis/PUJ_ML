## =========================================================================
## @author Leonardo Florez-Valencia (florez-l@javeriana.edu.co)
## =========================================================================

import math
from Perceptron import *
import ActivationFunctions

w = [ 1, 1, 2, 3 ]
b = 0.3
p = Perceptron( w, b, ActivationFunctions.LogisticSigmoid( ) )
print( p( [ 0, 0, 1, 3 ] ) )

## eof - $RCSfile$