from glob import glob

from scipy.misc import imread
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

from kernel import kernel,k

np.set_printoptions(precision=4)

path = 'ks/cleaned/*.ks'
files = glob(path)
genomes = [f.split('/')[-1].split('.')[0].split('_') for f in files]
genomes = set(np.array(genomes).ravel())
genomes = [int(g) for g in genomes]

print len(genomes)


##for fileName in sorted(files):
##    print '_'*60
##    print fileName
##    img = imread(fileName)
##    img = gray(img)
##    a,b = fileName.split('/')[-1].split('.')[0].split('-')
##    a,b = ord(a)-65, ord(b)-65
##    if img[0,0] < 10:
##        img = 255-img
##    KS = img/1.0
##    sigma = 1
##    ki = kernel(KS, sigma)
##    x[a][b] = ki
##    x[b][a] = ki
##
##
##print x
##pca = PCA(n_components=2)
##pca.fit(x)
##print 'pca ratio', pca.explained_variance_ratio_
##
##fig = plt.figure()
##ax = fig.add_subplot(121, projection = '3d')
##ax.scatter(x[:,0],x[:,1],x[:,2], color = 'bbrrr')
##ax = fig.add_subplot(122)
##x = pca.transform(x)
##print x
##ax.scatter(x[:,0],x[:,1], color='bbrrr')
####ax.axis('square')
##
##plt.show()
