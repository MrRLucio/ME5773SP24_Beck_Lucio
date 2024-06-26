from mpi4py import MPI
import math
import time

def f(x):
    return x*math.exp(x)

############################################
def gauleg(x1, x2, x, w, n):
    EPS = 3.0e-16
    m = (n + 1) // 2
    xm = 0.50 * (x2 + x1)
    xl = 0.50 * (x2 - x1)
    
    for i in range(1, m + 1):
        z = math.cos(math.pi * (i - 0.25) / (n + 0.50))
        while True:
            p1 = 1.0
            p2 = 0.0
            for j in range(1, n + 1):
                p3 = p2
                p2 = p1
                p1 = ((2.0 * j - 1.0) * z * p2 - (j - 1.0) * p3) / j
            
            pp = n * (z * p1 - p2) / (z * z - 1.0)
            z1 = z
            z = z1 - p1 / pp
            
            if abs(z - z1) > EPS:
                continue
            
            x[i - 1] = xm - xl * z
            x[n - i] = xm + xl * z
            w[i - 1] = 2.0 * xl / ((1.0 - z * z) * pp * pp)
            w[n - i] = w[i - 1]
            break
#######################################################################


#Set up the MPI process
comm = MPI.COMM_WORLD

#acquire the total number of tasks
size = comm.Get_size()

#Get each task's ID
rank = comm.Get_rank()

inputs = []

if rank == 0:
    
    for x in range(size):
        slc = [x, 0, 0, 0]
        inputs.append(slc)
    
    #print("The Gaussian Quadrature n values are: ", inputs[:][0] )

else:
    inputs = None

data = comm.scatter(inputs, root=0)


#Doing the Quadratures
if rank != 0:
    #begin timer
    start = time.perf_counter()

    #performing the Gaussian-Legendre Int.
    n = data[0]
    x = [0.0] * n
    w = [0.0] * n
    x1, x2 = -1.0, 1.0
    gauleg(x1, x2, x, w, n)
    #print("x =", x)
    #print("w =", w)
    
    sum = 0.0
    for i in range(0,n):
        sum = sum + w[i]*f(x[i])
    data[1] = sum
    #print("Process ", rank, "of n=", data, f"has sum = ",{sum})
    exact = 2/math.exp(1)
    RE = abs(sum-exact)/exact
    data[2] = RE
    #print("Process ", rank, "of n=", data, f"has relative error =",{RE})
    finish = time.perf_counter()
    elapsed = finish - start
    data[3] = elapsed
    #print("Process ", rank, "of n=", data, f"took {elapsed} seconds")

Output = comm.gather(data, root=0)

if rank == 0:
    
    print("Quadrature #,          Integration Result,                     Percent Error,                      Run Time (s)")
    for i in range(1, size):
        print(f"     {Output[i][0]}      \t\t      {Output[i][1]:.16E}              {Output[i][2]:.16E}              {Output[i][3]}")
    


'''
# Example usage:
n = 3
x = [0.0] * n
w = [0.0] * n
x1, x2 = -1.0, 1.0
gauleg(x1, x2, x, w, n)
print("x =", x)
print("w =", w)

sum = 0.0
for i in range(0,n):
    sum = sum + w[i]*f(x[i])
print(f"sum = ",{sum})
exact = 2/math.exp(1)
print(f"Relative error =",{abs(sum-exact)/exact})
'''



