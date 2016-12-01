import numpy as np
import time

'''Python 2.7 code for matrix ngrams
Very computationally expensive '''

x0 = np.random.randint(9, size=(12, 13))

#Input: matrix, and number n of desired ngrams
def matrixNgramAll(matrix, n):
    t0 = time.time()
    
    num_rows = (len(matrix))
    num_columns = (len(matrix[0]))
    print(str(num_rows)+"x"+str(num_columns)+" matrix")
    
    ngrams = [] #list of np.array matrix n-grams
    
    #for each column
    for c in range(0, num_columns):
        print("Column " + str(c+1))
        
        #for each row 
        for r in range(0, num_rows):
            print("Row " + str(r+1))
            temp_list_of_rows = []

            gram_rows = np.array(matrix[r:(r+n)]) #make matricies with sliding window of n rows
            if len(gram_rows) == n:
                 #print(gram_rows)
#                 print("------")

                for j in range(0, n): #shorten num of gram_row columns to n, with sliding window of n columns 
                    #array[row][column] 
                    temp_row = gram_rows[j][0+c:n+c] #n rows, :n columns
                    #only append temp rows of correct column n-gram length
                    if (temp_row.size) == n:
                        temp_list_of_rows.append(temp_row)
                    if (temp_row.size) < n:
                        print("not enough columns to compute")

                gram = np.array(temp_list_of_rows)
                print(gram)
                print("-------------")
                
                #make sure that gram is not an emtpy array (checking temp_row.size doesn't actually help)
                if gram.size == n*n:
                    ngrams.append(gram)
                          
            if len(gram_rows) < n:
                print("not enough rows to compute")
    
    #return list of grams
    print("self info: done in %0.3fs." % (time.time() - t0))
    return ngrams

            
print(x0)
ngrams = matrixNgramAll(x0, 4) #self info: done in 0.053s.
print(ngrams)