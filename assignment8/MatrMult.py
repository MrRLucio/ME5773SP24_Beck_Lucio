import cython as cy
import numpy as np
cimport numpy as np
import time
cimport time


def matrMult(np.ndarray[float] A, np.ndarray[float] B):
    '''
    MatrMult Matrix Multiplies the two matrices A and B to produce a Matrix C, where
    matrix A is on the Left, and matrix B is on the right, like so: [A][B] = [C];

    This is accomplished using a triply nested for loop, and is intended as a demonstration
    of how to flat code a matrix multiplication, rather than an eficient  means to do so.
    '''
    
    cdef int n
    cdef int m
    cdef int p
    cdef int i
    cdef int j
    cdef float summer
    cdef np.ndarray[float] C

    n = A.shape[0]

    if(A.shape[1] != B.shape[0]):
        raise error('A must have the same number of rows as B has columns.')
    # end if

    m = A.shape[1] #= B.shape
    p = B.shape[1]
    
    C = np.zeros((n,p))


    #following the index of the target location in the new matrix
    for i in range(n):
        for j in range(p):
            
            summer = 0

            #performing the row-column multiplications and sum
            for k in range(m):
                summer = summer + A[i,k]*B[k,j]
            #end population nested loop
            
            C[i,j] = summer

        #end j-index nested loop
    #end i-index loop
    
    return C

#end function

if __name__ == '__main__':
    
    cdef float t_0
    cdef float t_f
    cdef float dt3A
    cdef float dt3np
    cdef float dt10A
    cdef float dt10np
    cdef float dt100A
    cdef float dt100np
    cdef float dt1000A
    cdef float dt1000np
    
    cdef int i
    cdef int d
    
    cdef np.ndarray[float] a
    cdef np.ndarray[float] b

    t_0 = time.time()
    d = 3
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = matrMult(a,b)
    # end for
    t_f = time.time()
    dt3A = (t_f-t_0)/100

    
    t_0 = time.time()
    d = 3
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = np.dot(a,b)
    # end for
    t_f = time.time()
    dt3np = (t_f-t_0)/100
 
    print("Average times to multiply two 3x3 matrices with...")
    print("Team 1's Cythonized Code: {0}, Numpy: {0}", dt3A, dt3np)


    t_0 = time.time()
    d = 10
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = matrMult(a,b)
    # end for
    t_f = time.time()
    dt10A = (t_f-t_0)/100
    
    t_0 = time.time()
    d = 10
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = np.dot(a,b)
    # end for
    t_f = time.time()
    dt10np = (t_f-t_0)/100
   
    print("Average times to multiply two 10x10 matrices with...")
    print("Team 1's Cythonized Code: {0}, Numpy: {0}", dt10A, dt10np)



    t_0 = time.time()
    d = 100
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = matrMult(a,b)
    # end for
    t_f = time.time()
    dt100A = (t_f-t_0)/100
 
    t_0 = time.time()
    d = 100
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = np.dot(a,b)
    # end for
    t_f = time.time()
    dt100np = (t_f-t_0)/100
    
    print("Average times to multiply two 100x100 matrices with...")
    print("Team 1's Cythonized Code: {0}, Numpy: {0}", dt100A, dt100np)


    t_0 = time.time()
    d = 1000
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = matrMult(a,b)
    # end for
    t_f = time.time()
    dt1000A = (t_f-t_0)/100
   
    t_0 = time.time()
    d = 1000
    for i in range(100):
        a = np.random.rand(d,d)
        b = np.random.rand(d,d)
        c = np.dot(a,b)
    # end for
    t_f = time.time()
    dt1000np = (t_f-t_0)/100

    print("Average times to multiply two 1000x1000 matrices with...")
    print("Team 1's Cythonized Code: {0}, Numpy: {0}", dt1000A, dt1000np)

    '''
    c = matrMult(a,b)
    cee = np.dot(a,b)
    
    print("\n")
    print(c)
    print()
    print(cee)
    print("\n")
    '''


