from nltk.tokenize import word_tokenize
import numpy as np
import random

def data_stream():
    """Stream the data in 'leipzig100k.txt' """
    with open('/Users/harshinder/Downloads/homework2-master/leipzig100k.txt', 'r') as f:
        for line in f:
            for w in word_tokenize(line):
                if w.isalnum():
                    yield w
   
def bloom_filter_set():
    """Stream the data in 'Proper.txt' """
    with open('/Users/harshinder/Downloads/homework2-master/Proper.txt','r') as f:
        for line in f:
            yield line.strip()

a = []
for i in data_stream():
    if len(i) % 8 == 0:
         a.append(i)
    else:
        a.append(i.ljust(len(i) + (8-(len(i) % 8)),'!'))
        
d = []      

for i in range(len(a)):
    d.append([ord(x) for x in a[i]])

dd = []
        
for i in range(len(d)):
    dd.append(256**7*d[i][0] + 256**6*d[i][1] + 256**5*d[i][2] + 256**4*d[i][3] + 256**3*d[i][4] + 256**2*d[i][5] + 256 **1*d[i][6] + 2256**0*d[i][7])



############### DO NOT MODIFY ABOVE THIS LINE #################


# Implement a universal hash family of functions below: each function from the
# family should be able to hash a word from the data stream to a number in the
# appropriate range needed.


p = 100000000000000000039
def uhf(p, m):
    a = random.randint(1,p-1)
    b = random.randint(0,p-1)
    return lambda x: ((a * x + b) % p)% m

############### 

################### Part 1 ######################
from bitarray import bitarray


sizess =  2**18   # size of the filter
num_hash = 5

hashes = [np.vectorize(uhf(p,2*len(dd)))(range(len(dd))) for
                                            _ in range(5)]

hash_fns2 = [np.vectorize(uhf(p,sizess))(range(sizess)) for
                                            _ in range(5)]




hash_fns = [hashes[0], hashes[1], hashes[2], hashes[3], hashes[4]]  # place holder for hash functions



ads = []


for i in bloom_filter_set():
    ads.append(i)


bloom_filter = None

num_words = len(dd)         # number in data stream
num_words_in_set = len(ads)  # number in Bloom filter's set


import math


class BloomFilter(object):
    def __init__(self, *sizes):
        self.hashes = [ Hash(size) for size in sizes ]
        
    def add(self, num):
        for h in self.hashes:
            h.add(num)
            
    def get(self, num):
        for h in self.hashes:
            if not h.get(num):
                return 0
        return 1
    
    def fp(self):
        total = 0.
        for h in self.hashes:
            occupancy = sum(h.bits)
            f = occupancy / float(h.size)
            total += math.log(f, 2)
            
        return 2**total
    
    def empirical_fp(self, actual, max):
        found_true = 0
        found_false = 0
        for i in range(max):
            if self.get(i):
                if i in actual:
                    found_true += 1
                else:
                    found_false += 1
                    
        return found_false / float(max)
            
    
    def show(self):
        rows = len(self.hashes)
        cols = max([ h.size for h in self.hashes ])
        grid = BlockGrid(cols, rows, fill=(0,0,0))
        for i, h in enumerate(self.hashes):
            for pos in range(h.size, cols):
                grid[i, pos] = (255, 255, 255)
            for j, bit in enumerate(h.bits):
                if bit:
                    grid[i, j] = (255, 0, 0)
        return grid.show()
    

ads = []
for i in bloom_filter_set():
    BloomFilter(i,hashes[0])



#for word in bloom_filter_set(): # add the word to the filter by hashing etc.
#    pass 

#for word in data_stream():  # check for membership in the Bloom filter
#    pass 

print('Total number of words in stream = %s'%(num_words,))
print('Total number of words in stream = %s'%(num_words_in_set,))
      
################### Part 2 ######################

hash_range = 24 # number of bits in the range of the hash functions

size2 = 2**hash_range

# fm_hash_functions = [None]*35  # Create the appropriate hashes here

fm_hash_functions = [np.vectorize(uhf(p,size2))(range(size2)) for
                                            _ in range(35)]


G1 = [fm_hash_functions[0],fm_hash_functions[1],fm_hash_functions[2],fm_hash_functions[3],fm_hash_functions[4]]
G2 = [fm_hash_functions[5],fm_hash_functions[6],fm_hash_functions[7],fm_hash_functions[8],fm_hash_functions[9]]
G3 = [fm_hash_functions[10],fm_hash_functions[11],fm_hash_functions[12],fm_hash_functions[13],fm_hash_functions[14]]
G4 = [fm_hash_functions[15],fm_hash_functions[16],fm_hash_functions[17],fm_hash_functions[18],fm_hash_functions[19]]
G5 = [fm_hash_functions[20],fm_hash_functions[21],fm_hash_functions[22],fm_hash_functions[23],fm_hash_functions[24]]
G6 = [fm_hash_functions[25],fm_hash_functions[26],fm_hash_functions[27],fm_hash_functions[28],fm_hash_functions[29]]
G7 = [fm_hash_functions[30],fm_hash_functions[31],fm_hash_functions[32],fm_hash_functions[33],fm_hash_functions[34]]





def findTrailingZeros(n): 
    count = 0
    i=5
    while (n/i>=1): 
        count += int(n/i) 
        i *= 5
        return int(count) 

def num_trailing_bits(n):
    count = 0
    i = 5
    
    """Returns the number of trailing zeros in bin(n)

    n: integer
    """
    pass

num_distinct = 0

#for word in data_stream(): # Implement the Flajolet-Martin algorithm
#    pass

print("Estimate of number of distinct elements = %s"%(num_distinct,))

################### Part 3 ######################

var_reservoir = [0]*512
second_moment = 0
third_moment = 0

# You can use numpy.random's API for maintaining the reservoir of variables

#for word in data_stream(): # Imoplement the AMS algorithm here
#    pass 
      
print("Estimate of second moment = %s"%(second_moment,))
print("Estimate of third moment = %s"%(third_moment,))
