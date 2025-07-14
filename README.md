# flowerdle
[overall](https://github.com/mynameisashllee/flowerdle/blob/main/overall.png?raw=true)

## description
flowerdle is a real life two player wordle game - but instead of letters, there's minecraft flowers! and instead of one person, there's two! compete in a fierce race to guess the right flowers... or perish by pollen. just kidding.

## how it works
there are four flowers - tulips (pink), poppies (red), oxeye daisies (white) and cornflowers (blue). each flower has a resistor of different resistance inside it to distinguish them. the resistors are held below each flower stem with a case, with pins poking out the bottom so you can plant them into the breadboard.
[flower](https://github.com/mynameisashllee/flowerdle/blob/main/flower.png?raw=true)

at the start, the firmware generates a random four-colour code. the aim for both players is to guess the correct order of the colours in the least amount of tries.

there are 2 breadboards for players with spaces to put the flowers and leds (red and green).
[breadboards](https://github.com/mynameisashllee/flowerdle/blob/main/breadboards.png?raw=true)

and there's a breadboard for the oled display.
[oled](https://github.com/mynameisashllee/flowerdle/blob/main/oled.png?raw=true)

on each turn, you plug in all four flowers for your guess. then, the led lights up green or red based on whether the guess for that slot is correct or wrong, respectively.
[leds](https://github.com/mynameisashllee/flowerdle/blob/main/img/leds.png?raw=true)

once your turn is done, it increments the number of tries on the display. whoever gets the code correct first wins! 
[winner](https://github.com/mynameisashllee/flowerdle/blob/main/img/winner.png?raw=true)

## schematic
[schematic](https://github.com/mynameisashllee/flowerdle/blob/main/img/schematic.png?raw=true)

## directory
📁 src
│
├── 📂 [cad](src/cad)
│   ├── 📄 [case cads](src/cad/breadboard_case)
│   └── 📄 [flower cads](src/cad/flowers)
│   └── 📄 [flower base cads](src/cad/structures)
│
├── 📂 [firmware](src/firmware)
│   ├── 📄 [code.py](src/firmware/code.py)
│
└── 📂 [schematic](src/schematic)
│   └── 📄 kicad files
│
└── 📄 [bom](src/bom.md)