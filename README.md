# Smart-Check

Smart check is a simple project whose aim is to ease peoples lives. It is really hard to manage and maintain inventory in a world where consistancy counts, and Smart-Check is here to solve that.

## Prerequisites
The [`mfrc522`](https://pypi.org/project/mfrc522/) python library. Click the link to go to the pip page.

The [`imbox`](https://pypi.org/project/imbox/) python library. Click the link to go to the pip page.

## The Code
Other than the libraries, the actual files that we use are [`mailing.py`](mailing.py) and [`Smart_Check_GUI.py`](Smart_Check_GUI.py). We have gone through many changes and iterations of the project, and we have landed on these two files. Starting is as simple as runing 'Smart_Check_GUI.py' in an IDLE or in the console.

Tested, and it works on Python 3.5.3+.

## Wiring:
For ease of reference

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

### Other
| Output | Physical Pin |
| --- | --- |
| Red LED | 36 |
| Green LED | 16 |
