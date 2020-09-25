Lab 2 Read me document

This directory contains the files relevant to Lab 2 for SYSC 3010.

Lab 2 pertains to interfacing the RPI with hardware and writing to a 
ThingSpeak channel.

Part 1

Step 1

The python file relevant to step on of part 1 is called:

Lab2-hardware-step1.py

This file controls a sense hat on the RPI and changes between a W an a B
when the joystick is moved.

Step 3

For the purposes of this lab the hardware connected to the pi is configured 
as below:


      +3.3V
      -----
        |
        /
        \ 330 ohm
        /  
        \
        |
        |
     -------
     |     |
     | LED |
     |     |
     -------
        |
        |
     -------
     |     |    --------------
     | NPN |---| 10k resistor |--- GPIO 3
     |     |    --------------

     -------
        |
        |
      _____
       ___
        _


      +3.3V
      -----
        |
        |
        /
        \
        /  10k
        \
        /
        |
        |----- GPIO 2
        |
        \
         \   <-- switch
          \
        |
        |
      _____
       ___
        _


The python program Lab2-hardware-step3.py causes the LED to turn on when the
switc is pressed.

Part 2
