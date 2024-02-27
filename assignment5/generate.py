import numpy as np
import time as tm
import h5py as h5

matrix_shape = (5000, 5000)
A = np.random.randint(low=2, high=10, size=matrix_shape, dtype=np.int64)
#^this line brought to you by ChatGPT3.5

A = np.asfortranarray(A)
#^this line brought to you by ChatGPT3.5

print(A)
print(A.dtype)

B = np.random.randint(low=100, high=127, size=matrix_shape, dtype=np.int8)
#^this line brought to you by ChatGPT3.5

print(B)
print(B.dtype)

C = np.full(matrix_shape, fill_value=1/3, dtype=np.float64)
#^this line brought to you by ChatGPT3.5

print(C)
print(C.dtype)



D = np.full([10,10],fill_value=1000,dtype='int16',order='F')
#^this line partially brought to you by ChatGPT3.5

for i in range(1,11):
    for j in range(1,11):
        D[i-1,j-1] = D[i-1,j-1] + i + 10*(j-1)
np.asfortranarray(D)
print(D)
print(D.dtype)

E = np.array([[350.0,350.2],[350.1,350.3]],dtype='float32',order='C')
print(E)
print(E.dtype)


T_A0 = tm.time() 
np.savetxt('A.csv', A, fmt='%d', delimiter=', ')
T_Af = tm.time() 

T_B0 = tm.time() 
np.savetxt('B.csv', B, fmt='%d', delimiter=', ')
T_Bf = tm.time() 

T_C0 = tm.time() 
np.savetxt('C.csv', C, fmt='%.18f', delimiter=', ')
T_Cf = tm.time() 

T_D0 = tm.time() 
np.savetxt('D.csv', D, fmt='%d', delimiter=', ')
T_Df = tm.time() 

T_E0 = tm.time() 
np.savetxt('E.csv', E, fmt='%.7f', delimiter=', ')
T_Ef = tm.time() 

delta_TA = T_Af-T_A0 
delta_TB = T_Bf-T_B0 
delta_TC = T_Cf-T_C0 
delta_TD = T_Df-T_D0 
delta_TE = T_Ef-T_E0 

print('\n')
print('time to make a CSV of A: ' + str(delta_TA))
print('time to make a CSV of B: ' + str(delta_TB))
print('time to make a CSV of C: ' + str(delta_TC))
print('time to make a CSV of D: ' + str(delta_TD))
print('time to make a CSV of E: ' + str(delta_TE))


#Using Numpy to save the arrays
TA0 = tm.time()
np.save('A.npy',A)
TAf = tm.time()

TB0 = tm.time()
np.save('B.npy',B)
TBf = tm.time()

TC0 = tm.time()
np.save('C.npy',C)
TCf = tm.time()

TD0 = tm.time()
np.save('D.npy',D)
TDf = tm.time()

TE0 = tm.time()
np.save('E.npy',E)
TEf = tm.time()


D_TA = TAf-TA0
D_TB = TBf-TB0
D_TC = TCf-TC0
D_TD = TDf-TD0
D_TE = TEf-TE0


print('\n')
print('time to make a npy file of A: ' + str(D_TA))
print('time to make a npy file of B: ' + str(D_TB))
print('time to make a npy file of C: ' + str(D_TC))
print('time to make a npy file of D: ' + str(D_TD))
print('time to make a npy file of E: ' + str(D_TE))


f = h5.File("matrix_db.hdf5",'w')

f.create_group('integer_group')
f['integer_group'].attrs['description'] = 'Integer Matrices A, B, and D'

TA0 = tm.time()
f['integer_group'].create_dataset('A', data = A, chunks=(500,500), compression='gzip')
TAf = tm.time()

TB0 = tm.time()
f['integer_group'].create_dataset('B', data = B, chunks=(1000,1000), compression='gzip')
TBf = tm.time()

TD0 = tm.time()
f['integer_group'].create_dataset('D', data = D)
TDf = tm.time()

f.create_group('float_group')
f['float_group'].attrs['description'] = 'Float Matrices C and E'

TC0 = tm.time()
f['float_group'].create_dataset('C', data = C, compression='gzip')
TCf = tm.time()

TE0 = tm.time()
f['float_group'].create_dataset('E', data = E)
TEf = tm.time()

D_TA = TAf-TA0
D_TB = TBf-TB0
D_TC = TCf-TC0
D_TD = TDf-TD0
D_TE = TEf-TE0


print('\n')
print('time to make a compressed and chunked HDF5 dataset of A: ' + str(D_TA))
print('time to make a compressed and chunked HDF5 dataset of B: ' + str(D_TB))
print('time to make a compressed  HDF5 dataset of C: ' + str(D_TC))
print('time to make an HDF5 dataset of D: ' + str(D_TD))
print('time to make an HDF5 dataset of E: ' + str(D_TE))




f.flush()




