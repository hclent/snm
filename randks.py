import numpy as np


def randks2(size=(3,5)):
    KS = randks(size)
    with open('ks.txt','w') as f:
        for i in range(KS.shape[0]):
            for j in range(KS.shape[1]):
                if KS[i][j] < 1e99:
                    f.write('{}\ta{}\tb{}\n'.format(str(KS[i][j]), i, j) )            


def randks(size=(3,5)):
    pool = [1,3,4,6,0,0,0,0]
    pool += [1e100 for i in range(len(pool)/2)]
    KS = np.random.choice(pool,size)
    return np.array(KS,dtype=np.float64)

if __name__ == '__main__':
##set the size large to see performance of kernel
    randks2([100,100])
