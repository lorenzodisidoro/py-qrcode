import sys
import cv2
import imutils
from PIL import Image
from pyzbar.pyzbar import decode, ZBarSymbol

# @function 'detect_qr' detect and decode qrcode from frame using pyzbar lib
# @param 'inputFrame' type <class 'numpy.ndarray'>
# @return if detected type 'bool'
def detect_qr(inputFrame):
    img = Image.fromarray(inputFrame)
    decodedImg = decode(img, symbols=[ZBarSymbol.QRCODE])

    if len(decodedImg) > 0:
        decodedBytes = decodedImg[0].data
        stringData = decodedBytes.decode("utf-8")
        print("QRCode content:")
        print(stringData)

        return True
    else:
        return False

if len(sys.argv)>1:
    args = sys.argv[1:]

    if args[0] == "-f":
        inputImage = cv2.imread(args[1])
        frame = imutils.resize(inputImage, width=400)
        print(detect_qr(frame))
    else:
        print("An error occurred when parsing arguments")
else:
    cam = cv2.VideoCapture(0)
    qrDecoder = cv2.QRCodeDetector()
    cv2.namedWindow("QRCode detector")
    img_counter = 0

    # waiting to capture
    print("Waiting to scan a QRCode")
    undetected = False
    while not(undetected):
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break

        resizedFrame = imutils.resize(frame, width=400)
        cv2.waitKey(1)
        undetected = detect_qr(resizedFrame)
    
    cam.release()
    cv2.destroyAllWindows()
