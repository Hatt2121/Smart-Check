# Smart-Check

Smart check is a simple project whose aim is to ease peoples lives. It is really hard to manage and maintain inventory in a world where consistancy counts, and Smart-Check is here to solve that.

## Prerequisites
The [`mfrc522`](https://pypi.org/project/mfrc522/) python library.

The [`imbox`](https://pypi.org/project/imbox/) python library.

## The Code
Other than the libraries, the actual files that we use are [`mailing.py`](mailing.py) and [`Smart_Check_GUI.py`](Smart_Check_GUI.py). We have gone through many changes and iterations of the project, and we have landed on these two files. Starting is as simple as runing 'Smart_Check_GUI.py' in an IDLE or in the console.

## Wiring:
For ease of reference

### 4.2 E-Ink Screen
Deprecated!!
| Output | Physical Pin |
|----|----|
|3.3V|1|
|GND|6|
|DIN|19|
|CLK|23|
|CS|24|
|DC|22|
|RST|11|
|BUSY|18|

### RFID Scanner: RC522

| Output | Physical Pin |
| ---- | ---- | 
| SDA | 24 |
| SCK | 23 | 
| MOSI | 19 |
| MISO | 21 |
| IRQ | UNUSED |
|GND | 6 |
| RST | 22 |
| 3.3V | 1 |
