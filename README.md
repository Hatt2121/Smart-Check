# Smart-Check

Smart check is a simple project dedicated to inventory management in a time where there are an abundant amount of passive RFID tags, and low power E-Ink screens. This project is dedicated to creating a simple experience for those managing other's contents in a situation where they are trying to micromanage their lives. 

## Wiring:

### 4.2 E-Ink Screen

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
