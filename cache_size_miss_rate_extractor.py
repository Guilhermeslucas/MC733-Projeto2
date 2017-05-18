import os
import sys

files = [f for f in os.listdir('.') if os.path.isfile(f) and f[-4:] == '.txt']

fp = open('cache_size_and_miss_rate.csv', 'w')

for file in files:
    with open(file) as f:
        j = 0
        k = 0
        n = 0
        for i, line in enumerate(f):
            if i == (10 + j*69):  # Line with cache size
                cache = line[10:-1]
                j = j+1
            elif i == (41 + k*69):  # Line with miss rate
                rate_i = line[25:31].replace('.', ',')
                k = k+1
            elif i == (58 + n*69):
                rate_d = line[25:31].replace('.', ',')
                value = file+'\t'+cache+'\t'+rate_i+'\t'+rate_d+'\n'
                n = n+1
                fp.write(value)

fp.close()
