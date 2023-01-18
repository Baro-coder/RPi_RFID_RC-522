import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

def main():
    reader = SimpleMFRC522()
    
    try:
        print('Place your tag to read...')
        id, data = reader.read()
        print(f'ID:     {id}')
        print(f'DATA:   {data}')
    finally:
            GPIO.cleanup()

if __name__ == '__main__':
    main()
