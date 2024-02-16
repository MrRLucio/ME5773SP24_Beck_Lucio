import numpy as np
import math as mth
import numexpr as ne
import time as tm

print('')

N = 10**7
deltax = 2/N


F1 = 0

tf_0 = tm.time()

for i in range(0,N):
    
    xi = deltax*i - 1
    fx = mth.sqrt(4-4*(xi**2))
    F1 = F1+(fx*deltax)

tf_f = tm.time()

tf_el = (tf_f-tf_0)
#print(tf_el)

print('Time elapsed using a for loop: '+str('%.6f'%tf_el))
print('The Integral evaluates as: '+str(F1))


#print('now for x stuff')

#x_vals = np.linspace(-1,1,num=N,endpoint=False)

#print(x_vals)
#print(x_vals.size)
#print(x_vals[N-1])
#print(deltax)


tnp_0 = tm.time()

i_vec = np.arange(0,N)
#print(i_vec)

x_vec = (2*i_vec/N) - 1
#print(x_vec)

F_vec = np.sqrt(4-4*np.square(x_vec))*deltax

#print(F_vec)

F2 = np.sum(F_vec)

tnp_f = tm.time()

tnp_el = tnp_f-tnp_0

print('\nTime elapsed for NumPy vectorization: '+str(round(tnp_el,6)))
print('The Integral evaluates as: '+str(F2))


tne_0 = tm.time()

i_vec = np.arange(0,N)
#print(i_vec)

x_vec = (2*i_vec/N) - 1
#print(x_vec)

F_vec = ne.evaluate('sqrt(4-4*x_vec**2)*deltax')

F3 = ne.evaluate('sum(F_vec)')

tne_f = tm.time()
tne_e = tne_f-tne_0

print('\nTime elapsed for NumExpr Evaluation: '+str(round(tne_e,6)))
print('The Integral evaluates as: '+str(F3))

print('')
