# flowerdle
![overall](https://github.com/mynameisashllee/flowerdle/blob/main/img/overall.png?raw=true)

## description
flowerdle is a real life two player wordle game - but instead of letters, there's minecraft flowers! and instead of one person, there's two! compete in a fierce race to guess the right flowers... or perish by pollen. just kidding.

## youtube demo
[link](https://youtu.be/ab2HIsHCvx8)

## how it works
there are four flowers - tulips (pink), poppies (red), oxeye daisies (white) and cornflowers (blue). each flower has a resistor of different resistance inside it to distinguish them. the resistors are held below each flower stem with a case, with pins poking out the bottom so you can plant them into the breadboard.
![flower](https://raw.githubusercontent.com/mynameisashllee/flowerdle/refs/heads/main/img/flower.png)

at the start, the firmware generates a random four-colour code. the aim for both players is to guess the correct order of the colours in the least amount of tries.

there are 2 breadboards for players with spaces to put the flowers and leds (red and green).
![breadboards](https://raw.githubusercontent.com/mynameisashllee/flowerdle/refs/heads/main/img/breadboards.png)

and there's a breadboard for the oled display.
![oled](https://raw.githubusercontent.com/mynameisashllee/flowerdle/refs/heads/main/img/oled.png)

the breadboard cases have unfortunately not been printed as of shipping, but hopefully will be before project demos! check out how they will look in the [cad files](src/cad/breadboardcase).

on each turn, you plug in all four flowers for your guess. then, the led lights up green or red based on whether the guess for that slot is correct or wrong, respectively.
![leds](https://raw.githubusercontent.com/mynameisashllee/flowerdle/refs/heads/main/img/leds.png)

once your turn is done, it increments the number of tries on the display. whoever gets the code correct first with the least number of tries wins! 
![winner](https://raw.githubusercontent.com/mynameisashllee/flowerdle/refs/heads/main/img/winner.png)

## schematic
![schematic](https://raw.githubusercontent.com/mynameisashllee/flowerdle/refs/heads/main/img/schematic.png)

## journal
take a look at our daily journals at [journals](journal) and our process pictures at [pictures](journal/pics.md) (featuring food pics!).

## building files
* 📂 src
    * [📂 cad](src/cad)
        * [📄 case cads](src/cad/breadboardcase)
        * [📄 flower cads](src/cad/flowers)
        * [📄 flower base cads](src/cad/structures)
    * [📂 firmware](src/firmware)
        * [📄 code.py](src/firmware/code.py)
    * [📂 schematic](src/schematic)
        * 📄 kicad files
    * [📄 bom](src/bom.md)