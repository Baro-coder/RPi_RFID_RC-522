import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def main():
    reader = SimpleMFRC522()
    try:
        id, text = reader.read()
        print(id)
        print(text)
    finally:
            GPIO.cleanup()

if __name__ == '__main__':
    main()
