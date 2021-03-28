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
        f = open(folder+"/config/config.txt", "r")
        devlist=[]
        for i in f.readlines():
            if("Device: " in i):
                devlist.append(i[8:len(i)-1])
        window["-devlist-"].update(devlist)

    elif event=="-devlist-":
        device=(values["-devlist-"])

    elif event=="-generate-":
        line="Device: "+device[0]+"\n"
        peace=False
        f = open(folder+"/config/config.txt", "r")
        for i in f.readlines():
            if i=="Include: peace.txt\n":
                peace=True
        if(peace):
            f.close()
            f=open(folder+"/config/peace.txt","r")
        else:
            f = open(folder+"/config/config.txt", "r")
        tmp=[]
        lastdev="Device: "+device[0]+"\n"
        devfound=False
        convdev=[]
        for i in f.readlines():   
            print(i) 
            if i==line:
                if(i[-12:-1]=="; Benchmark"):
                    tmp.append(i)
                else:
                    tmp.append(i[0:-1]+"; Benchmark\n")
                devfound=True
                lastdev=i
            elif i[0:4]=="Conv":
                if(lastdev in convdev):
                    print("ignore")
                else:
                    convdev.append(lastdev)
                    if(devfound):
                        convolution=True
                        convfile=norm(i[13:len(i)])
                        print(convfile)
                        sr=wavfile.read(folder+convfile)[0]
                tmp.append(i)
            elif i[0:3]=="Dev":
                devfound=False
                lastdev=i
                tmp.append(i)
            else:
                if(i[-12:-1]=="; Benchmark"):
                    tmp.append(i[0:-12]+"\n")
                else:
                    tmp.append(i)
        f.close()

        temp = open('temp', 'w')
        for i in tmp:
            temp.write(i)
        temp.close()

        if(peace):
            shutil.move('temp', folder+"/config/peace.txt")
        else:
            shutil.move('temp', folder+"/config/config.txt")
        try:
			subprocess.run(folder+"/Benchmark.exe -c 1 -t 24000 -l 48 -r "+str(sr)+" -o ssweep.wav",timeout=1)
		except subprocess.TimeoutExpired:
			print("ok")

        subprocess.call("py periodogram.py")

        shutil.move("myresult/ssweep/ssweep GraphicEQ.txt", "GraphicEQ.txt")

        break
    # End program if user closes window 
    elif event == sg.WIN_CLOSED:
        break
window.close()