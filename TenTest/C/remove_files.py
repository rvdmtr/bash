import os,time,sys,shutil

#путь до директории, где хотим удалить файлы
path = '/home/dmtr/_SANDBOX/Tensor_Test/C_py/fordel/'


#путь до директории, куда скопировать файлы
#copypath = '/home/dmtr/_SANDBOX/Tensor_Test/C_py/copy_of_fordel'

dirs = 0
files = 0
dirslist = []
fileslist = []

def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')

def looking_files(path):
	"""Ходит по каталогам, определяет тип файлов"""
	global dirs,files
	global i

	for i in os.listdir(path):
		if os.path.isfile(path+'/'+i):
			files+=1
			os.remove(path+'/'+i)
			fileslist.append(path + '/' + i)
			looking_files(path+'/'+i)
		else:
			dirslist.append(path+'/'+i)
			dirs+=1
			os.rmdir(path+'/'+i)

#ORIGINAL
#	for i in os.listdir(path):
#		if os.path.isdir(path+'/'+i):
#			dirs+=1
#			os.rmdir(path+'/'+i)
#			dirslist.append(path + '/' + i)
#			looking_files(path+'/'+i)
#	else:
#			fileslist.append(path+'/'+i)
#			files+=1
#			os.remove(path+'/'+i)



def prinitng_files(filelist):
	for i in filelist:
		print(i)


looking_files(path)

print('--DIRS for delete:' + str(dirs))
prinitng_files(dirslist)
print('\n---FILES for delete:' + str(files))
prinitng_files(fileslist)

#shutil.copytree(path,copypath)
#shutil.rmtree(path)
print('\nDeleting files ...')
for i in range(90000+1):
    progbar(i, 90000, 20)
print()
print('\n... OK\n')