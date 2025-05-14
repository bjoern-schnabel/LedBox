# LED-Box Students guide

## Accessing the LED-Box. 

* In your classroom, there should be a open wifi hotspot called `LED-Box-WiFi`. Connect to it.
  * Do not connect to `LED-Box-WiFi 2`, unless the other one is not working
* If you are on a mobile device, make shure to **disable your cellular data**. If you are plugged in via ethernet, **disable the ethernet link**
* In your browser, access `led-box.bbrouter`. Do not try to access `https://led-box.bbrouter`
* Log in with your unique user name. If you have not logged into the LED-Box before, you can just type any unique name.

## Writing your programs

* The LED-Box runs on python. your programs should therefore be python files.

### Special libraries

* all special libraries are consolidated under the `ulib` library

#### display

* `from ulib import display`
* colors are represented as a 3-tupel of shape `(<red>,<green>,<blue>)` where values reach between 0 and 255.
* positions are represented as a 2-tupel of shape `(<y>,<x>)` where values reach between 0 and 15.

##### fill

* `display.fill(<color>)`
* sets the entire display to the selected color and immidiately shows it
* Example: `display.fill((100,0,0))` fills the entire display red.

##### set_xy

* `display.set_xy(<position>,<color>)`
* sets the pixel at the selected coordinate to the selected color. Does not immediately show. See `display.show()`.
* Example: `display.set_xy((2,4),(0,0,100))` sets the pixel at x=4, y=2 to blue.

##### show

* `display.show()`
* Applies all modifications done by set operations to the display

##### set_m

* `display.set_m(<position_dict>)`
* Sets a multitude of pixels to their assigned color and immediately shows the display.
* `position_dict` is a Dictionary, where the keys are the positions of the pixels that should be set and the values are the color. 
* Example: `display.set_m({(2,2):(100,100,0),(4,4):(0,100,0)})` sets pixel 2,2 to yellow and pixel 4,4 to green

##### fade

* `display.fade(<multipliers>)`
* Multiplies the colors of all pixels with their respective selected multiplier and immediately shows the result.
* `multipliers` is a 3-tupel of shape `(<red_mult>,<green_mult>,<blue_mult>)`
* Example: `display.fade(0,0.5,1)` turns the red channel off, fades the green and leaves blue untouched.

#### remote

* `from ulib import remote`
* Allows binding functions to a udp package receiver
* The `remote.py` script allows sending a keyboard input via udp to the led-box and thus allows using your PCs keybord as input in your LED-Box program

##### listen

* `remote.listen()`
* starts the udp receiver

##### bind_key

* `remote.bind_key(<key>,<function>)`
* Whenever the udp receiver receives a message that mathes `key`, the `function` is called and the received message is passed to the function
* Example: `remote.bind_key("A", print)` calls the builting print function whenever, an "A" is received (whenever the user presses *A* on their keyboard). This will print "A" to the console, everytime "A" is pressed

##### bind_all

* `remote.bind_all(<function>)`
* Whenever the udp receiver receives a message, the `function` is called and the received message is passed to the function
* Example: `remote.bind_all(print)` calls the builting print function whenever, a message is received (whenever the user presses any key on their keyboard). This will print the received message to the console.

##### unbind_key

* `remote.unbind_key(<key>,<function>)`
* The `function` will no longer be called when the udp receiver receives a message that mathes `key`.
* Example: `remote.unbind_key("A", print)` will stop calling the inbuild print function, when an "A" is received.

##### unbind_all

* `remote.unbind_all(<function>)`
* The `function` will no longer be called when the udp receiver receives a message.
* Example: `remote.unbind_all(print)` will stop calling the inbuild print function, when a message is received.