import pyqrcode
import png

your_link = "g"

url = pyqrcode.create(your_link)

img = "cuiatk.png"

url.png(img, scale=10)
