import module as md
import numpy as np
import time

print()

'''
A =  np.array([[   -5.8600,     3.9900,    -5.9300,    -2.8200,     7.6900, ],
               [    3.9900,     4.4600,     2.5800,     4.4200,     4.6100, ],
               [   -5.9300,     2.5800,    -8.5200,     8.5700,     7.6900, ],
               [   -2.8200,     4.4200,     8.5700,     3.7200,     8.0700, ],
               [    7.6900,     4.6100,     7.6900,     8.0700,     9.8300, ]])

b =  np.array([[    1.3200,    -6.3300,    -8.7700],
               [    2.2200,     1.6900,    -8.3300],
               [    0.1200,    -1.5600,     9.5400],
               [   -6.4100,    -9.4900,     9.5600],
               [    6.3300,    -3.6700,     7.4800]])





print(A)
print(b)


t_start = time.time()
res = md.mkl_solver_symm( A, b)
#res = md.mkl_solver( A,b )

t_end = time.time()

#print(res)
#print(A)
print(b)


print('Time spent: {0:.6f} s'.format(t_end-t_start))
'''

N=10000
#N=10

#print(N)
#print('\n\nN = '+str(N)+'\n')

#make an array to populate the  diagonal
DM = np.ones(N)
#print('array to populate a diagonal:')
#print(DM)

#Make an array to populate the off-diagonal lines
OD = np.ones(N-1)
#print(OD)

#Make the K matrix using numpy's diagonal matrix maker and matrix addition and multiplication
K=(np.diag(DM,0)*2)+(np.diag(OD,-1)*-1)+(np.diag(OD,1)*-1)

#Setting K at NN to be 1 (note: Numpy, like python proper, starts at a zero index)
K[N-1,N-1]=1
#print(K)

#writing f
f = np.zeros(N)
f[N-1]=1/N
f = np.matrix(f).T
#print(f)

#solving the system
u=np.linalg.solve(K,f)

print('From Numpy: u = ')
print(u)
#print('The last term in u is: '+str(u[N-1])+'\n\n')


#making new matrices for the results
W1 = K
q1 = f

'''
print()
#Solving the System of Equations with the standard solver.
print(W1)
print(q1)
t_start = time.time()
res = md.mkl_solver( W1, q1)
t_end = time.time()

dt_gen = t_start-t_end

#print(res)
#print(K)
print()
print(q1)
print(f"Time to evaluate using the mkl_solver routine: {dt_gen:1.8E} seconds")


'''
print()
#Now to solve the system of equations with the symmetric solver

print(W1)
print(q1)
print()
t_start = time.time()
res = md.mkl_solver_symm( W1, q1)
t_end = time.time()

dt_symm = t_start-t_end


#print(res)
#print(A)
print(q1)
print(f"Time to evaluate using the symmetric solver routine: {dt_symm:1.8E} seconds")






print()
