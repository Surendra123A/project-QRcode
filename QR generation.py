# Import QRCode from pyqrcode
import pyqrcode

#inputs

UserURL = str(input('Enter the URL: '))

nameOfQRfiles = str(input('enter the name of the QR Code file: '))

# Generate QR code
url = pyqrcode.create(f'{UserURL}')

# Create and save the svg file naming "myqr.svg"
url.svg(f"{nameOfQRfiles}.svg", scale = 10)

# Create and save the png file naming "myqr.png"
url.png(f'{nameOfQRfiles}.png', scale = 10)

