#In order for a raspbery pi to use the nfc reader the spi interface spi_bcm2835 must be loaded
# to do this - lsmod | grep spi
# We will use the mfrc522 library - https://pypi.org/project/mfrc522/

'Following pinout must be followed: - as per https://pimylifeup.com/raspberry-pi-rfid-rc522/
#    SDA connects to Pin 24.
#    SCK connects to Pin 23.
#    MOSI connects to Pin 19.
#    MISO connects to Pin 21.
#    GND connects to Pin 6.
#    RST connects to Pin 22.
#    3.3v connects to Pin 1.



from time import sleep
import sys
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt: # Will capture the ctrl+c closing and cleanup+exit 
    GPIO.cleanup()
    sys.exit()
     