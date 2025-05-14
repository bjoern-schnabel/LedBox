# LED-Box teachers guide

## Initial Setup (Linux [Ubuntu])

* On your device, please install *sshpass*. Open the command line and type `sudo apt install sshpass`
* Plug in the LED-Box and wait for the wifi network *LED-Box-WiFi* to appear. Connect to it. If you are connected via ethernet, **disable the ethernet connection**
* Connect to the LED-Box via *ssh*. In the command line type `ssh Doctor@led-box.bbrouter`. You will be asked if you trust the device. You trust the device.
* The ssh password is `Tardis`

## Recurring Setup (Linux [Ubuntu])

* Plug in the LED-Box and wait for the wifi to appear. Connect to the wifi.
* Open a new console and type `sshpass -p "Tardis" ssh Doctor@led-box.bbrouter "LedBox/startup.sh"` 
* The LED-Box now starts the server. You will see debug messages as well as output from the students programms in this terminal.
* Tell your students to connet to the LED-Box