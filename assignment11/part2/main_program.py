import module as md
import numpy as np
import time




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
#res = md.mkl_solver_symm( A,b )
res = md.mkl_solver( A,b )

t_end = time.time()

print(A)
print(b)


print('Time spent: {0:.6f} s'.format(t_end-t_start))

