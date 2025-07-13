# day 2 - 12 jul (sat)
today, we woke up super early and split up tasks.

we did some cad and 3d printed the flowers! we decided on four colours according to the filament - dandelion for yellow, tulip for pink, cornflower for blue and rose for red. For the tulips, we printed out individual blocks and glued them together because it didnt need too many but for the rest we just patterned them in cad instead of assembling it to save on time. 
the bottom plate needed some adjustment because the resistor holes didn't print right, and the size was kind of off. so i guess that's a problem for tomorrow. 
Had 2 project demos today which went quite well, and we went through our 3d designs that were printed out as well as our firmware.
Turns out the other two were printed in the wrong colour and our adjusted bottom plate is yet to be printed so those two are a problem for tomorrow i guess
Right now we're relying on paint markers to fix the colour problems in case too many people need the 3d printers tomorrow
and thats it for the night. goodnight!

or probably not so fast, cus I just stayed up and try to get the firmware done.

It was a pretty serious problem: the pins are not enough.
So I go google for some details and found something worse: not only the GPIO pin are not enough, bout we only have 3 analog pins to read 4 analog data.
I searched online to see if I can find any solution. I also talked to Gemini. But after all, I decide I .have to share the pins.

This is basically how it's going to work.
First, I can use a main GPIO pin to provide power for the sensor, and then just read the values and cut it off and switch to the secondary GPIO pin and read the remaining value, and finally switch back to the original state.

I worked like till 4 am. so hope I can still lock in tomorrow. (PS I'm having too much caffeine I'm just want to sleep now.)