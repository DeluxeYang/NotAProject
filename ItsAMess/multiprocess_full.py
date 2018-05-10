import multiprocessing 
import os

def fn():
    x = 0
    while True:
        x = x ^ 1

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = multiprocessing.Pool(6)
    for i in range(6):
        p.apply_async(fn)
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')