# convtographiceq
Initial release(28 March 2021): Only supports 48khz EQ APO config. Please switch the sample rate first. Other sample rates support will be updated.

For converting Equalizer Apo (or Peace) config to CSV for AutoEQ. This makes it possible to generate Graphic Eq for Wavelet (Non-Root Android Eq) and others.
https://i.imgur.com/fjK8muf.png

Before use, please download python and get pip:
https://phoenixnap.com/kb/install-pip-windows

How to use:
1. Open `rungui.bat`
2. Select folder of EqualizerAPO installation
3. Select the device which have the eq on
4. Press OK
5. Switch to the command line window, press any key
6. Wait until the program closes
7. Take the `GraphicEQ.txt` file and import to wavelet

Please report any issues you encountered. Any contributions to improve the GUI will be appreciated. 
This GUI currently works for Parametric EQ and Convolution EQ in APO without any non-filter or preamp commands (Copy, delay, etc).