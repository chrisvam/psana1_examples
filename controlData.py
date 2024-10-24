import sys
from psana import *

ds = MPIDataSource('exp=xpptut15:run=200:smd')
cd = Detector('ControlData')

for nstep, step in enumerate(ds.steps()):
    pvList = cd().pvControls()
    for pv in pvList:
        print(f'Step: {nstep} name/value: {pv.name()} {pv.value()}')
    for evt in step.events():
        pass
    if nstep >= 2:
        sys.exit()

