from os.path import getsize
from random import randint

def gather_samples(n, input_file):
    '''
    Args:
        n: number of rows to sample
        input_file: path to file
    '''
    samples = [] # stores the samples gathered
    file_size = getsize(input_file)
    seek_list = [randint(1, file_size) for x in xrange(n)]
    seek_list.sort() # optimize for seeking
    file = open(input_file, 'rU') # change depending on input file
    for byte in seek_list:
        file.seek(byte)
        file.readline() # will never sample the first line
        row = file.readline()
        if row:
            samples.append(save)
        else: # if EOF then get the first line
            file.seek(0)
            samples.append(file.readline())
    return samples