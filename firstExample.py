from psana import *
import matplotlib.pyplot as plt

ds = MPIDataSource('exp=xpptut15:run=54:smd')
det = Detector('cspad')

for nevent, evt in enumerate(ds.events()):
    if nevent >= 2:
        break
    # includes pedestal subtraction, common-mode correction, bad-pixel
    # suppression, and uses geometry to position the multiple CSPAD panels
    # into a 2D image
    print(f'Fetching event number {nevent}')
    img = det.image(evt)

    plt.imshow(img, vmin=-2, vmax=2)
    plt.show()
print('Done.')
