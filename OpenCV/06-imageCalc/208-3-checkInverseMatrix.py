# Python program to inverse
# a matrix using numpy
  
# Import required package
import numpy as np
  
# Taking a 4 * 4 matrix
A = np.array([[6, 1, 1, 3],
              [4, -2, 5, 1],
              [2, 8, 7, 6],
              [3, 1, 9, 7]])
  
# Calculating the inverse of the matrix
print(np.linalg.inv(A))


def getCofactor(mat, temp, p, q, n):
    print('q : ',q)
    i = 0
    j = 0
 
    # Looping for each element of the matrix
    for row in range(n):
        for col in range(n):
            # Copying into temporary matrix
            # only those element which are not in given row and column
            if (row != p and col != q) :
                temp[i][j] = mat[row][col]
                j += 1
                # Row is filled, so increase row index and reset col index
                if (j == n - 1):
                    j = 0
                    i += 1
 
# Recursive function for
# finding determinant of matrix.
# n is current dimension of mat[][].
def determinantOfMatrix(mat, n):
    D = 0 # Initialize result
    print('determinantOfMatrix start')
    # Base case : if matrix
    # contains single element
    if (n == 1):
        return mat[0][0]
         
    # To store cofactors
    temp = [[0 for x in range(N)]
               for y in range(N)]
 
    sign = 1 # To store sign multiplier
 
    # Iterate for each
    # element of first row
    for f in range(n):
        print('f : ', f)
        # Getting Cofactor of mat[0][f]
        getCofactor(mat, temp, 0, f, n)
        D += (sign * mat[0][f] *
              determinantOfMatrix(temp, n - 1))
 
        # terms are to be added
        # with alternate sign
        sign = -sign
    return D
 
def isInvertible(mat, n): 
    print('isInvertible start')
    if (determinantOfMatrix(mat, N) != 0):
        return True
    else:
        return False
     
# Driver Code
mat = [[ 1, 0, 2, -1 ],
       [ 3, 0, 0, 5 ],
       [ 2, 1, 4, -3 ],
       [ 1, 0, 5, 0 ]]
     
N = 4
if (isInvertible(mat, N)):
    print("Yes")
else:
    print("No")
 
# This code is contributed
# by ChitraNayal