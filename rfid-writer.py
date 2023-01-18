import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def main():
    reader = SimpleMFRC522()
    try:
        print('Insert new data to be written into tag:')
        data = input(' > ')
        print("\nNow place your tag to write...")
        reader.write(data)
        print("Data has been written.")
    finally:
            GPIO.cleanup()

if __name__ == '__main__':
    main()
