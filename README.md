
# A tool for converting Equalizer Apo (or Peace) config to Graphic EQ for Wavelet. 
![Image](https://i.imgur.com/O6lKxec.png)

## Update (6 April 2022):
- Released EXE file (need testing probably)

# Executable download at
https://github.com/zettonaender/eqapotographiceq-gui/releases/tag/build

# How to use:
1. Select folder of EqualizerAPO installation
2. Select the device which have the eq on
3. Select device sample rate (when in doubt just choose 48000).
4. Select output folder
5. Press OK
6. Wait until the program finishes, the GraphicEQ.txt file will be in OutputFolder/ssweep
7. Take the GraphicEQ.txt file and import to wavelet

Please report any issues you encountered. This GUI currently works for Parametric EQ and Convolution EQ in APO without any non-filter or preamp commands (Copy, delay, etc).

AutoEQ code taken from https://github.com/jaakkopasanen/AutoEq


## If you don't use the exe:
1. Before use, please download Python version>=3.7 and get pip: https://phoenixnap.com/kb/install-pip-windows
2. After you got pip working, Press Code->Download zip and extract.
3. Open rungui.bat or runguipeace.bat if you use Peace
