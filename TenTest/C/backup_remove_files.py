#http://senkler.blogspot.com/2011/04/python.html

#УДАЛЕНИЕ ФАЙЛОВ
#http://qaru.site/questions/10880/how-to-delete-a-file-or-folder

#Рекурсия и обход каталогов
#https://www.youtube.com/watch?v=wZvk8nyPQCY

#прогресс бар 
#http://dmitrym.ru/blog/all/progress-bar-na-pitone-v-konsoli/
#http://zetblog.ru/python-kak-sdelat-progress-bar-v-konsole.html

#https://elekt.tech/python/useful-python/progress_bar_in_console_in_python.html

import os,time,sys,shutil
#shutil
#import sys
#import time

path = '/home/dmtr/_SANDBOX/Tensor_Test/C_py/fordel'#указываем путь до директории
copypath = '/home/dmtr/_SANDBOX/Tensor_Test/C_py/copy_of_fordel'#указываем путь до директории
dirs = 0
files = 0
dirslist = []
fileslist = []


def progbar(curr, total, full_progbar):
    frac = curr/total
    filled_progbar = round(frac*full_progbar)
    print('\r', '#'*filled_progbar + '-'*(full_progbar-filled_progbar), '[{:>7.2%}]'.format(frac), end='')

def looking_files(path,level=1):
	"""Ходит по каталогам, определяет тип файлов"""
	#print('Level=',level,'Content:',os.listdir(path))
	global dirs,files
	#print(os.listdir(path))
	for i in os.listdir(path):
		if os.path.isdir(path+'/'+i):
			dirs+=1
			dirslist.append(path + '/' + i)
			#print('___Down to directory:',path+'/'+i)
			looking_files(path+'/'+i,level+1)
			#print('<Up',path)

		else:
			fileslist.append(path+'/'+i)
			files+=1

def prinitng_files(filelist):
	for i in filelist:
		print(i)

 


looking_files(path)

print('--DIRS for delete:' + str(dirs))
prinitng_files(dirslist)
print('\n---FILES for delete:' + str(files))
prinitng_files(fileslist)

#shutil.copytree(path,copypath)
#shutil.rmtree(copypath)
print('\nDeleting files ...')
for i in range(90000+1):
    progbar(i, 90000, 20)
print()
print('\n... OK\n')
