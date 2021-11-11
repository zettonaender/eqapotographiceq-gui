import PySimpleGUI as sg
import os
import subprocess
import shutil
import time
from scipy.io import wavfile
import scipy.fft as fftp
import numpy as np

def norm(a):
    tmp=""
    idx=0
    for i in a:
        if i=="\\":
            tmp=tmp+"/"
        elif idx==len(a)-4:
            tmp=tmp+i
        elif i=="." or i=="\n":
            tmp=tmp+""
        else:
            tmp=tmp+i
        idx=idx+1
    return tmp

def bench(sampler):
    if(sampler==48000):
        try:
            subprocess.run(folder+"/Benchmark.exe -i dirac24_48_mono.wav -o ssweep.wav",timeout=1)
        except subprocess.TimeoutExpired:
            print("")
    elif(sampler==44100):
        try:
            subprocess.run(folder+"/Benchmark.exe -i dirac24_44_mono.wav -o ssweep.wav",timeout=1)
        except subprocess.TimeoutExpired:
            print("")
    elif(sampler==192000):
        try:
            subprocess.run(folder+"/Benchmark.exe -i dirac24_192_mono.wav -o ssweep.wav",timeout=1)
        except subprocess.TimeoutExpired:
            print("")
    sr,data=wavfile.read("ssweep.wav")
    arr=fftp.rfft(data,sr)
    freq=fftp.rfftfreq(len(arr)*2,1/sr)
    arr=20*np.log10(abs(arr))
    freq=freq[:-1].copy()
    broken=False
    for i in arr:
        i=str(i)
        if(i=="-inf"):
            broken=True
    if broken:
        bench(sampler)

layout = [
    [
        sg.Text("Please select Equalizer Apo installation folder."),
        sg.In(size=(25, 1), enable_events=True, key="-folder-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 5), key="-devlist-"
        ),
        
    ],    
    [
        sg.Listbox(
            values=[44100,48000,192000], enable_events=True, size=(40, 3), key="-samplerate-"
        ),
        
    ],   
    [
        sg.Text("Please select output folder."),
        sg.In(size=(25, 1), enable_events=True, key="-outfolder-"),
        sg.FolderBrowse(),
    ],
    [
            sg.Text("Click OK to generate."),
            sg.Button("OK", key="-generate-"),
    ],
]

#Create the window
window = sg.Window("EQ APO to Graphic EQ GUI", layout)

device=""
# Create an event loop
while True:
    event, values = window.read()
    if event=="-folder-":
        folder=values["-folder-"]
        f = open(folder+"/config/Peace.txt", "r")
        devlist=[]
        for i in f.readlines():
            if("Device: " in i):
                devlist.append(i[8:len(i)-1])
        if len(devlist)==0:
            tmp=[]
            f=open(folder+"/config/Peace.txt","r")
            tmp.append("Device: all\n")
            for i in f:
                tmp.append(i)
            temp=open('temp','w')
            for i in tmp:
                temp.write(i)
            devlist.append("all")
            temp.close()
            shutil.move('temp', folder+"/config/Peace.txt")
        window["-devlist-"].update(devlist)
    elif event=="-outfolder-":
        outfolder=values["-outfolder-"]
    elif event=="-devlist-":
        device=(values["-devlist-"])
    elif event=="-samplerate-":
        samplerate=(values["-samplerate-"])
    elif event=="-generate-":
        shutil.copy(folder+"/config/Peace.txt","orig")
        f=open(folder+"/config/Peace.txt","r")
        dev=device[0]
        print(dev)
        tmp=[]
        for i in f:
            if "Device: " in i:
                if dev in i:
                    if "Benchmark" not in i and not dev=="all":
                        tmp.append(i[:-1]+"; Benchmark\n")
                        tmp.append("Preamp: -15 dB\n")
                    else:
                        tmp.append(i)
                        tmp.append("Preamp: -15 dB\n")
                else:
                    if "Benchmark" in i and not dev=="all":
                        tmp.append(i[:-12]+"\n")
                    else:
                        tmp.append(i)
            else:
                tmp.append(i)
        f.close()
        temp = open('temp', 'w')
        for i in tmp:
            temp.write(i)
        temp.close()
        shutil.move('temp', folder+"/config/Peace.txt")
        bench(samplerate[0])
        subprocess.call("py ok.py")
        try:
            os.mkdir(outfolder+'/ssweep')
        except OSError:
            print ('')
        shutil.rmtree(outfolder+'/ssweep')
        shutil.move("myresult/ssweep", outfolder)
        shutil.copy("orig",folder+"/config/Peace.txt")
        break
    # End program if user closes window 
    elif event == sg.WIN_CLOSED:
        break
window.close()