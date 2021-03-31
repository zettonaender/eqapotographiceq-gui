import PySimpleGUI as sg
import os
import subprocess
import shutil
from scipy.io import wavfile

sr=48000

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

layout = [
    [
        sg.Text("Please select Equalizer Apo installation folder."),
        sg.In(size=(25, 1), enable_events=True, key="-folder-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-devlist-"
        ),
        
    ],    
    [
            sg.Text("Please select device to generate from and press OK."),
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
        f = open(folder+"/config/peace.txt", "r")
        devlist=[]
        for i in f.readlines():
            if("Device: " in i):
                devlist.append(i[8:len(i)-1])
        if len(devlist)==0:
            tmp=[]
            f=open(folder+"/config/peace.txt","r")
            tmp.append("Device: all\n")
            for i in f:
                tmp.append(i)
            temp=open('temp','w')
            for i in tmp:
                temp.write(i)
            devlist.append("all")
            temp.close()
            shutil.move('temp', folder+"/config/peace.txt")
        window["-devlist-"].update(devlist)

    elif event=="-devlist-":
        device=(values["-devlist-"])

    elif event=="-generate-":
        f=open(folder+"/config/peace.txt","r")
        dev=device[0]
        tmp=[]
        for i in f:
            if "Device: " in i:
                if dev in i:
                    if "Benchmark" not in i and not dev=="all":
                        tmp.append(i[:-1]+"; Benchmark\n")
                    else:
                        tmp.append(i)
                else:
                    tmp.append(i)
            else:
                tmp.append(i)
        temp = open('temp', 'w')
        for i in tmp:
            temp.write(i)
        temp.close()
        shutil.move('temp', folder+"/config/peace.txt")
        try:
            subprocess.run(folder+"/Benchmark.exe -c 1 -t 24000 -l 48 -r "+str(sr)+" -o ssweep.wav",timeout=1)
        except subprocess.TimeoutExpired:
            print("")

        subprocess.call("py periodogram.py")

        shutil.move("myresult/ssweep/ssweep GraphicEQ.txt", "GraphicEQ.txt")

        break
    # End program if user closes window 
    elif event == sg.WIN_CLOSED:
        break
window.close()