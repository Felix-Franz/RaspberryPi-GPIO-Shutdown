# RaspberryPi GPIO Shutdown
A small python program that shuts down a RaspberryPi after connecting GPIO pin 3 to GND.


## Download
Just download or copy the code of this little software: [Download](https://github.com/Felix-Franz/RaspberryPi-GPIO-Shutdown/blob/master/GPIO_Shutdown.py) <br>
Save it anywhere on your pi.


## Requirements
You only need python and RPi.GPIO.<br>
If you are running Raspbian everything should be installed!
If python is not installed you only need to do this:
<pre>
sudo apt-get update
sudo apt-get install python
</pre>
<br>
To install [RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO) run following commands:
<pre>
sudo apt-get update
sudo apt-get install rpi.gpio
</pre>
If that doesn't work use this.
If 0.6.2 is not the latest version copy the download link from here: [https://pypi.python.org/pypi/RPi.GPIO](https://pypi.python.org/pypi/RPi.GPIO)
<pre>
sudo apt-get install python-dev gcc
wget https://pypi.python.org/packages/c1/a8/de92cf6d04376f541ce250de420f4fe7cbb2b32a7128929a600bc89aede5/RPi.GPIO-0.6.2.tar.gz
tar -xvf RPi.GPIO-0.5.11.tar.gz
cd RPi.GPIO-0.6.1
sudo python setup.py install
cd ..
sudo rm -rf RPi.GPIO-0.*
</pre>


## Run it!
Just navigate with your terminal to your downloaded file and run
<pre>python GPIO_Shutdown.py</pre>
 Replace the _GPIO_Shutdown.py_ with your filename.
 
 You may need to run it as root:
 <pre>sudo python GPIO_Shutdown.py</pre>
 <br>
 
Connect pin3 to the GND pin next to it (for example with a paperclip). Then the RaspberryPi starts to shutdown.<br>
If you are not sure about what pin is the right one, just look at the [RaspberryPi Website](https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/README.md).<br>
Be sure to use the right pin, using the wrong one may cause a damnage of your RaspberryPi!


## Additional configuration
If you want to use another pin than pin3 just change the 3 after _GPIO_Pin_ in the file
It may look like this:
<pre>
...
GPIO_Pin = 5
GPIO.setmode(GPIO.BCM)
...
</pre>


## Run on startup
To run it automatically after the startup of RaspberryPi, you just have to add following line above _exit 0_ to _/etc/rc.local_.<br>
You have to replace _path\_to\_file_ with your own path to your downloaded file.
<pre>python /path_to_file/GPIO_Shutdown.py &</pre>


## Uninstallation
Just remove your downloaded file and the line in _/etc/rc.local_<br>
If you do not need python anymore use:
<pre>sudo apt-get purge python</pre>


<br><br>
> I hope this helped you a bit.<br>
> Have fun with this small software.
