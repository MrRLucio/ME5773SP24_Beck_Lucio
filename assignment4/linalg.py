import numpy as np
import time as tm
import sys

stdout_stuff = sys.stdout

N=10000

#print(N)
stdout_stuff.write('\n\nN = '+str(N)+'\n')

#start time for making K and f
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
#print(K)

#writing f
f = np.zeros(N)
f[N-1]=1/N
#print(f)

#end time for making k and f
tm_f=tm.time()

#computing the elapsed time
tm_elapsed=tm_f-tm_0
print('Time needed to make K and f: '+str(round(tm_elapsed,9)))

#start time for solving the system
ts_0=tm.time()

#solving the system
u=np.linalg.solve(K,f)

#end time for solving the system
ts_f = tm.time()

#elapsed time for solving the system
delta_ts='%.9f'%(ts_f-ts_0)
stdout_stuff.write('Solver time elapsed: '+str(delta_ts)+'\n')

print('u = ')
print(u)
print('The last term in u is: '+str(u[N-1])+'\n\n')

