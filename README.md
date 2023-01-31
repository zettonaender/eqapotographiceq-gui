
# A tool for converting Equalizer Apo (or Peace) config to Graphic EQ for Wavelet. 
![Image](https://i.imgur.com/O6lKxec.png)

## Update (31 January 2023):
- Added note for wiggle fix. Will release an update soon for the release exe.

# Executable download at
https://github.com/zettonaender/eqapotographiceq-gui/releases/tag/build

# Read this if you get wiggles in the result:
We use Equalizer APO benchmark which writes a 16 bit wav file. Due to rounding error, you'll get wiggles if the dB gain is low (-20dB or less). To fix this, copy the 'Benchmark.exe' file from this page to the Equalizer APO folder. This modified exe writes a 24 bit wav file instead which fixes the wiggles.

# How to use:
1. Select folder of EqualizerAPO installation
2. Select the device which have the eq on
3. Select device sample rate (when in doubt just choose 48000).
4. Select output folder
5. Press OK
6. Wait until the program finishes, the GraphicEQ.txt file will be in OutputFolder/ssweep
7. Take the GraphicEQ.txt file and import to wavelet

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
