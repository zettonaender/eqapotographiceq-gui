filename='ssweep'
length=1
showplot=False

import csv
from scipy.io import wavfile
from matplotlib import pyplot as plt
from scipy.signal import periodogram
import numpy as np
import os

def normalize(arr):
	mx=max(arr)
	for i in range(0,len(arr)):
		arr[i]/=mx
	return arr

def todb(a):
	for i in range(0,len(a)):
		a[i]=20*np.log10(np.abs(a[i]))
	return a

def trim(a,b):
	freq=[]
	arr=[]
	for i in range(0,len(a)):
		if(a[i]>=20 and a[i]<=22000):
			freq.append(a[i])
			arr.append(b[i])
	arr=normalize(arr)
	arr=todb(arr)
	mn=np.min(arr)
	for i in range(0,len(arr)):
		arr[i]=(arr[i]-mn)/(-1)
	return [freq,arr]

def doeq():
	import autoeq as eq
	eq.batch_processing(input_dir=filename,output_dir='myresult/'+filename,standardize_input=True,compensation='zero.csv',equalize=True,show_plot=showplot)
	print('===============================================')
	print('Graphic EQ generated. Check myresult/'+filename)

sr1,data1=wavfile.read(filename+'.wav')

data1=data1.copy()

data1=periodogram(data1)[1]
data1=np.sqrt(data1)
data1=normalize(data1)

freq=[]
for i in range(1,len(data1)+1):
	freq.append(i*(1000/length)/sr1)

freq,data1=trim(freq,data1)

if(showplot):
	plt.plot(freq,data1)
	plt.show()

try:
    os.mkdir(filename+'/')
except OSError:
    print ('Folder already exist, ignore this.')
try:
    os.remove(filename+'/'+filename+'.csv')
except OSError:
    print ('File not found, ignore this.')
with open(filename+'/'+filename+'.csv', mode='w', newline='') as output:
	writer=csv.writer(output,delimiter=',')
	writer.writerow(['frequency','raw'])
	for i in range(0,len(freq)):
		writer.writerow([freq[i],data1[i]])

doeq()