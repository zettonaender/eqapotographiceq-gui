
  

## A tool for converting Equalizer Apo (or Peace) config to Graphic EQ for Wavelet.

![Image](https://i.imgur.com/O6lKxec.png)

# Executable download at

https://github.com/zettonaender/eqapotographiceq-gui/releases/tag/build

  ### Update (31 January 2023):
- Updated to fix wiggles. Be sure to use the modified benchmark exe.

# How to use:

1. Copy the **Benchmark.exe** from this repository and paste it to Equalizer APO folder.

2. Download the [release](https://github.com/zettonaender/eqapotographiceq-gui/releases/tag/build2)

3. Select folder of EqualizerAPO installation

4. Select the device which have the eq on

5. Select device sample rate (when in doubt just choose 48000).

7. Select output folder

8. Press OK

9. Wait until the program finishes, the GraphicEQ.txt file will be in OutputFolder/ssweep

10. Take the GraphicEQ.txt file and import to wavelet

  

Please report any issues you encountered. This GUI currently works for Parametric EQ and Convolution EQ in APO without any non-filter or preamp commands (Channels, Copy, Delay, etc)

  

AutoEQ code taken from https://github.com/jaakkopasanen/AutoEq

  

## How to report a bug

1. Shift+right click inside the folder with 'gui.exe' and open terminal/cmd

2. Type 'gui' and enter

3. Any error will show up and you can post it via the "issue" tab on GitHub.

  
  

## If you don't use the exe:

1. Before use, please download Python version>=3.7 and get pip: https://phoenixnap.com/kb/install-pip-windows

2. After you got pip working, Press Code->Download zip and extract.

3. Open rungui.bat or runguipeace.bat if you use Peace
