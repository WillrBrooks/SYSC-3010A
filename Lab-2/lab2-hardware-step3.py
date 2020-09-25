#for hardware configuration look in the readme file in this directory

from gpiozero import Button
from gpiozero import LED
from time import sleep

boardButton = Button(2)
LEDControl = LED(3)

while True:
	sleep(0.1)
	if boardButton.is_pressed:
		LEDControl.on()
	else:
		LEDControl.off()
	

