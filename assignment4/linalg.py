import numpy as np
import time as tm
import sys

stdout_stuff = sys.stdout

N=5

#print(N)
stdout_stuff.write(str(N)+'\n')

tm_0=tm.time()

#make an array to populate the  diagonal
DM = np.ones(N)
#print('array to populate a diagonal:')
#print(DM)

#Make an array to populate the off-diagonal lines
OD = np.ones(N-1)
#print(OD)

#Make the K matrix using numpy's diagonal matrix maker and matrix addition and multiplication
K=(np.diag(DM,0)*2)+(np.diag(OD,-1)*-1)+(np.diag(OD,1)*-1)

#Setting K at NN to be 1 (note: Numpy starts at a zero index)
K[N-1,N-1]=1
print(K)

#writing f
f = np.zeros(N)
f[N-1]=1/N
print(f)

tm_f=tm.time()

#computing the elapsed time
tm_elapsed=tm_f-tm_0
print(round(tm_elapsed,9))

ts_0=tm.time()

#solving the system
u=np.linalg.solve(K,f)

ts_f = tm.time()

delta_ts='%.9f'%(ts_f-ts_0)
stdout_stuff.write('Solver time elapsed: '+str(delta_ts)+'\n')

print('u = ')
print(u)
print('The last term in u is: '+str(u[N-1]))

