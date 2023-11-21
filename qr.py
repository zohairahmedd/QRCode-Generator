import qrcode

qr = qrcode.QRCode(version = 1, # sets version of QR code determining size of QR code
                   error_correction = qrcode.constants.ERROR_CORRECT_L, # error correction level. if QR code is damaged, error correction level determines the amount of data that can be restored if the QR Code is damaged (pypi.org)
                   box_size = 20, # sets size of each module - module is single black or white square in QR code
                   border = 2) # size of border around QR code which are blank white spaces

qr.add_data("This QR Code was created by Zohair!") # data that QR code gives when scanned
qr.make(fit = True) # automatically detects size of QR code - this is the default but specified regardless 

img = qr.make_image(fill_color = "black", back_colour = "white") # colour of QR codes square and background
img.save("myQRCode.png") # save the QR code as a .png with any file name 