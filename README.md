# eqapotographiceq-gui
Bug Fixes(1 April 2021): Removed tensorflow requirements and using python 3.7 is not necessary anymore.

Only supports 48khz for Convolution EQ. Other sample rates support will be updated.

For converting Equalizer Apo (or Peace) config to CSV for AutoEQ. This makes it possible to generate Graphic Eq for Wavelet (Non-Root Android Eq) and others.
https://i.imgur.com/fjK8muf.png

Before use, please download python and get pip:
https://phoenixnap.com/kb/install-pip-windows

After you got pip working, Press Code->Download zip and extract.

How to use:
1. Open `rungui.bat` or `runguipeace.bat` if you use Peace
2. Select folder of EqualizerAPO installation
3. Select the device which have the eq on
4. Press OK
5. Wait until the program closes
6. Take the `GraphicEQ.txt` file and import to wavelet

Please report any issues you encountered. Any contributions to improve the GUI will be appreciated. 
This GUI currently works for Parametric EQ and Convolution EQ in APO without any non-filter or preamp commands (Copy, delay, etc).
