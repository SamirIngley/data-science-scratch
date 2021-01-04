# Abstractly, vectors are objects that can be added together to form new vectors and that can be multiplied by scalars (ie numbers, constants),
# also to form new vectors. 

# if you have the heights, weights, and ages of a number of people, you can treat your data as three-dimensional vectors [height, weight, age]
# if you're teaching a class with 4 exams, you can treat student grades as four dimensional vectors [exam1, exam2, exam3, exam4]

# Eddie Woo: Matrix Multiplication
# A * B != B * A ORDER MATTERS
# "Dot Multplication" -> scalar product
# "Cross Multiplication" -> cross product / vector product (several numbers) 
# for example if you have sell sushi. Each sushi has a price. You know how much you sell each day of the week.
# prices: chk eel avo  quantity: M T W R F
         #[$3 $4 $5]        chk [6 7 8 9 1]
                           #eel [7 5 9 5 2]
                           #avo [8 9 1 0 3]

# so to dot multiplication, we have to take 6, 7, 8 and multiply with prices respectively, then sum them. (dot product)
# to do cross multiplication, we take each of the sums from above and put each in its own matrix. 

from typing import List

# > A type alias is defined by assigning the type to the alias. In this example, Vector and list[float] will be treated as interchangeable synonyms:
Vector = List[float]

height_weight_age = [70, # inches
                     170, # pounds
                     40] # years

grades = [95, # exam1
          80, # exam2
          75, # exam3
          62] # exam4

# We want to do arithmetic on these vectors, so we have to implement that for our python lists

# Vectors add componentwise. This means if two vectors w and w are the same length, their sum is just the vector who first element is 
# v[0] + w[0], whose second element is v[1] + w[1], and so on. If v and w are NOT the same length, we are not allowed to add them. 
# [1, 2] + [2, 1] = [1+2, 2+1] or [3, 3]

# we can easily implement this by "zip"-ing the two together

def add(v: Vector, w: Vector) -> Vector:
    # adds corresponding elements
    assert len(v) == len(w), "Vectors are not the same length" # make sure they're the same length
    return [v_i + w_i for v_i, w_i in zip(v, w)]

assert add([1,2,3], [4, 5, 6]) == [5, 7, 9]

def subtract(v: Vector, w: Vector) -> Vector:
    # subtracts correspoinding elements
    assert len(v) == len(w), "Vectors are not the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([4, 5, 6], [1, 2, 3]) == [3, 3, 3]

# componentwise sum a list of vectors, create a new vector whose first element is the sum
# of all the first elements. Whose second element is the sum of all the second elements and so on. 

def vector_sum(vectors: List[Vector]) -> Vector:
    ''' Sums all corresponding elements ''' 
    # Check that vectors is not empty
    assert vectors, "no vectors provided!"

    # Check that vectors are all the same length
    num_elements = len(vectors[0])
    assert all(len(item) == num_elements for item in vectors), "different size vectors!"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(constant: float, vector: Vector) -> Vector:
    ''' Multiplies every element by constant '''
    return [value*constant for value in vector]

assert scalar_multiply(2, [1, 2, 3]) == [2, 4, 6]


# compute the componentwise mean for a list of (same sized) vectors
def vector_mean(vectors: List[Vector]) -> Vector:
    ''' Computes the element wise average '''
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))

assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]

# DOT PRODUCT of two vectors is the sum of their componentwise products
def dot(v: Vector, w: Vector) -> float:
    ''' Computes v1[0]*v2[0] + v1[1]*v2[1] + ... v1[n]*v2[n] '''
    assert len(v) == len(w)
    return sum(i*j for i, j in zip(v, w))

assert dot([1, 2, 3], [4, 5, 6]) == 32

# Using dot product, easy to compute a vector's sum of squares
def sum_of_squares(v: Vector) -> float:
    ''' Returns v_1 * v_1 + ... + v_n * v_n ''' 
    return dot(v, v)

assert sum_of_squares([1, 2, 3]) == 14

# which we can use to compute its magnitude (length)
import math

def magnitude(v: Vector) -> float:
    ''' Returns the magnitude (or length) of v '''
    return math.sqrt(sum_of_squares(v))

assert magnitude([3, 4]) == 52

# We now have all the pieces we need to compute the distance between two vectors, defined as:
# Sqrt( (v1-w1)**2 + ... + (vn - wn)**2 )

def squared_distance(v: Vector, w: Vector) -> float:
    ''' Computes (v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 ''' 
    return sum_of_squares(subtract(v,w))

def distance(v: Vector, w: Vector) -> float:
    ''' Computes the distance between v and w ''' 
    return magnitude(subtract(v, w))

# Using lists as vectors is great for exposition but terrible for performance
# In production, you would want to use the NumPy library, which includes a high-performance
# array class with all sorts of arithmetic operations included

