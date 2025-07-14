# flowerdle
[photo]

## description
flowerdle is a real life two player wordle game - but instead of letters, there's minecraft flowers! and instead of one person, there's two! compete in a fierce race to guess the right flowers... or perish by pollen. just kidding.

## how it works
there are four flowers - tulips (pink), poppies (red), oxeye daisies (white) and cornflowers (blue). each flower has a resistor of different resistance inside it to distinguish them. the resistors are held below each flower stem with a case, with pins poking out the bottom so you can plant them into the breadboard.
[pic]

at the start, the firmware generates a random four-colour code. the aim for both players is to guess the correct order of the colours in the least amount of tries.

there are 2 breadboards for players with spaces to put the flowers and leds (red and green).
[pic]

and there's a breadboard for the oled display.
[pic]

on each turn, you plug in all four flowers for your guess. then, the led lights up green or red based on whether the guess for that slot is correct or wrong, respectively.
[pic]

once your turn is done, it increments the number of tries on the display. whoever gets the code correct first wins! 
[pic]

## schematic
[photos]

## bom
| Item                         | Amount |
| ---------------------------- | ------ |
| RP2040                       | 1      |
| Breadboard                   | 3      |
| 390 resistor                 | 16     |
| 1.2k resistor                | 8      |
| 2k resistor                  | 2      |
| 3.4k resistor                | 2      |
| 4.2k resistor                | 2      |
| 1.28" TFT LCD                | 1      |
| LED (Red)                    | 8      |
| LED (Green)                  | 8      |
| Diode                        | 8      |
| Jumper wires (male - female) | 26     |
| Jumper wires (male - male)   | 10     |
| Hot glue                     | lots   |
| 3D Print Filament            | lots   |