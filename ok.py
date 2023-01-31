import scipy.io.wavfile as wavfile
import matplotlib.pyplot as plt
import numpy as np
import scipy.fft as fftp
import scipy.interpolate as interpolate
import csv
import os
import shutil
from autoeq import batch_processing
showplot=False
def doeq():
	batch_processing(input_dir="ssweep",output_dir='myresult/'+"ssweep",standardize_input=True,compensation='zero.csv',equalize=True,show_plot=showplot)
	print('===============================================')
	print('Graphic EQ generated. Check -> Output Folder/'+"ssweep")

def startyourengine():
	sr,data=wavfile.read("ssweep.wav")
	arr=fftp.rfft(data)
	freq=fftp.rfftfreq(len(data),1/sr)
	arr=20*np.log10(abs(arr))

	freqarr=[]
	with open('zero.csv') as f:
		reader=csv.reader(f,delimiter=',')
		for i in reader:
			freqarr.append(i[0])
	x=interpolate.interp1d(freq,arr)
	arrnew=x(freqarr)
	arrnew=-1*arrnew
	with open('ssweep.csv', mode='w', newline='') as output:
		writer=csv.writer(output,delimiter=',')
		writer.writerow(['frequency','raw'])
		for i in range(0,len(freqarr)):
			writer.writerow([str(freqarr[i]),str(round(arrnew[i],2))])
	try:
		os.mkdir('ssweep/')
	except OSError:
		print ('')
	shutil.move('ssweep.csv','ssweep/ssweep.csv')
	doeq()