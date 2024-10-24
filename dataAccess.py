from psana import *

ds = MPIDataSource('exp=xpptut15:run=54:smd')
nevent = 0
for evt in ds.events():
    nevent += 1
    if nevent == 3:
        break
print(f'Processed {nevent} events.')
