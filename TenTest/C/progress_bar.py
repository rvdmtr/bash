import os

path = '/home/dmtr/_SANDBOX/Tensor_Test/C_py/fordel/'

def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')
 
#print('Deleting files...')
#for i in range(10000+1):
#    progbar(i, 10000, 30)
#print()

print(os.listdir(path))

def looking(path):
    for i in os.listdir(path):
        #print(os.path.abspath(path+'/'+i))
        if os.path.isfile(path+'/'+i):
           looking(path+'/'+i)
           print('file ..')
        else:
            print('dir..')
            looking(path)


looking(path)