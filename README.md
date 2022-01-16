Update (16 January 2022):
- Fixed the most annoying bug with benchmark clipping, resulting in wobbly mess in the output
- Fixed requirements to not need python 3.7 only
Will probably release an executable soon.

Update (11 November 2021): 
-Added output folder option
-Added safeguards for clipping
-Added fix for "samples clipped!" error in EQ APO Benchmark

For converting Equalizer Apo (or Peace) config to Graphic EQ for Wavelet. https://i.imgur.com/O6lKxec.png

Before use, please download Python version>=3.7 and get pip: https://phoenixnap.com/kb/install-pip-windows

After you got pip working, Press Code->Download zip and extract.

How to use:

1. Open rungui.bat or runguipeace.bat if you use Peace
2. Select folder of EqualizerAPO installation
3. Select the device which have the eq on
4. Select device sample rate (when in doubt just choose 48000).
5. Select output folder
6. Press OK
7. Wait until the program finishes, the GraphicEQ.txt file will be in OutputFolder/ssweep
8. Take the GraphicEQ.txt file and import to wavelet

Please report any issues you encountered. This GUI currently works for Parametric EQ and Convolution EQ in APO without any non-filter or preamp commands (Copy, delay, etc).

AutoEQ code taken from https://github.com/jaakkopasanen/AutoEq
