import time as tm
import numpy as np
import h5py as h5
'''
This Python code is to compare the time it takes to extract 
the matrices A, B, C, D, and E from CSV, numpy, and HDF5 files

Additionally, the code finds the size of the HDF5 datasets within
the HDF5 file
'''

#First setting up the HDF5 file to be read
f = h5.File("matrix_db.hdf5","r")



#Extracting the A files
At0 = tm.time()
A_txt = np.loadtxt('A.csv', delimiter=',', dtype='int64')
DAt = tm.time() - At0
print('\nTime to unpack A from its CSV file: ' + str(DAt))

An0 = tm.time()
A_npy = np.load('A.npy')
DAn = tm.time() - An0
print('Time to unpack A from its Numpy file: ' + str(DAn))

Adb = f['integer_group/A']
Ah0 = tm.time()
A_HDF = Adb[...]
DAh = tm.time() - Ah0
print('Time to unpack A from its HDF5 Dataset: ' + str(DAh))


#Extracting the B files
Bt0 = tm.time()
B_txt = np.loadtxt('B.csv', delimiter=',', dtype='int8')
DBt = tm.time() - Bt0
print('\nTime to unpack B from its CSV file: ' + str(DBt))

Bn0 = tm.time()
B_npy = np.load('B.npy')
DBn = tm.time() - Bn0
print('Time to unpack B from its Numpy file: ' + str(DBn))

Bdb = f['integer_group/B']
Bh0 = tm.time()
B_HDF = Bdb[...]
DBh = tm.time() - Bh0
print('Time to unpack B from its HDF5 Dataset: ' + str(DBh))


#Extracting the C files
Ct0 = tm.time()
C_txt = np.loadtxt('C.csv', delimiter=',', dtype='float64')
DCt = tm.time() - Ct0
print('\nTime to unpack C from its CSV file: ' + str(DCt))

Cn0 = tm.time()
C_npy = np.load('C.npy')
DCn = tm.time() - Cn0
print('Time to unpack C from its Numpy file: ' + str(DCn))

Cdb = f['float_group/C']
Ch0 = tm.time()
C_HDF = Cdb[...]
DCh = tm.time() - Ch0
print('Time to unpack C from its HDF5 Dataset: ' + str(DCh))



#Extracting the D files
Dt0 = tm.time()
D_txt = np.loadtxt('D.csv', delimiter=',', dtype='int16')
DDt = tm.time() - Dt0
print('\nTime to unpack D from its CSV file: ' + str(DDt))

Dn0 = tm.time()
D_npy = np.load('D.npy')
DDn = tm.time() - Dn0
print('Time to unpack D from its Numpy file: ' + str(DDn))

Ddb = f['integer_group/D']
Dh0 = tm.time()
D_HDF = Ddb[...]
DDh = tm.time() - Dh0
print('Time to unpack D from its HDF5 Dataset: ' + str(DDh))



#Extracting the E files
Et0 = tm.time()
E_txt = np.loadtxt('E.csv', delimiter=',', dtype='float32')
DEt = tm.time() - Et0
print('\nTime to unpack E from its CSV file: ' + str(DEt))

En0 = tm.time()
E_npy = np.load('E.npy')
DEn = tm.time() - En0
print('Time to unpack E from its Numpy file: ' + str(DEn))

Edb = f['float_group/E']
Eh0 = tm.time()
E_HDF = Edb[...]
DEh = tm.time() - Eh0
print('Time to unpack E from its HDF5 Dataset: ' + str(DEh) + '\n')






