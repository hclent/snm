from glob import glob

from scipy.misc import imread
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

from kernel import kernel
from clean import cleanKS
np.set_printoptions(precision=4)

interest = ['11691', '7057', '28918','25571', '4242']
cleanKS(interest)


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

pca = PCA(n_components=3)
pca.fit(x)
print 'pca ratio', pca.explained_variance_ratio_

xCap = pca.transform(x)
print xCap

fig = plt.figure()
ax = fig.add_subplot(121, projection = '3d')
ax.scatter(xCap[:,0],xCap[:,1],xCap[:,2], color = 'rrbbb')
##limit = 1
##ax.set_xlim(-limit, limit)
##ax.set_ylim(-limit, limit)
##ax.set_zlim(-limit, limit)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('x3')


ax = fig.add_subplot(122)
ax.scatter(xCap[:,0],xCap[:,1], color='rrbbb')
ax.axis('square')


names = genomeInfo['name']
for pt,gID in zip(xCap, genomeIDs):
    ax.text(pt[0],pt[1],names[gID])


##plt.savefig("test.svg")
plt.show()
