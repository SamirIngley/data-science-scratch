# Matrix is a two dimensional collection of numbers. We will represent matrices as lists of lists
# If A is a matrix, then A[i][j] is the elementh in the ith row and the jth column.
# mathematical convention: capitalize the matrix

from typing import List

Vector = List[float]

# Another type alias
Matrix = List[List[float]]

A = [[1, 2, 3],     # A has 2 rows and 3 columns
     [4, 5, 6]]

B = [[1, 2],        # B has 3 rows and 2 columns  
     [3, 4],
     [5, 6]]   

# Side note: in mathematics you would usually name the first row of the matrix "row 1" and the first column "column 1". 
# Because we are using Python lists, which are zero-indexed, we'll call the first row of a matrix "row 0" and the first column "column 0".

# Given the list of lists represenation, the matrix A has a len(A) rows and len(A[0]) columns,
# which we consider its shape.
from typing import Tuple

def shape(A: Matrix) -> Tuple[int, int]:
    ''' Returns (# of rows of A, # of columns of A) '''
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0 # number of elements in first row
    return num_rows, num_cols

# If a matrix has n rows and k columns, we will refer to it as an n x k matrix. 
# We can think of each row of an n x k matrix as a vector of lengthh k, and each
# column as a vector of length n

def get_row(A: Matrix, i:int) -> Vector:
    ''' Returns the i-th row of A (as Vector) '''
    return A[i]

def get_column(A: Matrix, j:int) -> Vector:
    ''' Returns the j-th column of A (as a Vector)'''
    return [A_i[j]          # jth element of row A_i 
            for A_i in A]   # for each row A_i

# We'll also want to be able to create a matrix given its shape and a function for generating its elements. 
# We can do this using a nested list comprehension:
from typing import Callable

def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    ''' Returns a num_rows x num_cols matrix whose (i, j)-th entry is entry_fn(i, j) '''
    return [[entry_fn(i, j)             # given i, create a list
             for j in range(num_cols)]  # [entry_fn(i, 0), ... ]
             for i in range(num_rows)]  # create one list for each i

# Given this function, you could make a 5 x 5 identity matrix (with 1s on the diagonal and 0s elsewhere) like so:
def identity_matrix(n: int) -> Matrix:
    ''' Returns the n x n identity matrix ''' 
    return print(make_matrix(n, n, lambda i, j: 1 if i == j else 0))

assert identity_matrix(3) == [[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 1]]

# ??? not sure why the error is happening