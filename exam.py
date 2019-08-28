import glob
import os
files = sorted(glob.glob('./data/*.txt'))

for file in files:
    print('------------------START:', os.path.basename(file))
