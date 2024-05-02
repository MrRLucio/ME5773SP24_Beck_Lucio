import cupy as cp
import time as time
import numpy as np


defK_kernel = cp.RawKernel(r'''
extern "C" __global__
void defK( double* K_p, int ncols, int nrows) {
    /*
    This function defines a square matrix K (row-major format)
    with all elements in the diagonal as 4 and all elements
    next to the diagonal as -2. The last element of the diagonal
    set to 2. All other elements are set to zero.

    INPUTS:
    - K: Pointer to the memory in K.
    - nrows: Number of rows of the matrix
    - ncols: Number of columns of the matrix

    */
    
    // FYI: This is a comment
    
    /* and this is also a comment */

    // Define global indices of the threads along each direction.
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;   
    
    // Check that the i, j location lies within the matrix dimensions.
    if ( ( i < nrows) && ( j < ncols ) ){
        
        // Define the contiguous global index of the matrix.
        // i.e the index to access a single data point from the main 
        // pointer in K 
        // Consider the global indices as follows
        //
        // K_local = [[(0,0),(0,1),(0,2)],  // i,j indices for K.
        //            [(1,0),(1,1),(1,2)],
        //            [(2,0),(2,1),(2,2)]]
        //
        // K_g = [[ 0, 1, 2],  // global contiguous indices for K.
        //        [ 3, 4, 5],
        //        [ 6, 7, 8]]
        //
        // we use long long type (int64) because the 
        // integer value gets very large.
        //

        long long g_indx = i * ncols + j ;    
        
        if (i==j && i!=(nrows-1) ){

            // Diagonal elements that aren't the final value.
            K_p[g_indx] = 4.0;
        
        } else if (i==j && i==(nrows-1) ){
            
            // Final diagonal must be 2
            K_p[g_indx] = 2.0;

        } else if  (j==(i+1) || j==(i-1)){
        
            K_p[g_indx] = -2.0;
        
        } else {

            K_p[g_indx] = 0.0;

        }
        
    }

}
''', 'defK') 

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

t_start = time.time()
N = 30000
#N=10

K = cp.empty((N,N),dtype = cp.float64)

# Define the execution grid.
block_dim = 16
grid_dim  = N//block_dim+1 # Guarantee we send at least 1 grid.

# We are required to create the holder of the result.
# print("-")
defK_kernel((grid_dim,grid_dim,1), (block_dim,block_dim,1), ( K, K.shape[0],K.shape[1]))  # grid, block and arguments


# Make the values in f:
f = cp.zeros((N,1))
f[N-1] = 1/N

# Making and printing the solution vector [u] to the problem [K][u] = [f]:
u = cp.linalg.solve(K,f)
print(u)

t_end = time.time()

# Checking the values in the matrix and RHS vector:
print(K)
print(f)

print(f"Time spent creating the matrix and rhs vector, and solving for the lhs vector using CuPy: {t_end-t_start:.6f} s")


# Now to repeat the process with Numpy functions:

print("Numpy Time:")

#start time for the host device operations
th_0=time.time()

#make an array to populate the  diagonal
DM = np.ones(N)
#print('array to populate a diagonal:')
#print(DM)

#Make an array to populate the off-diagonal lines
OD = np.ones(N-1)
#print(OD)

#Make the K matrix using numpy's diagonal matrix maker and matrix addition and multiplication
K_H=(np.diag(DM,0)*4)+(np.diag(OD,-1)*-2)+(np.diag(OD,1)*-2)

#Setting K at NN to be 2 (note: Numpy starts at a zero index)
K_H[N-1,N-1]=2
#print(K)

#writing f
f_H = np.zeros(N)
f_H[N-1]=1/N
#print(f)

#calculating u_host
u_H = np.linalg.solve(K_H,f_H)
print(u_H)

#end time for making K_h, f_h, and u_h, and printing u_H
th_f=time.time()

#computing the elapsed time
tm_elapsed=th_f-th_0

#checking the host stuff
print(K_H)
print(f_H)

print(f"Time needed to make Matrix [K], RHS [f], and solution [u] with numpy, as well as to print[u]: {th_f-th_0:.6f} s")


