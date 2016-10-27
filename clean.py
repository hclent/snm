from glob import glob
import os

def getGeneCount():
    savePath = 'ks/geneCount.txt'
    with open(savePath,'w') as f:
        f.write('id,geneCount,name\n')
    for filename in glob('ks/fasta/*.*'):
        with open(filename) as f: 
            f.seek(-5555,2)
            count = f.readlines()[-2].split('||')[-1].rstrip()
            gid = filename.split('/')[-1].split('-')[0]
            print filename
            print gid
            print 'gene count:', count
        with open('ks/geneCount.txt','a') as f:
            f.write(gid+','+count+',\n')

##getGeneCount()


def cleanKS(gids = ['11691', '7057', '28918', '25571', '4242']):
    '''
        gids - genomes (IDs) of interest
    '''
    for f in glob('ks/cleaned/*.*'):
        os.remove(f)
    
    for filename in glob('ks/real/*.ks'):
    ##    get genome IDs from filename
        g1, g2 = filename.split('/')[-1].split('.')[0].split('_')
    ##    if this file is of interest
        if g1 in gids and g2 in gids:
            
            saveName = 'ks/cleaned/' + g1 + '_' + g2 + '.ks'
            with open(filename) as f:
                l = [i for i in f.readlines() \
                             if not i.startswith('#') \
                                 and not i.startswith('NA')\
                                 and not i.startswith('undef')\
                     ]

            l = [\
            i.split('\t')[0]+'\t' \
            +'-'.join(i.split('\t')[4:6])+'\t' \
            +'-'.join(i.split('\t')[8:10]) \
            for i in l]


            with open(saveName,'w') as f:
                f.write('\n'.join(l))


cleanKS()
