# py-qrcode

`py-qrcode` is a tool written in Python useful to detect QRCode from camera using [OpenCV-Python](https://opencv-python-tutroals.readthedocs.io/en/latest/index.html) and [pyzbar](https://pypi.org/project/pyzbar/)

## Usage 
Required Python 3.7 and [pyzbar](https://pypi.org/project/pyzbar/) using 

MacOS X:
```bash
brew install zbar
```

Linux:
```bash
sudo apt-get install libzbar0
```

Clone this repository using the following command
```bash
git clone https://github.com/lorenzodisidoro/py-qrcode.git
```

and install dependencies
```bash
cd py-qrcode && pip3 install -r requirements.txt
```

## Start scanning

Use following command to detect from camera 
```bash
python3 py-qrcode.py
```

or decode from image file
```bash
python3 py-qrcode.py -f /local/path/qrcode_img.jpg
```