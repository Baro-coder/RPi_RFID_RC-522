# RPi RFID RC-522

### Raspberry Pi RFID reader/writer

---

## Modules

#### - Raspberry Pi

#### - RFID RC522

---

## Wiring

![image](https://user-images.githubusercontent.com/74451381/213295948-ecebbc7c-2ee1-4bf0-a95e-f517375678db.png)

*Wiring image is downloaded from [pimylifeup.com](https://pimylifeup.com/raspberry-pi-rfid-rc522/)*

- SDA connects to Pin 24.
- SCK connects to Pin 23.
- MOSI connects to Pin 19.
- MISO connects to Pin 21.
- GND connects to Pin 6.
- RST connects to Pin 22.
- 3.3v connects to Pin 1.

---

## Raspbian set up

1. Enable SPI interface

```
  sudo raspi-config
```

Interfacing Options -> SPI -> Enable

2. Reboot

```
  sudo reboot
```

3. Check if the SPI is enabled
```
  lsmod | grep spi
```

4. Installation:
  
  - Change directory:
  
```
  cd ???/RPi_RFID_RC-522/
```

  - Run install script
  
```
  ./install.sh
```

5. Run program:
  
  - reader:

```
  python3 rfid-reader.py
```
  
  - writer:
```
  python3 rfid-writer.py
```
