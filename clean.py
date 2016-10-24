from glob import glob

for filename in glob('ks/fasta/*.fasta'):
    with open(filename) as f:
        f.seek(-5555,2)
        print filename
        print 'gene count:',
        print f.readlines()[-2].split('||')[-1]
        
##for filename in glob('ks/real/*.ks'):
##    
##    if '11691' in filename or '7057' in filename\
##    or '28918' in filename or '25571' in filename:
##        
##        saveName = 'ks/cleaned/' + filename.split('/')[-1].split('.')[0] + '.ks'
##        with open(filename) as f:
##            l = [i for i in f.readlines() if not i.startswith('#') and not i.startswith('NA')]
##
##        l = [\
##        i.split('\t')[0]+'\t' \
##        +'-'.join(i.split('\t')[4:6])+'\t' \
##        +'-'.join(i.split('\t')[8:10]) \
##        for i in l]
##
##
##        with open(saveName,'w') as f:
##            f.write('\n'.join(l))

