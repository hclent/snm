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
genomeIDs = [f.split('/')[-1].split('.')[0].split('_') for f in files]
genomeIDs = set(np.array(genomeIDs).ravel())
genomeIDs = [int(g) for g in genomeIDs]

print genomeIDs

x = pd.DataFrame(columns=genomeIDs, index=genomeIDs)

for f in files:
    print '_'*60
    print f
    genA, genB = f.split('/')[-1].split('.')[0].split('_')
    genA, genB = int(genA), int(genB)
    ki = kernel(f, sigma=1)
    print ki
    x[genA][genB] = ki
    x[genB][genA] = ki

genomeInfo = pd.read_csv('ks/geneCount.txt',
                         index_col = 'id')

for i in genomeIDs:
    x[i][i] = 1
    
print x

pca = PCA(n_components=2)
pca.fit(x)
print 'pca ratio', pca.explained_variance_ratio_

fig = plt.figure()
ax = fig.add_subplot(121, projection = '3d')
ax.scatter(x.iloc[:,0],x.iloc[:,1],x.iloc[:,2], color = 'bbrr')
ax = fig.add_subplot(122)
xCap = pca.transform(x)
print xCap
ax.scatter(xCap[:,0],xCap[:,1], color='bbrr')
ax.axis('square')

names = genomeInfo['name']
for pt,gID in zip(xCap, genomeIDs):
    ax.text(pt[0],pt[1],names[gID])
    
plt.show()
