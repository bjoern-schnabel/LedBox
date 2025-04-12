from ulib import display_emu as display
from ulib import fancy
import time

points = fancy.hilbert()
print(points)

display.fill((0,0,255))
display.show()
#while display.max_value()[1] > (1, 1, 1):
for i in range(20):
	display.fade((0.9, 0.9, 0.9))
	time.sleep(0.1)

for y in range(0, display.height):
	for x in range(0, display.width):
		display.set_xy((x,y),(x*1.6, y*1.6, x*y/10))
		display.show()
for x in range(0, display.width):
	for y in range(0, display.height):
		display.set_xy((x,y),(0, 0, 0))
		display.show()

while True:
	for point in points:
		#print(point)
		display.set_xy((point[0],point[1]),(255, 255, 255))
		display.show()
		time.sleep(0.05)
		display.fade((0.9, 0.9, 0.95))
