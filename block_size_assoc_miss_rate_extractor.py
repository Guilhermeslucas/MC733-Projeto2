import os
import sys

files = [f for f in os.listdir('.') if os.path.isfile(f) and f[-4:] == '.txt']

fp = open('block_size_assoc_and_miss_rate.csv', 'w')

for file in files:
    with open(file) as f:
        j = 0
        k = 0
        n = 0
        m = 0
        for i, line in enumerate(f):
            if i == (12 + j*69):  # Line with block size
                cache = line[10:-1]
                j = j+1
            elif i == (16 + m*69):  # Assoc
                assoc = line[11:-1]
                m = m+1
            elif i == (41 + k*69):  # Line with instruction miss rate
                rate_i = line[25:31].replace('.', ',')
                k = k+1
            elif i == (58 + n*69):  # Line with data miss rate
                rate_d = line[25:31].replace('.', ',')
                value = file+'\t'+cache+'\t'+rate_i+'\t'+rate_d+'\t'+assoc+'\n'
                n = n+1
                fp.write(value)

fp.close()
