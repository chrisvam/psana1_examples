from psana import *
ds = MPIDataSource('exp=xpptut15:run=280')
det = Detector('ACQ1')
for nevent,evt in enumerate(ds.events()):
    # waveforms are in Volts, times are in Seconds
    waveforms = det.waveform(evt)
    times = det.wftime(evt)
    # this shows there are 4 channels, each with 80000 samples
    print(waveforms.shape, times.shape)
    break
import matplotlib.pyplot as plt
plt.plot(times[0],waveforms[0])
plt.show()
